import customtkinter as ctk
import threading
import time
import socket
from datetime import datetime
from tkinter import ttk, messagebox

from scanner import scan_ports
from services import get_service
from ai_engine import get_scan_profile
from vulnerabilities import check_vulnerabilities
from os_detection import detect_os
from report_generator import export_pdf


class FastScanPro(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("FastScan Pro")
        self.geometry("1400x800")
        ctk.set_appearance_mode("dark")

        self.control = {"pause": False, "stop": False}
        self.scanned_count = 0
        self.total_ports = 0
        self.last_percent = -1
        self.start_time = 0
        self.scan_data = None
        self.live_open_ports = []

        # ================= TOP BAR =================
        top = ctk.CTkFrame(self)
        top.pack(fill="x", padx=10, pady=10)

        self.target = ctk.CTkEntry(top, width=220, placeholder_text="Target IP / Domain")
        self.target.pack(side="left", padx=10)

        self.scan_type = ctk.CTkOptionMenu(
            top,
            values=[
                "Quick Scan", "Full Scan", "Stealth Scan",
                "TCP Scan", "UDP Scan", "Intense Scan"
            ]
        )
        self.scan_type.pack(side="left", padx=10)

        self.speed = ctk.CTkOptionMenu(top, values=["Fast", "Medium", "Slow"])
        self.speed.pack(side="left", padx=10)

        self.custom_ports = ctk.CTkEntry(top, width=150, placeholder_text="Custom (80-100)")
        self.custom_ports.pack(side="left", padx=10)

        ctk.CTkButton(top, text="Start Scan", command=self.start_scan).pack(side="left", padx=10)
        ctk.CTkButton(top, text="Export PDF", command=self.export_report).pack(side="left", padx=10)

        # ================= STATUS =================
        status_frame = ctk.CTkFrame(self)
        status_frame.pack(fill="x", padx=10)

        self.status = ctk.CTkLabel(status_frame, text="Status: Idle")
        self.status.pack(side="left", padx=10)

        self.timer = ctk.CTkLabel(status_frame, text="Scan Time: 0s")
        self.timer.pack(side="right", padx=10)

        # ================= TABS =================
        self.tabs = ctk.CTkTabview(self)
        self.tabs.pack(fill="both", expand=True, padx=10, pady=10)

        self.output_tab = self.tabs.add("Scan Output")
        self.ports_tab = self.tabs.add("Ports & Services")
        self.vuln_tab = self.tabs.add("Vulnerabilities")
        self.host_tab = self.tabs.add("Host Details")

        self.output_box = ctk.CTkTextbox(self.output_tab)
        self.output_box.pack(fill="both", expand=True, padx=10, pady=10)

        # ===== DARK TABLE =====
        self.tree = ttk.Treeview(self.ports_tab, columns=("Port", "Status", "Service"), show="headings")

        self.tree.heading("Port", text="Port")
        self.tree.heading("Status", text="Status")
        self.tree.heading("Service", text="Service")

        self.tree.column("Port", width=100, anchor="center")
        self.tree.column("Status", width=120, anchor="center")
        self.tree.column("Service", width=200, anchor="center")

        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        # DARK STYLE
        style = ttk.Style()
        style.theme_use("default")

        style.configure("Treeview",
            background="#1e1e1e",
            foreground="white",
            fieldbackground="#1e1e1e",
            rowheight=28
        )

        style.configure("Treeview.Heading",
            background="#2b2b2b",
            foreground="white"
        )

        style.map("Treeview",
            background=[("selected", "#3a7ebf")]
        )

        self.vuln_box = ctk.CTkTextbox(self.vuln_tab)
        self.vuln_box.pack(fill="both", expand=True, padx=10, pady=10)

        self.host_box = ctk.CTkTextbox(self.host_tab)
        self.host_box.pack(fill="both", expand=True, padx=10, pady=10)

    # ================= HELPERS =================

    def resolve(self, target):
        try:
            return socket.gethostbyname(target)
        except:
            return target

    def update_timer(self):
        while not self.control["stop"]:
            if self.start_time:
                elapsed = int(time.time() - self.start_time)
                self.timer.configure(text=f"Scan Time: {elapsed}s")
            time.sleep(1)

    def insert_table_fast(self, results):
        batch_size = 500

        for i in range(0, len(results), batch_size):
            batch = results[i:i+batch_size]

            for port, status in batch:
                self.tree.insert("", "end", values=(port, status, get_service(port)))

            self.update_idletasks()

    # ================= START =================

    def start_scan(self):
        self.control = {"pause": False, "stop": False}
        self.scanned_count = 0
        self.last_percent = -1
        self.scan_data = None
        self.live_open_ports = []

        self.output_box.delete("1.0", "end")
        self.vuln_box.delete("1.0", "end")
        self.host_box.delete("1.0", "end")

        for row in self.tree.get_children():
            self.tree.delete(row)

        threading.Thread(target=self.run_scan).start()
        threading.Thread(target=self.update_timer).start()

    # ================= MAIN SCAN =================

    def run_scan(self):
        target_input = self.target.get()
        ip = self.resolve(target_input)

        profile = get_scan_profile(self.scan_type.get())

        speed = self.speed.get()
        if speed == "Fast":
            profile["threads"] = 800
            profile["timeout"] = 0.3
        elif speed == "Medium":
            profile["threads"] = 400
            profile["timeout"] = 0.7
        else:
            profile["threads"] = 200
            profile["timeout"] = 1.5

        if self.custom_ports.get():
            try:
                start, end = map(int, self.custom_ports.get().split("-"))
                ports = list(range(start, end + 1))
            except:
                ports = profile["ports"]
        else:
            ports = profile["ports"]

        self.total_ports = len(ports)
        self.start_time = time.time()

        self.output_box.insert("end", f"Scan Started: {target_input} ({ip})\n\n")

        results = scan_ports(ip, ports, profile, self.update_progress, self.control)

        self.control["stop"] = True

        open_ports = self.live_open_ports

        duration = int(time.time() - self.start_time)
        completed_time = datetime.now().strftime("%H:%M:%S")

        self.scan_data = {
            "target": target_input,
            "ip": ip,
            "scan_type": self.scan_type.get(),
            "duration": duration,
            "completed_time": completed_time,
            "open_ports": open_ports,
            "results": results,
            "services": {p: get_service(p) for p, _ in results},
            "issues": check_vulnerabilities(open_ports),
            "risk": "High" if open_ports else "Low"
        }

        self.output_box.insert("end", "\n===== SCAN COMPLETED =====\n\n")
        self.output_box.insert("end", f"Open Ports: {len(open_ports)} → {open_ports}\n")
        self.output_box.insert("end", f"Duration: {duration}s\n")

        # OPEN PORTS FIRST SORT
        sorted_results = sorted(results, key=lambda x: (0 if "OPEN" in x[1] else 1, x[0]))

        self.insert_table_fast(sorted_results)

        # VULNERABILITIES
        issues = check_vulnerabilities(open_ports)
        for issue in issues:
            self.vuln_box.insert("end", f"• {issue}\n")

        # HOST DETAILS
        os_name = detect_os(open_ports)

        self.host_box.insert("end", f"Target: {target_input}\nIP: {ip}\nOS: {os_name}\n")

        self.status.configure(text="Status: Completed")

    # ================= PROGRESS =================

    def update_progress(self, port, status):
        self.scanned_count += 1

        if status == "OPEN":
            self.live_open_ports.append(port)

        percent = int((self.scanned_count / self.total_ports) * 100)

        if percent in [25, 50, 75, 100] and percent != self.last_percent:
            self.last_percent = percent
            self.output_box.insert("end", f"Progress: {percent}%\n")
            self.output_box.see("end")

    # ================= PDF EXPORT =================

    def export_report(self):
        if not self.scan_data:
            messagebox.showwarning("Export Failed", "No scan data available")
            return

        threading.Thread(target=self._export_pdf_thread).start()

    def _export_pdf_thread(self):
        try:
            data = self.scan_data.copy()
            data["results"] = data["results"][:2000]  # LIMIT

            export_pdf("scan_report.pdf", data)

            messagebox.showinfo("Export", "PDF saved successfully")
            self.output_box.insert("end", "\n[✔] PDF exported\n")

        except Exception as e:
            messagebox.showerror("Error", str(e))