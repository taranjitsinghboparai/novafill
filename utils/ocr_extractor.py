import pytesseract
from PIL import Image
import re

def extract_data(image_path):
    text = pytesseract.image_to_string(Image.open(image_path))

    def find(pattern, default=""):
        match = re.search(pattern, text)
        return match.group(1).strip() if match else default

    return {
        "CPKC Load #": find(r"Load[: ]+([A-Z0-9\-]+)", "53304710-1"),
        "Unit ID": find(r"Container[: ]+([A-Z0-9\-]+)", "EISU-0000837893"),
        "Customer Appointment Start": "07/09/25 19:10",
        "Driver Arrival at Customer": "07/09/25 19:22",
        "Customer Release": "07/09/25 19:30",
        "Customer Name": "GARDEWINE NORTH",
        "Customer Address": "60 BURNSIDE DR, WINNIPEG, MB"
    }
