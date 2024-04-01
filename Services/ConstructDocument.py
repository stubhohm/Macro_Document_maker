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
        self.template_selected = None
        self.required_fields = None
        self.attorney_selected = None
        self.case_selected = None
        self.pdf_path = None
        self.macro_path = None
        self.case_path = None
        self.attorney_path = None
        self.submitted_data = None
        self.create_doc = None

    def critical_fail(self, text = ''):
        self.critical_error = True
        print(text)
        self.go_to_new_menu(self.name)

    def refresh_screen(self):
        self.target_menu = self.name
        self.call_update = True

    def header_and_return_to_main(self, root):
        header = self.ttk.Label(root, text=f'Filling out {self.template_selected} template.')
        header.pack() 
        main_menu_button = self.ttk.Button(root, text='Return to Main Menu', command= lambda: self.go_to_new_menu('Main_Screen'))
        main_menu_button.pack(pady=10)

    def make_unknown_entry(self, root, item):
        item_text = ''
        if 'get_function' in item[1]:
            return None
        if 'attorney' in item[0]:
            item_text = 'Attorney '
        if 'applicant' in item[0]:
            item_text = 'Applicant '
        if 'filing' in item[0]:
            item_text = 'Filing '
        if 'decedent' in item[0]:
            item_text = 'Decedent '
        if 'interested' in item[0]:
            item_text = 'Interested Person '
        item_text += item[1]
        row_frame = self.ttk.Frame(root)
        row_frame.pack(fill = 'x')
        item_label = self.ttk.Label(row_frame, text = item_text)
        item_label.pack()
        item_entry = self.ttk.Entry(row_frame)
        item_entry.pack(pady=(0,5))
        key = item[1]
        info_type = item[0]
        return [info_type, key, item_entry]

    def display_unknown_fields(self, root, called_info):
        header = self.ttk.Label(root, text=f"Unkown fields for {self.case_selected}'s {self.template_selected}")
        header.pack(pady=5)
        canvas = self.tk.Canvas(root)
        scrollbar = self.ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        canvas.pack(fill="both", expand=True)
        frame = self.ttk.Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor="nw")
        entries = []
        for item in called_info:
            entry = self.make_unknown_entry(frame, item)
            if not entry:
                continue
            entries.append(entry)
        return entries

    def open_py_file(self, path):
        try:
            with open(path, 'r') as file:
                    file = file.read()
            return file
        except Exception as e:
            print(f'Error opening file {path}. Error: {e}')
            return None
        
    def write_py_file(self, path, contents):
        try:
            with open(path, 'w') as file:
                    file = file.write(contents)
            print(f'wrote file to {path}')
        except Exception as e:
            print(f'Error writing file {path}. Error: {e}')

    def go_to_new_menu(self, target_menu):
        self.target_menu = target_menu
        self.call_update = True

    def get_called_document_paths(self, data_base, editor):
        if self.doc_inited:
            return
        print(self.selected_attorney, self.case_selected, self.template_selected)
        data_base.get_local_doc_path(self.template_selected)
        self.pdf_path = data_base.destination_file
        data_base.get_local_py_path(self.template_selected)
        self.macro_path = data_base.destination_file_py
        editor.destination_file_py = self.macro_path
        data_base.get_attorney_path(self.selected_attorney)
        self.attorney_path = data_base.destination_file_py
        data_base.get_case_path(self.case_selected)
        self.case_path = data_base.destination_file_py
        self.doc_inited = True

    def update_dict(self, dicts, dict_type, text):
        for entry in self.submitted_data:
            type = entry[0]
            key = entry[1]
            if not type == dict_type:
                continue
            new_value = entry[2]
            old_value = dicts[key]
            old_text = f"self.{type}['{key}'] = '{old_value}'"
            new_text = f"self.{type}['{key}'] = '{new_value}'"
            print(old_text)
            print(new_text)
            if old_text in text:
                print(f'Old text is present')
            else:
                print(f'Old text was not found')
            text = text.replace(old_text, new_text)
        return text

    def update_case_with_submitted_data(self, old_dicts):
        if not self.submitted_data:
            return
        case_text = self.open_py_file(self.case_path)
        if not case_text:
            self.critical_fail('Failed to open case file for updating values')
        dict_type = ['applicant_info', 'filing_info', 'decedent_info', 'interested_person', 'attorney_info']
        for i, dicts in enumerate(old_dicts):
            case_text = self.update_dict(dicts, dict_type[i], case_text)
        self.write_py_file(self.case_path, case_text)
        self.submitted_data = None
        self.create_doc = True
        self.refresh_screen()
             
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
        return called_information

    def get_called_information(self):
        macro_file = self.open_py_file(self.macro_path)
        if not macro_file:
            self.critical_fail()
            return [None]
        return self.scan_text_for_fields(macro_file)
  
    def instnace_py_class(self, class_name, script_path):
        try:
            # Import the module dynamically
            with open(script_path, 'r') as file:
                contents = file.read()
            exec(contents, globals())
            class_obj = globals()[class_name]
            # Create an instance of the class
            instanced_class = class_obj()
            return instanced_class

        except Exception as e:
            print(f"Error creating instance: {e}")
            return None
     
    def get_known_information(self):
        case_instance = self.instnace_py_class('CaseInformation', self.case_path)
        if not case_instance:
            self.critical_fail('Failed instancing Case during Doc Construction')
            return [None]
        att_instance = self.instnace_py_class('AttorneyInformation', self.attorney_path)
        if not att_instance:
            self.critical_fail('Failed instancing Attorney during Doc Construction')
            return [None]
        att_instance.update_dictionary()
        case_instance.update_dictionary()
        case_instance.attorney_info = att_instance.attorney_info
        case_dict = [case_instance.applicant_info, case_instance.filing_info, case_instance.decedent_info, case_instance.interested_person, case_instance.attorney_info]
        return case_dict

    def remove_known_data(self, known_data, called_data):
        for item in list(called_data):
            type = item[0]
            key = item[1]
            dict = None
            if 'get' in key:
                called_data.remove(item)
                continue
            if type == 'applicant_info':
                dict = known_data[0]
            if type == 'filing_info':
                dict = known_data[1]
            if type == 'decednet_info':
                dict = known_data[2]
            if type == 'attorney_info':
                dict = known_data[4]
            if not dict:
                continue
            value = dict[key]
            if value == '':
                continue
            called_data.remove(item)

    def ensure_case_information(self, case_info, called_info, info_type):
        for key in case_info.keys():
            value = case_info[key]
            empty = ''
            if not value == empty:    
                continue
            entry = [info_type, key]
            if entry in called_info:
                continue
            called_info.append(entry)
                
        '''
        def display_options(self, root, options, selection_type):
        combo_box = self.ttk.Combobox(root, values=options)
        combo_box.set(f'Select an {selection_type}')
        combo_box.bind('<<ComboboxSelected>>', lambda event, st = selection_type: self.on_box_select(st))
        combo_box.pack(pady=10)
        return combo_box
        '''

    def get_function_data(self, case_info, called_info, info_type):
        in_list = False
        for item in called_info:
            if info_type in item:
                in_list = True
                print(f'Infotype: {info_type} in list via {item}')
                break
        if not in_list:
            print(f'{info_type} not in list')
            return
        empty = ''
        get_function_keys = ['Name', 'Telephone', 'Bar Number', 'Street address', 'City', 'State','Zip']
        for key in case_info.keys():
            value = case_info[key]
            if not value == empty:
                continue
            for get_key in get_function_keys:
                if get_key not in key:
                    continue
            entry = [info_type, key]
            called_info.append(entry)

    def on_submit_entries(self, entries):
        submissions = []
        for entry in entries:
            value_type = entry[0]
            key = entry[1]
            value = entry[2].get()
            submission = [value_type, key, value]
            submissions.append(submission)
        self.submitted_data = submissions
        self.refresh_screen()

    def submit_entries_button(self, root, entries):
        submit_button = self.ttk.Button(root, text = 'Submit Previuosly Unknown Data', command = lambda: self.on_submit_entries(entries))
        submit_button.pack()

    def instance_macro_classes(self, editor):
        snake_macro_name = editor.make_snake(self.template_selected)
        macro_class = self.instnace_py_class(snake_macro_name, self.macro_path)
        macro_class.bool = editor.bool
        editor.pdf_type = macro_class
        attorney_class = self.instnace_py_class('AttorneyInformation', self.attorney_path)
        attorney_class.update_dictionary()
        case_class = self.instnace_py_class('CaseInformation', self.case_path)
        case_class.update_dictionary()
        case_class.attorney_info = attorney_class.attorney_info
        editor.pdf_path = self.pdf_path
        editor.open_pdf()
        return case_class

    def publish_doc(self, editor):
        if not self.create_doc:
            return
        case_class = self.instance_macro_classes(editor)
        editor.get_fields()
        editor.copy_pdf()
        editor.update_form_fields(case_class)
        editor.fill_in_form()
        output_file_name = f'{self.template_selected} on behalf of {self.case_selected}.pdf'
        editor.output_pdf_path = output_file_name
        editor.output_new_doc()
        print(f'your new pdf can be found under the name {output_file_name}')

    def menu_main(self, root, input_data, editor):
        # Extract input data
        self.selected_attorney = input_data[0]
        self.template_selected = input_data[1]
        self.case_selected = input_data[2]
        data_base = input_data[3]

        # Make a copy of the selected pdf and get related scripts and files.
        self.get_called_document_paths(data_base, editor)
        self.publish_doc(editor)

        called_info = self.get_called_information()
        case_dict = self.get_known_information()
        
        # See what data is called for and what data we know.
        self.ensure_case_information(case_dict[0], called_info,'applicant_info')
        self.ensure_case_information(case_dict[1], called_info, 'filing_info')
        self.ensure_case_information(case_dict[4], called_info, 'attorney_information')
        self.get_function_data(case_dict[2], called_info,'decedent_info')
        self.get_function_data(case_dict[3], called_info,'interested_person')

        # Sort the called information by type:
        called_info = sorted(called_info, key=lambda x: (x[0], x[1]))
        
        # Remove known data from called info list
        self.remove_known_data(case_dict, called_info)
        self.update_case_with_submitted_data(case_dict)
        # Header for page
        header_frame = self.ttk.Frame(root)
        header_frame.pack()
        self.header_and_return_to_main(header_frame)

        # Unknow Field Frame
        unknow_field_frame = self.ttk.Frame(root)
        unknow_field_frame.pack(fill='both', expand = True)
        entries = self.display_unknown_fields(unknow_field_frame, called_info)
        self.submit_entries_button(unknow_field_frame, entries)  
               
        # If user selected to fill in Case or Attorny Data these functions run
        
        '''
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
        '''
