from docx import Document
import classes

document = Document('''.\data\[docx]2018년 고1 3월 영치.docx''')
lines = document.paragraphs

for line in lines:
    text = line.text



