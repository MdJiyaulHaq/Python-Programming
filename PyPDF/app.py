import pypdf

with open("pdf_1.pdf", "rb") as file:
    reader = pypdf.PdfReader(file)
    print(f"Number of pages: {len(reader.pages)}")

    pages = reader.pages
    all_pages = []
    for i, page in enumerate(pages):
        print(f"Processing page {i + 1}")
        # Rotate each page by 90 degrees clockwise
        page.rotate(90)
        all_pages.append(page)

    writer = pypdf.PdfWriter()
    for page in all_pages:
        writer.add_page(page)
    with open("rotated.pdf", "wb") as output_file:
        writer.write(output_file)
    print("All pages rotated and saved to rotated.pdf")
