import pytesseract
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

import os
os.environ['TESSDATA_PREFIX'] = r"C:\Program Files\Tesseract-OCR\tessdata"


def extract_text(image):
    data = pytesseract.image_to_data(
        image,
        output_type=Output.DICT
    )
    return data
