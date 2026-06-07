from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

def generate_pdf(result):

    pdf_file = (
        "reports/security_report.pdf"
    )

    doc = SimpleDocTemplate(
        pdf_file
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "AI Cybersecurity Assistant Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            f"Threats: {', '.join(result['findings'])}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Severity: {result['severity']}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Server Issues: {', '.join(result['issues'])}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"MITRE: {', '.join(result['mitre'])}",
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            "Recommendations",
            styles["Heading2"]
        )
    )

    for rec in result[
        "recommendations"
    ]:

        content.append(
            Paragraph(
                f"• {rec}",
                styles["Normal"]
            )
        )

    doc.build(content)

    return pdf_file