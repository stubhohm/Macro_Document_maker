name = 'Name'
address = 'Street Address'
city = 'City'
county = 'County'
state = 'State'
zip = 'Zip'
bar_no = 'Bar Number'
tele = 'Telephone'
f_name = 'First Name'
m_name = 'Middle Name'
l_name = 'Last Name'
rel = 'Relation'

court_county = 'Probate Court County'
court_address = 'Street Address'
court_tele = 'Telephone'
judge ='Judge'
deat_cert_attach = 'Death Cert Attached'
death_cert_avail = 'Death Cert Available'
case_no = 'Case Number'
MCL = 'MCL 7003311' 
codicile_date = 'Codicil Date'
codicile_county = 'Codicile County'

death_date = 'Date of Death'
death_time = 'Time of Death'
will_date = 'Will Date'

age_if_minor ='Age if Minor'
legal_dis = 'Legal Disability'
legal_rep ='REPRESENTED BY Name address and capacity'
keys = [name, 
        address, 
        city, 
        county, 
        state, 
        zip, 
        bar_no, 
        tele, 
        f_name, 
        m_name, 
        l_name, 
        rel,
        court_county, 
        court_address, 
        court_tele,
        judge, 
        deat_cert_attach,
        death_cert_avail,
        case_no,
        codicile_date,
        codicile_county,
        death_date,
        death_time,
        will_date,
        age_if_minor,
        legal_dis,
        legal_rep]

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
        self.doc_name = None
        self.py_file_text = None

    def test_pdf(self):
        snake_name = self.doc_name.replace(' ', '_')
        self.output_pdf_path = f'View_field_names_for_{snake_name}.pdf'

    def open_py_file(self):
        with open(self.destination_file_py, 'r') as py_file:
            py_file = py_file.read()
        self.py_file_text = py_file

    def write_py_file(self):
        with open(self.destination_file_py, 'w') as dest_file:
            dest_file.write(self.py_file_text)

    def set_py_doc_info_type(self, definition, text):
        info_type = ''
        if 'Attorney' in definition:
            info_type = 'attorney_info'
        elif 'Applicant' in definition:
            info_type = 'applicant_info'
        elif 'Filing' in definition:
            info_type = 'filing_info'
        elif 'Decedent' in definition:
            info_type = 'decedent_info'
        elif 'Interested Person' in definition:
            info_type = 'interested_person'
        else:
            return info_type, False

        # Check for compound info function calls
        if 'Full Name, Addrress and Phone' in definition:
            info_type = f'get_name_address_phone({text}{info_type})'
            return info_type, False
        if 'Full Name, Bar No, Address and Phone' in definition:
            info_type = f'get_name_address_phone({text}{info_type}, True)'
            return info_type, False
        if 'Full Name' in definition:
            info_type = f'get_full_name({text}{info_type})'
            return info_type, False
        if 'Full Address' in definition:
            info_type = f'get_full_address({text}{info_type})'
            return info_type, False
            
        info_type = info_type + '['
        return info_type, True

    def set_py_doc_key(self, definition, text):
        for key in keys:
            if key in definition:
                key_name = "'" + key + "'"
                text = text + key_name + ']'
                return text

    def make_field_text(self, definition):
        text = 'case_information.'
        # Sets un marked sections to be empty
        if 'None' in definition or 'Case Information Fields' in definition:
            text = "' '"
        # Check what info type we need based on selection and if a key is needed
        info_type, needs_key = self.set_py_doc_info_type(definition, text)
        text = text + info_type
        # If a key is needed fills in the needed key
        if needs_key:
            text = self.set_py_doc_key(definition, text)            
        
        return text

    def replace_place_holders(self, entries, progress, bar_size):
        print("start replacement")
        for i, entry in enumerate(entries):
            field_name, var = entry['field'], entry['var'].get()
            print(f'Field: {field_name} Selected Output: {var}')
            text = self.make_field_text(var)
            print(f'New Text: {text}')
            old_string = f"'field: {field_name}'"
            self.py_file_text = self.py_file_text.replace(old_string, text)
            progress['value'] = i
        self.write_py_file()
        progress['value'] = bar_size

    def add_existing_fields(self,):
        self.open_py_file()
        
        fx_text = '\n\n    def update_fields(self, case_information, existing_fields):'
        self.py_file_text = self.py_file_text + fx_text 
        for field in self.existing_fields:
            field_text = self.existing_fields[field]
            
            text = f"\n        #{field}"
            if '/FT' in field_text and '/Kids' in field_text:
                # If the field has Children
                print(f'{field_text}')

            if '/FT' in field_text and field_text['/FT'] == '/Btn':
                # If the field is a button
                text = f"\n        existing_fields['{field}'] = self.bool(True)#{field}"

            else:
                # The field is just text
                text = f"\n        existing_fields['{field}'].update(" +'{' + f"'/V': 'field: {field}'" + '})'

            self.py_file_text = self.py_file_text + text
        self.write_py_file()

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

    def get_pdf_type(self):
        try:
            snake_name = self.doc_name.replace(' ', '_')
            print(snake_name)
            # Import the module dynamically
            module_name = self.destination_file_py
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

    def make_new_case_file():
        case_info_directory = 'Classes\\Doc_types\\CaseInformation.py'
        with open(case_info_directory, 'r') as output_file:
            case_info_copy = output_file.read()
        
