def check_vulnerabilities(open_ports):
    issues = []

    if 21 in open_ports:
        issues.append("FTP may allow anonymous login")
    if 23 in open_ports:
        issues.append("Telnet is insecure (plaintext)")
    if 445 in open_ports:
        issues.append("SMB vulnerable to exploits")

    return issues