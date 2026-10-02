# Network Scanner

A Python-based network scanning and reconnaissance tool with a graphical user interface for performing TCP and UDP port scanning, service identification, basic host analysis, vulnerability checks, and PDF report generation.

> **Educational & Authorized Security Testing Tool**
>
> This project is intended for educational purposes, cybersecurity labs, CTF environments, and authorized security testing only. Scan only systems and networks for which you have explicit permission.

---

## 📌 Overview

**Network Scanner** is a desktop-based network reconnaissance application developed using Python.

The application provides a graphical interface that allows users to:

- Enter a target IP address or hostname
- Select different scan profiles
- Perform TCP and UDP port scanning
- Scan custom port ranges
- Perform multithreaded scanning
- Identify commonly associated services
- Perform basic banner grabbing
- Perform basic operating system inference
- Perform basic vulnerability checks
- Monitor scan progress
- View scan results
- Generate PDF reports

The project was developed to provide practical experience with **computer networking, socket programming, port scanning, multithreading, cybersecurity concepts, and Python GUI development**.

---

# ✨ Features

## 🔍 Network Scanning

The scanner supports:

- TCP port scanning
- UDP port scanning
- Multithreaded port scanning
- Custom port ranges
- Target IP/hostname resolution
- Configurable scan speed
- Scan progress monitoring
- Open port detection
- Closed port detection
- Basic filtered/open|filtered detection

---

## ⚡ Scan Profiles

The application provides multiple predefined scan profiles:

- Quick Scan
- Full Scan
- Stealth Scan
- TCP Scan
- UDP Scan
- Intense Scan

Each profile uses different scanning configurations such as:

- Port range
- Timeout
- Number of worker threads
- Scan protocol

> **Important:** The current `Stealth Scan` profile uses TCP connection-based scanning. It is not a true Nmap SYN (`-sS`) scan.

---

## 🌐 TCP Scanning

TCP scanning is implemented using Python sockets.

The scanner attempts to establish a TCP connection with the target port.

Conceptually:

