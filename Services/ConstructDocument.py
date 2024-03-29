from Classes.Case_fields import attorney_info, applicant_info, decedent_info, filing_info, interested_person

class ConstructDocument():
    name = 'Construct_Document'
    
    def __init__(self, display, tk, ttk, messagebox, filedialog):
        self.display = display
        self.tk = tk
        self.ttk = ttk
        self.messagebox = messagebox
        self.filedialog = filedialog
        self.critical_error = False
        self.doc_inited = False
        self.call_update = False
        self.target_menu = None
        self.options = []
        self.att_fields = []
        self.selected_template = None
        self.required_fields = None
        self.attorney_selected = None
        self.case_selected = None
        self.pdf_path = None
        self.macro_path = None
        self.case_path = None
        self.attorney_path = None

    def critical_fail(self):
        self.critical_error = True
        self.go_to_new_menu(self.name)

    def refresh_screen(self):
        self.target_menu = self.name
        self.call_update = True

    def open_py_file(self, path):
        try:
            with open(path, 'r') as file:
                    file = file.read()
            return file
        except Exception as e:
            print(f'Error opening file {path}. Error: {e}')
            return None

    def go_to_new_menu(self, target_menu):
        self.target_menu = target_menu
        self.call_update = True

    def get_called_document_paths(self, data_base, editor):
        if self.doc_inited:
            return
        data_base.get_local_doc_path(self.selected_template)
        self.pdf_path = data_base.destination_file
        data_base.get_local_py_path(self.selected_template)
        self.macro_path = data_base.destination_file_py
        editor.destination_file_py = self.macro_path
        data_base.get_attorney_path(self.selected_attorney)
        self.attorney_path = data_base.destination_file_py
        data_base.get_case_path(self.selected_case)
        self.case_path = data_base.destination_file_py
        self.doc_inited = True


    def scan_text_for_fields(self, file):
        lines = file.splitlines()
        attorney = [attorney_info, 'attorney_info']
        applicant = [applicant_info, 'applicant_info']
        deced = [decedent_info,'decedent_info']
        file = [filing_info, 'filing_info']
        interest = [interested_person, 'interested_person']
        info_types = [applicant, attorney, deced, file, interest]
        called_information = []
        # This big nested for loop is probably the ugliest/smelliest part of this codebase
        for line in lines:
            if 'case_information.' not in line:
                continue
            for type in info_types:
                if type[1] not in line:
                    continue
                for key in type[0].keys():
                    if key not in line and 'get' not in line:
                        continue
                    if 'get' in line:
                        key = 'get_function'
                    query = [type[1], key]
                    if query in called_information:
                        continue
                    called_information.append(query)
                    break
                break           
        print(called_information)
        return called_information

    def get_called_information(self):
        macro_file = self.open_py_file(self.macro_path)
        if not macro_file:
            self.critical_fail()
            return [None]
        return self.scan_text_for_fields(macro_file)

    def scan_text_for_known_information(self, file):
        lines = file.splitlines()
        applicant = [applicant_info, 'applicant_info']
        deced = [decedent_info,'decedent_info']
        file = [filing_info, 'filing_info']
        interest = [interested_person, 'interested_person']
        info_types = [applicant, deced, file, interest]
        known_information = []
        
            
    def get_known_information(self, editor):
        case_file = self.open_py_file(self.case_path)
        if not case_file:
            self.critical_fail()
            return [None]
        return self.scan_text_for_known_information(case_file)
        


    def header_and_return_to_main(self, root):
        header = self.ttk.Label(root, text=f'Filling out {self.selected_template} template.')
        header.pack() 
        main_menu_button = self.ttk.Button(root, text='Return to Main Menu', command= lambda: self.go_to_new_menu('Main_Screen'))
        main_menu_button.pack(pady=10)

    #def display_options(self, root, options, selection_type):
        combo_box = self.ttk.Combobox(root, values=options)
        combo_box.set(f'Select an {selection_type}')
        combo_box.bind('<<ComboboxSelected>>', lambda event, st = selection_type: self.on_box_select(st))
        combo_box.pack(pady=10)
        return combo_box

    def on_fill_in_doc(self):
        self.refresh_screen()
        return
        
    def fill_in_doc_button(self, root):
        fill_in_doc_button = self.ttk.Button(root, text='Create Document', command= lambda: self.on_fill_in_doc())
        fill_in_doc_button.pack(pady=10)

  
    def menu_main(self, root, input_data, editor):
        # Extract input data
        self.selected_attorney = input_data[0]
        self.selected_template = input_data[1]
        self.selected_case = input_data[2]
        data_base = input_data[3]

        print(self.selected_attorney, self.selected_case, self.selected_template)
        # Make a copy of the selected pdf and get related scripts and files
        self.get_called_document_paths(data_base, editor)
        called_info = self.get_called_information()
        known_info = self.get_known_information(data_base, editor)
        self.ensure_client_information()
        self.ensure_filing_information()

        

        # Header for page
        header_frame = self.ttk.Frame(root)
        header_frame.pack()
        self.header_and_return_to_main(header_frame)

        # Drop Down Frame
        option_frame = self.ttk.Frame(root)
        option_frame.pack()       
               
        # If user selected to fill in Case or Attorny Data these functions run
        case_att_button_frame = self.ttk.Frame(root)
        case_att_button_frame.pack()
        self.delete_selected_item(case_att_button_frame, data_base, editor)
        if self.delete_attorney or self.delete_case:
            self.delete_case, self.delete_attorney = False, False
            return
        
        self.add_attorney_fields(data_base, editor, case_att_button_frame)
        self.add_case_file(data_base, editor, case_att_button_frame)
        if self.add_attorney or self.add_case:
            self.add_attorney, self.add_case = False, False
            return
        if self.sub_att or self.sub_case:
            self.sub_att, self.sub_case = False, False
            return            
        
        second_frame = self.ttk.Frame(root)
        second_frame.pack(fill = 'x')
        self.add_new_case_or_attorney_button(second_frame)
        
        # Fill in doc button
        third_frame = self.ttk.Frame(root)
        third_frame.pack(fill = 'x')
        self.fill_in_doc_button(third_frame)


        # Fill in is done find all boxes that have '' as their input and add them to a list
        # For each item in the list label = what type of case info it wants, checkbox to leave blank
        # update case info with filled in fields

        # publish doc
