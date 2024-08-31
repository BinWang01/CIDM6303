import PyPDF2

with open("first.pdf", "rb") as file:
    reader = PyPDF2.PdfReader(file)
    print(len(reader.pages))
    page = reader.pages[0]
    page.rotate(90)
    writer = PyPDF2.PdfWriter()
    writer.add_page(page)
    with open("rotated.pdf", "wb") as output:
        writer.write(output)

merger = PyPDF2.PdfMerger()
file_names = ["rotated.pdf", "second.pdf"]
for file_name in file_names:
    merger.append(file_name)
merger.write("combined.pdf")
