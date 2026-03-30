from pypdf import PdfReader

reader=PdfReader("US-Employee_Policy.pdf")

document_text=""
for page in reader.pages:
document_text += page.extract_text()
