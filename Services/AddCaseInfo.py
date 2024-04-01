from Classes.Case_fields import attorney_info

class AddCaseInfo():
    name = 'Add_Case_Info'
    
    def __init__(self, display, tk, ttk, messagebox, filedialog):
        self.display = display
        self.tk = tk
        self.ttk = ttk
        self.messagebox = messagebox
        self.filedialog = filedialog
        self.critical_error = False
        self.call_update = False
        self.target_menu = None
        self.options = []
        self.att_fields = []
        self.template_selected = None
        self.required_fields = None
        self.case_name = None
        self.doc_inited = False
        self.add_case = False
        self.delete_case = False
        self.update_case = False
        self.sub_case = False
        self.add_attorney = False
        self.delete_attorney = False
        self.update_attorney = False
        self.sub_att = False
        self.attorney_box = None
        self.attorney_selected = None
        self.case_box = None
        self.case_selected = None
        self.fill_in_doc = False

    def critical_fail(self):
        self.critical_error = True
        self.go_to_new_menu(self.name)

    def on_box_select(self, selection_type):
        if selection_type == 'Attorney':
            self.attorney_selected = self.attorney_box.get()
        else:
            self.case_selected = self.case_box.get()

    def refresh_screen(self):
        self.target_menu = self.name
        self.call_update = True

    def go_to_new_menu(self, target_menu):
        self.add_case = False
        self.delete_case = False
        self.update_case = False
        self.sub_case = False
        self.add_attorney = False
        self.delete_attorney = False
        self.update_attorney = False
        self.sub_att = False
        self.attorney_selected = None
        self.case_selected = None
        self.fill_in_doc = False
        self.target_menu = target_menu
        self.call_update = True

    def get_called_document(self, data_base, editor):
        if self.doc_inited:
            return
        data_base.get_local_doc_path(self.template_selected)
        data_base.get_local_py_path(self.template_selected)
        editor.input_pdf_path = data_base.destination_file
        editor.destination_file_py = data_base.destination_file_py
        editor.doc_name = self.template_selected
        editor.open_pdf()
        if not editor.input_pdf_reader:
            self.critical_fail()
            return
        editor.copy_pdf()
        editor.get_fields()
        editor.get_pdf_type()
        self.doc_inited = True

    def header_and_return_to_main(self, root):
        header = self.ttk.Label(root, text=f'Filling out {self.template_selected} template.')
        header.pack() 
        main_menu_button = self.ttk.Button(root, text='Return to Main Menu', command= lambda: self.go_to_new_menu('Main_Screen'))
        main_menu_button.pack(pady=10)

    def display_options(self, root, options, selection_type):
        combo_box = self.ttk.Combobox(root, values=options)
        combo_box.set(f'Select an {selection_type}')
        combo_box.bind('<<ComboboxSelected>>', lambda event, st = selection_type: self.on_box_select(st))
        combo_box.pack(pady=10)
        return combo_box

    def get_stored_case_names(self, data_base):
        cases = data_base.get_case_names()
        holder = []
        for option in cases:
            option = option[0]
            option = option.strip('{')
            option = option.strip('}')
            holder.append(option)
        cases = holder
        return cases
        
    def get_stored_attorney_names(self, data_base):
        attorneys = data_base.get_attorney_names()
        holder = []
        for option in attorneys:
            option = option[0]
            option = option.strip('{')
            option = option.strip('}')
            holder.append(option)
        attorneys = holder
        return attorneys

    def add_new_case_or_attorney_button(self, root):
        case_frame = self.ttk.Frame(root)
        case_frame.pack()
        new_case_button = self.ttk.Button(case_frame, text='Add New Case', command= lambda: self.on_new_case_select())
        new_case_button.pack(pady=10, side=self.tk.LEFT)
        update_case_button = self.ttk.Button(case_frame, text='Update Existing Case', command= lambda: self.on_update_case_select())
        update_case_button.pack(pady=10, side=self.tk.LEFT)
        remove_case_button = self.ttk.Button(case_frame, text='Delete Existing Case', command= lambda: self.on_delete_case_select())
        remove_case_button.pack(pady=10, side=self.tk.LEFT)
        att_frame = self.ttk.Frame(root)
        att_frame.pack()
        new_attorney_button = self.ttk.Button(att_frame, text='Add New Attorney', command= lambda: self.on_new_attorney_select())
        new_attorney_button.pack(pady=10, side=self.tk.LEFT)
        update_attorney_button = self.ttk.Button(att_frame, text='Update Existing Attorney', command= lambda: self.on_update_attorney_select())
        update_attorney_button.pack(pady=10,side=self.tk.LEFT)
        delete_attorney_button = self.ttk.Button(att_frame, text='Delete Existing Attorney', command= lambda: self.on_delete_attorney_select())
        delete_attorney_button.pack(pady=10,side=self.tk.LEFT)

    def on_new_attorney_select(self):
        self.add_attorney = True
        self.refresh_screen()

    def on_new_case_select(self):
        self.add_case = True
        self.refresh_screen()

    def on_update_attorney_select(self):
        self.update_attorney = True
        self.add_attorney = True
        self.refresh_screen()
    
    def on_update_case_select(self):
        self.update_case = True
        self.add_case = True
        self.refresh_screen()
    
    def on_delete_attorney_select(self):
        self.update_attorney = True
        self.delete_attorney = True
        self.refresh_screen()
    
    def on_delete_case_select(self):
        self.update_case = True
        self.delete_case = True
        self.refresh_screen()

    def submit_att(self):
        self.get_fields()
        self.refresh_screen()

    def get_fields(self):
        att_dict = attorney_info
        if isinstance(self.att_fields, dict):
            self.sub_att = True
            return
        for item in self.att_fields:
            key = item[0]
            entry = item[1]
            text = entry.get()
            att_dict[key] = text
        self.att_fields = att_dict
        self.sub_att = True

    def validate_att_fields(self):
        valid = True
        return valid

    def create_new_attorney(self, data_base, editor):
        # Currently always returns true
        if not self.validate_att_fields():
            return
        editor.make_new_attorney_doc_copy()
        editor.define_attorney_dictionary(self.att_fields)
        editor.write_py_file()
        data_base.destination_file_py = editor.destination_file_py
        full_name = self.att_fields['First Name'] + ' ' + self.att_fields['Middle Name'] + ' ' + self.att_fields['Last Name']
        data_base.add_attorney_to_db(full_name)
        self.sub_att, self.add_attorney, self.update_attorney = False, False, False
        self.refresh_screen()

    def update_attorney_doc(self, data_base, editor):
        attorney_name = self.attorney_selected.get()
        data_base.get_attorney_path(attorney_name)
        editor.destination_file_py = data_base.destination_file_py
        editor.open_py_file()
        text = editor.py_file_text
        if not text:
            self.critical_fail()
            return
        for i, key in enumerate(attorney_info.keys()):
            entry = self.att_fields[i]
            text = text.replace(f"['{key}'] = '",f"['{key}'] = '{entry}'#")
        return

    def add_attorney_fields(self, data_base, editor, root):
        if self.sub_att and self.update_attorney:
            self.update_attorney_doc(data_base, editor)
            self.update_attorney = False
            self.sub_att = False
            return
        if self.sub_att:
            self.create_new_attorney(data_base, editor)
        if not self.add_attorney:
            return
        append = True
        if isinstance(self.att_fields, dict):
            append = False
        for i, key in enumerate(attorney_info.keys()):
            label_text = f'{i+1}. {key}'
            label = self.ttk.Label(root, text = label_text)
            label.pack(pady=(3,0))
            entry = self.ttk.Entry(root)
            entry.pack()
            if not append:
                entry.insert(0,self.att_fields[key])
            if append:
                self.att_fields.append([key, entry])
            else:
                self.att_fields[key] = entry
        
        submit_button = self.ttk.Button(root, text = "Submit Attorney info", command = lambda: self.submit_att() )
        submit_button.pack()

    def on_new_case_submit(self):
        try:
            self.case_name = self.case_name.get()
        except:
            print('Error Encountered getting case name')
        self.sub_case = True
        self.add_case = True
        self.refresh_screen()

    def create_new_case(self, data_base, editor):
        # Currently always returns true
        if not isinstance(self.case_name, str):
            print('The Case Name was improperly formatted')
            return
        editor.make_new_case_file_copy()
        editor.make_new_case_dictionary(self.case_name)
        data_base.destination_file_py = editor.destination_file_py
        editor.write_py_file()
        data_base.add_case_to_db(self.case_name)
        self.sub_case, self.add_case, self.update_case = False, False, False
        self.refresh_screen()

    def add_case_file(self, data_base, editor, root):
        if not self.add_case:
            return
        if self.sub_case:
            self.create_new_case(data_base, editor)
            return
        if self.update_case:
            print('update case')
        case_entry_label = self.ttk.Label(root, text='Enter New Case Name')
        case_entry_label.pack(pady=(5,0))
        case_entry = self.ttk.Entry(root)
        case_entry.pack(pady=(1,1))
        self.case_name = case_entry
        case_entry_button = self.ttk.Button(root, text='Create New Case File', command = lambda: self.on_new_case_submit())
        case_entry_button.pack(pady=(1,0))
    
    def on_fill_in_doc(self):
        self.fill_in_doc = True
        self.attorney_selected = self.attorney_box.get()
        self.case_selected = self.case_box.get()
        text = None
        if self.case_selected == 'Select an Case Name':
            text = 'a case file'
        if self.attorney_selected == 'Select an Attorney':
            att_text = 'an attorney'
            if text:
                text += f', and {att_text}'
            else: 
                text = att_text
        if text:
            text = f'You must select {text} to begin formatting a document'
            print(text)
            self.fill_in_doc = False
            self.refresh_screen()
            return
        self.refresh_screen()

    def fill_in_doc_button(self, root):
        fill_in_doc_button = self.ttk.Button(root, text='Start Document', command= lambda: self.on_fill_in_doc())
        fill_in_doc_button.pack(pady=10)

    def begin_doc(self):
        if not self.fill_in_doc:
            return
        if not self.case_selected:
            print('you must select a case')
            return
        if not self.attorney_selected:
            print('you must select an attorney')
            return
        self.go_to_new_menu('Construct_Document')

    def on_delete_attorney_submit(self, data_base, editor):
        attorney_selected = self.attorney_selected.get()
        if not self.messagebox.askokcancel('Confirm Attorney Deletion', f'Do you really want delete {attorney_selected}?'):
            self.delete_attorney = False
            self.update_attorney = False
            self.refresh_screen()
            return
        data_base.get_attorney_path(attorney_selected)
        editor.destination_file_py = data_base.destination_file_py
        editor.remove_file()
        data_base.remove_attorney_from_db(attorney_selected)

    def on_delete_case_submit(self, data_base, editor):
        case_selected = self.case_selected.get()
        data_base.get_case_path(case_selected)
        editor.destination_file_py = data_base.destination_file_py 

    def delete_selected_item(self, root, data_base, editor):
        if self.delete_attorney:
            delete_button = self.ttk.Button(root, text = 'Delete Selected Attorney', command = lambda: self.on_delete_attorney_submit(data_base, editor))
        elif self.delete_case:
            delete_button = self.ttk.Button(root, text = 'Delete Selected Case', command = lambda: self.on_delete_case_submit(data_base, editor))
        else:
            return
        delete_button.pack()
        
    def menu_main(self, root, input_data, editor):
        # Extract input data
        data_base = input_data[0]
        self.template_selected = input_data[1]

        self.begin_doc()

        # Make a copy of the selected pdf and get related scripts and files
        self.get_called_document(data_base, editor)
        
        # Header for page
        header_frame = self.ttk.Frame(root)
        header_frame.pack()
        self.header_and_return_to_main(header_frame)

        # Query the user for attorney info for a drop down box
        attorneys = self.get_stored_attorney_names(data_base)
        # Query the user for case info by case name for a drop down box
        cases = self.get_stored_case_names(data_base)
        # Drop Down Frame
        option_frame = self.ttk.Frame(root)
        option_frame.pack()

        either = (self.add_attorney or self.delete_attorney) or (self.add_case or self.delete_case)
        if not either or self.update_case:
            self.case_box = self.display_options(option_frame, cases, 'Case Name')
        if not either or self.update_attorney:
            self.attorney_box = self.display_options(option_frame, attorneys, 'Attorney')
        
               
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
