from PyPDF2 import PdfReader, PdfWriter

def merge_selected_pages(files, pages, output):
    writer = PdfWriter()
    for file in files:
        reader = PdfReader(file)
        for p in pages:
            if p-1 < len(reader.pages):
                writer.add_page(reader.pages[p-1])
    with open(output, "wb") as f:
        writer.write(f)

# Example
merge_selected_pages(["file1.pdf", "file2.pdf"], [1, 3], "merged.pdf")