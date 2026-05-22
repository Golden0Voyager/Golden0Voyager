import os
from pypdf import PdfReader

pdf_path = "Haining Yu Resume & Portfolio |于海宁个人简历和作品集.pdf"
txt_path = "extracted_resume.txt"

print(f"Opening PDF: {pdf_path}")
reader = PdfReader(pdf_path)
total_pages = len(reader.pages)
print(f"Total pages: {total_pages}")

extracted_text = []
for i, page in enumerate(reader.pages):
    text = page.extract_text()
    extracted_text.append(f"--- PAGE {i+1} ---")
    extracted_text.append(text if text else "[No text found on this page]")

with open(txt_path, "w", encoding="utf-8") as f:
    f.write("\n".join(extracted_text))

print(f"Successfully extracted text to {txt_path}")
