'''from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter'''

class DocumentEditor:
    name = 'Document_Editor'
    def __init__(self, reader, writer, canvas, letter, bool) -> None:
        self.reader = reader
        self.writer = writer
        self.canvas = canvas
        self.letter = letter
        self.bool = bool
        self.input_pdf_reader = None
        self.output_pdf_writer = None
        self.existing_fields = None
        self.output_pdf_path = None
        self.input_pdf_path = None
        self.pdf_type = None
        self.auto_fill = False
        self.destination_file_py = None

    def test_pdf(self, name):
        snake_name = name.replace(' ', '_')
        self.output_pdf_path = f'View_field_names_for_{snake_name}.pdf'

    def add_existing_fields(self,):
        with open(self.destination_file_py, 'r') as py_file:
            py_file = py_file.read()
        
        fx_text = '\n\n    def update_fields(self, case_information, existing_fields):'
        py_file = py_file + fx_text 
        for field in self.existing_fields:
            field_text = self.existing_fields[field]
            
            text = f"\n        #{field}"
            if '/FT' in field_text and '/Kids' in field_text:
                # If the field has Children
                print(f'Field {field} has kids')

            elif '/FT' in field_text and field_text['/FT'] == '/Btn':
                # If the field is a button
                text = f"\n        existing_fields['{field}'] = self.bool(True)#{field}"

            else:
                # The field is just text
                text = f"\n        existing_fields['{field}'] = 'field: {field}'"

            py_file = py_file + text
        py_file = py_file + f"\n\n\n\n'''{self.existing_fields}'''"
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

    def get_pdf_type(self, name):
        try:
            snake_name = name.replace(' ', '_')
            print(snake_name)
            # Import the module dynamically
            module_name = self.destination_file_py  # Replace 'module_name' with an appropriate module name
            print(module_name)

            with open(module_name, 'r') as file:
                contents = file.read()
            exec(contents, globals())
            class_obj = globals()[snake_name]
            # Create an instance of the class
            self.pdf_type = class_obj()
            self.pdf_type.bool = self.bool
            print(self.pdf_type)
            print('object instanced')

        except Exception as e:
            print(f"Error creating instance: {e}")

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