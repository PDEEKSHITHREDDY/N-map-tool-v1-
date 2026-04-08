import socket
from concurrent.futures import ThreadPoolExecutor, as_completed


# ===== TCP SCAN =====
def tcp_scan(target, port, timeout):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((target, port))
        sock.close()

        return port, "OPEN" if result == 0 else "CLOSED"
    except:
        return port, "FILTERED"


# ===== UDP SCAN =====
def udp_scan(target, port, timeout):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(timeout)
        sock.sendto(b"test", (target, port))
        sock.recvfrom(1024)
        sock.close()
        return port, "OPEN"
    except:
        return port, "OPEN|FILTERED"


# ===== SINGLE PORT DISPATCH =====
def scan_port(target, port, config):
    scan_type = config["scan_type"]

    if scan_type == "UDP":
        return udp_scan(target, port, config["timeout"])

    # Default TCP-based scan
    return tcp_scan(target, port, config["timeout"])


# ===== MAIN MULTITHREADED SCANNER =====
def scan_ports(target, ports, config, update_callback=None, control=None):

    results = []

    with ThreadPoolExecutor(max_workers=config["threads"]) as executor:
        futures = {
            executor.submit(scan_port, target, port, config): port
            for port in ports
        }

        for future in as_completed(futures):

            if control and control["stop"]:
                break

            # Pause support
            while control and control["pause"]:
                pass

            port, status = future.result()
            results.append((port, status))

            # Send update to UI
            if update_callback:
                update_callback(port, status)

    return results