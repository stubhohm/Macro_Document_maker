'''from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter'''

class DocumentEditor:
    name = 'Document_Editor'
    def __init__(self, reader, writer, canvas, letter,) -> None:
        self.reader = reader
        self.writer = writer
        self.canvas = canvas
        self.letter = letter
        self.input_pdf_reader = None
        self.output_pdf_writer = None
        self.existing_fields = None
        self.output_pdf_path = 'test.pdf'
        self.input_pdf_path = None
        self.pdf_type = None
        self.auto_fill = False
        self.destination_file_py = None

    def add_existing_fields(self,):
        with open(self.destination_file_py, 'r') as py_file:
            py_file = py_file.read()
        
        fx_text = '\n\n    def update_fields(self, case_information, existing_fields):'
        py_file = py_file + fx_text 
        for field in self.existing_fields:
            text = f"\n        existing_fields['{field}'] = case_information."
            py_file = py_file + text
        
        with open(self.destination_file_py, 'w') as dest_file:
            dest_file.write(py_file)

    def update_menu(self, menu_names, input):
        self.input_case_data(input)
        # see what still needs info and query user
        self.update_form_fields(input.case_information)
        self.fill_in_form()
        self.output_new_doc()
        print("outputting doc")

    def open_pdf(self):
        # Step 1: Open and Read the PDF Document
        self.input_pdf_reader = self.reader(open(self.input_pdf_path, "rb"))
        
    def get_fields(self):
        self.existing_fields = self.input_pdf_reader.get_fields()

    def copy_pdf(self):
        # Step 2: Create a Copy of the PDF Document
        self.output_pdf_writer = self.writer()

        # Copy all pages from input PDF to output PDF
        for page_num in range(len(self.input_pdf_reader.pages)):
            page = self.input_pdf_reader.pages[page_num]
            self.output_pdf_writer.add_page(page)

    def update_form_fields(self, case_information):
        self.pdf_type.update_fields(case_information, self.existing_fields)

    def fill_in_form(self):
        # Step 3: Fill in the Form Fields
        for page in self.output_pdf_writer.pages:
            self.output_pdf_writer.update_page_form_field_values(page, self.existing_fields)

    def output_new_doc(self,):
        # Create a canvas to add text to the PDF
        c = self.canvas.Canvas(self.output_pdf_path, pagesize=self.letter)
        c.save()

        # Step 4: Export the Filled Document
        with open(self.output_pdf_path, "wb") as output_file:
            self.output_pdf_writer.write(output_file)