```text
Target
   │
   ▼
Create TCP Socket
   │
   ▼
Attempt Connection
   │
   ├── Connection Successful → OPEN
   │
   └── Connection Failed → CLOSED
📡 UDP Scanning

The application also provides UDP scanning.

UDP scanning sends a UDP probe to the target port and waits for a response.

Conceptually:

Target
   │
   ▼
Create UDP Socket
   │
   ▼
Send UDP Probe
   │
   ▼
Wait for Response
   │
   ├── Response → OPEN
   │
   └── No Response → OPEN|FILTERED

UDP scanning can be less definitive than TCP scanning because many UDP services do not respond to arbitrary packets.

🧵 Multithreaded Scanning

The scanner uses Python's:

ThreadPoolExecutor

to perform multiple port checks concurrently.

Instead of scanning every port sequentially:

Port 1 → Port 2 → Port 3 → Port 4 → ...

multiple ports can be processed concurrently:

             ┌── Port 1
             ├── Port 2
Scanner ─────┼── Port 3
             ├── Port 4
             └── Port 5

This helps improve scanning performance compared with a purely sequential implementation.

🔎 Service Identification

The project uses Python's socket service database to identify commonly associated services.

Examples include:

21   → FTP
22   → SSH
23   → Telnet
25   → SMTP
53   → DNS
80   → HTTP
110  → POP3
143  → IMAP
443  → HTTPS

If a service is not recognized, the application can report it as:

Unknown

The project also includes basic TCP banner-grabbing functionality.

🖥️ Basic OS Detection

The project includes basic rule-based operating system inference.

Some current rules are based on commonly associated ports.

For example:

Port 445 or 3389 → Windows
Port 22          → Linux/Unix
Otherwise        → Unknown

This is a heuristic-based implementation.

It is not equivalent to advanced TCP/IP stack fingerprinting or Nmap's full operating-system detection.

🛡️ Basic Vulnerability Checks

The application performs basic checks for potentially insecure or exposed services.

Current checks include services commonly associated with:

21  → FTP
23  → Telnet
445 → SMB

Examples of informational warnings include:

FTP may allow anonymous login
Telnet is insecure because it uses plaintext communication
SMB may be exposed to security risks

These checks are intended as basic indicators.

They do not confirm that a target is actually vulnerable.

The application is not intended to replace dedicated vulnerability scanners.

📊 Risk Analysis

The application provides a basic risk classification based on the scan results.

The current project uses a simple rule-based approach.

For example:

Open ports detected
        ↓
Potentially exposed services
        ↓
Basic risk indication

This is not a CVSS-based vulnerability scoring system.

📄 PDF Report Generation

The application can generate PDF reports containing information from the completed scan.

The report can include:

Target
Resolved IP address
Scan type
Scan duration
Completion time
Risk information
Detected issues
Open ports
Services
Full scan results

PDF reports are generated using:

ReportLab
🖼️ Screenshots
Main Dashboard

Scan Results

Ports and Services

Vulnerability Results

Host Details

PDF Report

Note: Change the screenshot filenames above if your actual files use different names.

🛠️ Technologies Used
Technology	Purpose
Python	Core programming language
CustomTkinter	Graphical user interface
Tkinter / ttk	Interface components and result tables
Socket	TCP/UDP network communication
ThreadPoolExecutor	Concurrent port scanning
ReportLab	PDF report generation
📁 Project Structure
Network Scanner/
│
├── main.py
├── dashboard.py
├── scanner.py
├── ai_engine.py
├── os_detection.py
├── services.py
├── vulnerabilities.py
├── report_generator.py
├── requirements.txt
│
├── screenshots/
│   ├── dashboard.png
│   ├── scan-results.png
│   ├── ports-services.png
│   ├── vulnerabilities.png
│   ├── host-details.png
│   └── pdf-report.png
│
└── README.md
📂 File Description
main.py

The main entry point of the application.

It starts the Network Scanner graphical application.

dashboard.py

Contains the primary graphical user interface.

It handles functionality such as:

Target input
Scan profile selection
Scan speed selection
Custom port ranges
Starting scans
Displaying progress
Displaying results
Displaying host information
Displaying vulnerability information
PDF report generation
scanner.py

Contains the core network scanning functionality.

It handles:

TCP scanning
UDP scanning
Port scanning
Multithreaded execution
Socket communication
Scan results
ai_engine.py

Contains configuration logic for the available scan profiles.

The current implementation uses predefined rule-based configurations for different scan modes.

It is not a machine-learning model.

os_detection.py

Contains the basic operating-system inference functionality.

It uses detected ports and simple rules to infer a possible operating system.

services.py

Handles service identification and basic banner grabbing.

It uses Python's socket service database to associate common ports with service names.

vulnerabilities.py

Contains basic checks for potentially risky services.

Current checks include:

FTP
Telnet
SMB
report_generator.py

Handles PDF report generation.

It uses ReportLab to create a report containing scan information and results.

requirements.txt

Contains the external Python dependencies required by the project.

Install them using:

pip install -r requirements.txt
⚙️ Installation
Requirements

Before running the project, install:

Python 3.10 or newer
pip
Required Python packages
A network environment where you have permission to perform scanning

Check your Python version:

python --version

or:

python3 --version
📥 Installation from GitHub

Clone the repository:

git clone https://github.com/PDEEKSHITHREDDY/Network-Scanner.git

Move into the project directory:

cd Network-Scanner

If your GitHub repository has a different name, replace the URL and directory name accordingly.

🐍 Create a Virtual Environment

Using a virtual environment is recommended.

Windows
python -m venv venv

Activate it:

venv\Scripts\activate
Linux / macOS
python3 -m venv venv

Activate it:

source venv/bin/activate
📦 Install Dependencies

Install the required packages:

pip install -r requirements.txt
▶️ Running the Application

Start the application using:

python main.py

The Network Scanner graphical interface should launch.

🚀 How to Use
Step 1 — Enter a Target

Enter an IP address or hostname that you are authorized to scan.

Example:

192.168.1.1

or:

example.com
Step 2 — Select a Scan Profile

Choose one of the available profiles:

Quick Scan
Full Scan
Stealth Scan
TCP Scan
UDP Scan
Intense Scan
Step 3 — Select Scan Speed

The application provides different speed configurations.

The selected speed affects parameters such as:

Number of concurrent workers
Socket timeout
Step 4 — Configure Ports

You can use the predefined port ranges or provide a custom range.

Example:

80-100

This scans ports:

80
81
82
...
100
Step 5 — Start the Scan

Start the scan from the graphical interface.

The application displays scan progress and results while the scan is running.

🔍 Scan Profiles
Quick Scan

Designed for quickly checking a smaller range of commonly used ports.

Useful when you want a fast overview of common services.

Full Scan

Scans the full TCP port range:

1-65535

This provides broad port coverage but can take longer.

TCP Scan

Performs TCP connection-based port scanning.

The scanner attempts to establish a connection to each selected TCP port.

UDP Scan

Performs UDP probing against the selected ports.

UDP results can be less definitive than TCP results because UDP services may not respond to arbitrary packets.

Stealth Scan

The current implementation uses TCP connection-based scanning with a different timeout and concurrency configuration.

It is not equivalent to Nmap's SYN scan (-sS).

Intense Scan

Performs a broader scan using the full port range:

1-65535

and more conservative scanning parameters.

📋 Understanding Scan Results

The application provides information about discovered ports and services.

Example:

Port    Status    Service
----    ------    -------
22      OPEN      SSH
80      OPEN      HTTP
443     OPEN      HTTPS

An open port means that the target accepted the connection or responded according to the scanning method used.

🔬 Technical Workflow

The overall workflow of the application is:

                    ┌────────────────────┐
                    │      User          │
                    │ Target + Profile   │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │    dashboard.py    │
                    │       GUI          │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │     scanner.py     │
                    │   TCP / UDP Scan   │
                    └─────────┬──────────┘
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
             ┌─────────────┐     ┌─────────────┐
             │ TCP Sockets │     │ UDP Sockets │
             └──────┬──────┘     └──────┬──────┘
                    │                   │
                    └─────────┬─────────┘
                              ▼
                    ┌────────────────────┐
                    │   Scan Results     │
                    └─────────┬──────────┘
                              │
              ┌───────────────┼────────────────┐
              ▼               ▼                ▼
       ┌─────────────┐ ┌─────────────┐ ┌───────────────┐
       │  Services   │ │ OS Detection│ │ Vulnerability │
       │  Detection  │ │             │ │    Checks     │
       └──────┬──────┘ └──────┬──────┘ └───────┬───────┘
              │               │                │
              └───────────────┼────────────────┘
                              ▼
                    ┌────────────────────┐
                    │   Results Display  │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │ PDF Report Export  │
                    └────────────────────┘
🧠 Multithreading Architecture

The scanner uses Python's ThreadPoolExecutor.

Instead of processing ports one after another:

Port 1
  ↓
Port 2
  ↓
Port 3
  ↓
Port 4

multiple ports can be processed concurrently:

                 ┌── Port 1
                 ├── Port 2
Scanner ─────────┼── Port 3
                 ├── Port 4
                 └── Port 5

The number of concurrent workers depends on the selected scanning configuration.

🔐 Security Considerations

Network scanning generates traffic toward the target system.

Scanning can:

Trigger firewall alerts
Trigger IDS/IPS alerts
Generate security logs
Affect network monitoring systems
Be prohibited by organizational policies

Therefore, only scan systems for which you have authorization.

⚠️ Limitations

This project is an educational network scanning tool and has several technical limitations.

TCP Scanning

The current TCP scanner uses connection-based scanning.

It does not implement raw-packet SYN scanning.

UDP Scanning

UDP scanning can produce ambiguous results because many UDP services do not respond to arbitrary probes.

OS Detection

The current OS detection mechanism is heuristic-based.

It does not perform complete TCP/IP fingerprinting.

Service Detection

Service identification primarily uses known port/service mappings and basic banner information.

It does not provide the same level of service/version fingerprinting as advanced network scanners.

Vulnerability Detection

The vulnerability module provides basic service-based checks.

It does not perform:

CVE verification
Exploit validation
Authenticated vulnerability assessment
Web application vulnerability scanning
Deep service enumeration
Full vulnerability database correlation
Risk Scoring

The current risk classification is basic and should not be considered a professional vulnerability risk rating such as CVSS.

🔮 Future Scope

Possible future improvements include:

Advanced host discovery
CIDR network scanning
TCP SYN scanning
Improved UDP probing
Advanced service/version detection
Improved banner grabbing
Advanced OS fingerprinting
CVE database integration
CVSS-based risk scoring
Network topology visualization
Scan history
Scan result filtering
JSON export
CSV export
XML export
Improved PDF reports
More vulnerability checks
Configurable scan profiles
Network discovery
Improved logging
Better error handling
Result search functionality
🎓 Learning Outcomes

This project provides practical experience with:

Networking
TCP/IP
TCP connections
UDP communication
Ports
Services
Network reconnaissance
Python
Socket programming
Multithreading
Exception handling
Modular programming
File handling
GUI development
Cybersecurity
Port scanning
Service enumeration
Network reconnaissance
Basic vulnerability identification
Security risk awareness
Software Development
Modular architecture
GUI development
Report generation
Configuration management
Project documentation
🧪 Testing

The application should be tested only against authorized targets.

Recommended environments include:

Your own computer
Your own local network
Virtual machines
Cybersecurity labs
CTF environments
Intentionally vulnerable training machines

For example, a local test target may be:

127.0.0.1

or another system in a private lab where you have permission to perform scanning.

📄 Example Output

A typical scan may produce results such as:

Target: 192.168.1.1

Port     Status       Service
--------------------------------
22       OPEN         SSH
80       OPEN         HTTP
443      OPEN         HTTPS

The application can then use these results for:

Service identification
Basic security checks
Host analysis
PDF report generation
📑 PDF Report

The generated PDF report can contain:

Network Scan Report
────────────────────────────────

Target:
IP Address:
Scan Type:
Duration:
Completed At:

Risk Information

Detected Issues

Open Ports

Services

Full Scan Results

The exact report contents depend on the scan results.

🧰 Dependencies

The main external libraries used by the project include:

customtkinter
reportlab

Install all dependencies with:

pip install -r requirements.txt
🗂️ Recommended GitHub Repository Structure
Network-Scanner/
│
├── main.py
├── dashboard.py
├── scanner.py
├── ai_engine.py
├── os_detection.py
├── services.py
├── vulnerabilities.py
├── report_generator.py
│
├── requirements.txt
├── README.md
├── .gitignore
│
├── screenshots/
│   ├── dashboard.png
│   ├── scan-results.png
│   ├── ports-services.png
│   ├── vulnerabilities.png
│   ├── host-details.png
│   └── pdf-report.png
│
└── reports/
    └── sample-report.pdf
👨‍💻 Author
Pinninti Deekshith Reddy

Cybersecurity Student | Network Security | Ethical Hacking

Interested in:

Cybersecurity
Network Security
Ethical Hacking
Security Tools
Python
Network Reconnaissance
📜 License

This project is provided for educational and authorized security-testing purposes.

If an open-source license is added to this repository, the terms of that license will apply to the use, modification, and distribution of the project.

⚖️ Legal & Ethical Disclaimer

Network Scanner is intended only for authorized security testing and educational purposes.

Do not use this software to scan systems, networks, websites, servers, or devices without appropriate authorization.

Unauthorized network scanning may violate:

Organizational policies
Network usage policies
Terms of service
Applicable cybersecurity laws and regulations

The author does not encourage or support unauthorized scanning, exploitation, or disruption of systems.

The user is solely responsible for ensuring that their use of this software is lawful and authorized.

---

## 👨‍💻 Developed By

**Pinninti Deekshith Reddy**

Cybersecurity Student | Network Security | Ethical Hacking
