from PyPDF2 import PdfReader, PdfWriter

# Define the file path for the uploaded PDF
input_pdf_path = "Fun\Economics_Stiglitz.pdf"
output_pdf_path = "Fun\Economics_Stiglitz_265-286.pdf"

# Open the input PDF and initialize a PdfWriter object for the output
reader = PdfReader(input_pdf_path)
writer = PdfWriter()

# Extract the desired page range (181-262)
start_page = 265 - 1  # Pages are zero-indexed
end_page = 286

# Add the selected pages to the writer
for page_num in range(start_page, end_page):
    writer.add_page(reader.pages[page_num])

# Write the output to a new PDF
with open(output_pdf_path, "wb") as output_pdf:
    writer.write(output_pdf)

output_pdf_path
