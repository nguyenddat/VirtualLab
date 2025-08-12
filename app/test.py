import os

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

from PIL import Image
from pdf2image import convert_from_path
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
file_path = os.path.join(os.getcwd(), "app/artifacts/SGK VL 11 CTST.pdf")

pages = convert_from_path(file_path, dpi=300)
full_text = ""
for i, page in enumerate(pages):
    text = pytesseract.image_to_string(page, lang='vie')
    print(text)
    full_text += f"\n=== Trang {i+1} ===\n{text}"

embeddings = OpenAIEmbeddings()