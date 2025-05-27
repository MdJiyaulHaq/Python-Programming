import pypdf

merger = pypdf.PdfWriter()
file_names = ["pdf_1.pdf", "pdf_2.pdf"]
for file_name in file_names:
    merger.append(file_name)
merger.write("merged.pdf")
merger.close()
