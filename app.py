import PyPDF2


with open("first.pdf", "rb") as file:
    reader = PyPDF2.PdfReader(file)
    print(len(reader.pages))
    
