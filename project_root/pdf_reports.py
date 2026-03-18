import os
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def generate_pdf_report(inputs, risk_score, action):
    """
    Creates a professional one-page clinical PDF summary.
    PDFs are stored in outputs/reports/.
    """
    os.makedirs("outputs/reports", exist_ok=True)

    filename = f"outputs/reports/depression_report_{datetime.now().timestamp()}.pdf"
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    y = height - 60

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "Clinical Depression Risk Report")
    y -= 40

    # Patient Inputs Section
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Patient Inputs:")
    y -= 20

    c.setFont("Helvetica", 10)
    for key, value in inputs.items():
        c.drawString(60, y, f"{key}: {value}")
        y -= 14
        if y < 80:
            c.showPage()
            y = height - 60

    # Risk Score
    y -= 20
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, f"Predicted Depression Risk Score: {risk_score:.3f}")

    # Action
    y -= 25
    c.setFont("Helvetica", 11)
    c.drawString(50, y, f"Recommended Clinical Action: {action}")

    c.showPage()
    c.save()

    return filename
