def get_scan_profile(scan_type):

    # Default config
    config = {
        "scan_type": "TCP",
        "threads": 400,
        "timeout": 0.7,
        "ports": list(range(1, 1025))
    }

    if scan_type == "Quick Scan":
        config.update({
            "ports": list(range(1, 1001)),
            "threads": 800,
            "timeout": 0.3
        })

    elif scan_type == "Full Scan":
        config.update({
            "ports": list(range(1, 65536)),
            "threads": 500,
            "timeout": 0.5
        })

    elif scan_type == "Stealth Scan":
        config.update({
            "scan_type": "TCP",
            "threads": 900,
            "timeout": 0.2
        })

    elif scan_type == "TCP Scan":
        config.update({
            "scan_type": "TCP"
        })

    elif scan_type == "UDP Scan":
        config.update({
            "scan_type": "UDP",
            "threads": 300,
            "timeout": 1.0
        })

    elif scan_type == "Intense Scan":
        config.update({
            "ports": list(range(1, 65536)),
            "threads": 200,
            "timeout": 1.5
        })

    return config