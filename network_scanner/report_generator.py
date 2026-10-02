from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()


def export_pdf(filename, data):

    doc = SimpleDocTemplate(filename)
    elements = []

    # ===== TITLE =====
    elements.append(Paragraph("Network Scan Report", styles["Title"]))
    elements.append(Spacer(1, 12))

    # ===== OVERVIEW =====
    elements.append(Paragraph("Overview", styles["Heading2"]))
    elements.append(Spacer(1, 8))

    overview = [
        f"Target: {data['target']}",
        f"IP: {data['ip']}",
        f"Scan Type: {data['scan_type']}",
        f"Duration: {data['duration']} sec",
        f"Completed At: {data['completed_time']}",
        f"Risk Level: {data['risk']}"
    ]

    for item in overview:
        elements.append(Paragraph(item, styles["Normal"]))

    elements.append(Spacer(1, 15))

    # ===== RISKS =====
    elements.append(Paragraph("Risk Analysis", styles["Heading2"]))
    elements.append(Spacer(1, 8))

    if data["issues"]:
        for issue in data["issues"]:
            elements.append(Paragraph(f"• {issue}", styles["Normal"]))
    else:
        elements.append(Paragraph("No major risks detected", styles["Normal"]))

    elements.append(Spacer(1, 15))

    # ===== OPEN PORTS =====
    elements.append(Paragraph("Open Ports", styles["Heading2"]))
    elements.append(Spacer(1, 8))

    open_table = [["Port", "Service"]]

    for port in data["open_ports"]:
        open_table.append([str(port), data["services"].get(port, "Unknown")])

    table = Table(open_table)
    table.setStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("GRID", (0, 0), (-1, -1), 1, colors.black)
    ])

    elements.append(table)
    elements.append(Spacer(1, 20))

    # ===== FULL RESULTS =====
    elements.append(Paragraph("Full Scan Results", styles["Heading2"]))
    elements.append(Spacer(1, 8))

    full_table = [["Port", "Status", "Service"]]

    for port, status in data["results"]:
        full_table.append([
            str(port),
            status,
            data["services"].get(port, "Unknown")
        ])

    table2 = Table(full_table)
    table2.setStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("GRID", (0, 0), (-1, -1), 1, colors.black)
    ])

    elements.append(table2)

    doc.build(elements)