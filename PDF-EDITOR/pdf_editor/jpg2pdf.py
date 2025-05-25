def convert_jpg_to_pdf(jpg_file_path, pdf_file_path):
    """
    Convert a JPG file to a PDF file.

    :param jpg_file_path: Path to the input JPG file.
    :param pdf_file_path: Path to the output PDF file.
    """
    from PIL import Image

    # Open the JPG file
    with Image.open(jpg_file_path) as img:
        # Convert the image to RGB mode if it's not already
        if img.mode != 'RGB':
            img = img.convert('RGB')
        # Save the image as a PDF
        img.save(pdf_file_path, 'PDF')
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python jpg2pdf.py <input_jpg_file> <output_pdf_file>")
        sys.exit(1)

    input_jpg = sys.argv[1]
    output_pdf = sys.argv[2]

    convert_jpg_to_pdf(input_jpg, output_pdf)
    print(f"Converted {input_jpg} to {output_pdf}")
    import os
    if os.path.exists(output_pdf):
        print(f"Output PDF file created at: {output_pdf}")
    else:
        print("Failed to create output PDF file.")
        sys.exit(1)
