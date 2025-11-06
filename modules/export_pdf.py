# Module pour export PDF
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def export_to_pdf(data):
    c = canvas.Canvas('data/export_regulations.pdf', pagesize=A4)
    c.drawString(100, 800, 'Rapport Réglementations')
    y = 750
    for key, value in data.items():
        c.drawString(100, y, f"{key}: {value}")
        y -= 20
    c.save()
