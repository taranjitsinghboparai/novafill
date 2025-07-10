from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO

# === Step 1: Field values to fill ===
field_values = {
    "CPKC Load #": "53268683-3",
    "Unit ID": "CPPU-0000532512",
    "Customer Appointment Start": "07/02/25 20:00",
    "Driver Arrival at Customer": "07/02/25 20:05",
    "Customer Release": "07/02/25 20:39",
    "Customer Name": "WESTFAIR FOODS LTD – LOBLAWS",
    "Customer Address": "101 WESTON ST, DC 37, WINNIPEG, MB R3E2T4"
}

# === Step 2: Coordinates to place text (locked-in) ===
coordinates = {
    "CPKC Load #": (330, 695),
    "Unit ID": (330, 665),
    "Customer Appointment Start": (240, 620),
    "Driver Arrival at Customer": (240, 570),
    "Customer Release": (240, 525),
    "Customer Name": (130, 405),
    "Customer Address": (130, 380)
}

# === Step 3: Create overlay PDF with text ===
packet = BytesIO()
can = canvas.Canvas(packet, pagesize=letter)
can.setFont("Helvetica", 12)

for field, (x, y) in coordinates.items():
    text = field_values.get(field, "")
    can.drawString(x, y, text)

can.save()
packet.seek(0)

# === Step 4: Merge overlay with original blank form ===
original_pdf_path = "Wait Form .PDF"
output_pdf_path = "Driver_Wait_Form_Output.pdf"

original_pdf = PdfReader(original_pdf_path)
overlay_pdf = PdfReader(packet)
output = PdfWriter()

page = original_pdf.pages[0]
page.merge_page(overlay_pdf.pages[0])
output.add_page(page)

with open(output_pdf_path, "wb") as f:
    output.write(f)

print("✅ Done! Saved to:", output_pdf_path)
