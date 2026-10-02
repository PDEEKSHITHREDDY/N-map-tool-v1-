def detect_os(open_ports):
    if 445 in open_ports or 3389 in open_ports:
        return "Windows"
    elif 22 in open_ports:
        return "Linux/Unix"
    return "Unknown"