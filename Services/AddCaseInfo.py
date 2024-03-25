from Classes.Case_fields import attorney_info

class AddCaseInfo():
    name = 'Add_Case_Info'
    
    def __init__(self, display, tk, ttk, messagebox, filedialog):
        self.display = display
        self.tk = tk
        self.ttk = ttk
        self.messagebox = messagebox
        self.filedialog = filedialog
        self.call_update = False
        self.target_menu = None
        self.options = []
        self.att_fields = []
        self.selected_template = None
        self.required_fields = None
        self.case_name = None
        self.doc_inited = False
        self.add_case = False
        self.sub_case = False
        self.add_attorney = False
        self.sub_att = False
        self.attorney_selected = None
        self.case_selected = None
        self.fill_in_doc = False


    def refresh_screen(self):
        self.target_menu = self.name
        self.call_update = True

    def go_to_new_menu(self, target_menu):
        self.target_menu = target_menu
        self.call_update = True

    def on_box_select(self, event):
        print(event)
        print(vars(event))
        
        print('selected a thing')

    def get_called_document(self, data_base, editor):
        if self.doc_inited:
            return
        data_base.get_local_doc_path(self.selected_template)
        data_base.get_local_py_path(self.selected_template)
        editor.input_pdf_path = data_base.destination_file
        editor.destination_file_py = data_base.destination_file_py
        editor.doc_name = self.selected_template
        editor.open_pdf()
        editor.copy_pdf()
        editor.get_fields()
        editor.get_pdf_type()
        self.doc_inited = True

    def header_and_return_to_main(self, root):
        header = self.ttk.Label(root, text=f'Filling out {self.selected_template} template.')
        header.pack() 
        main_menu_button = self.ttk.Button(root, text='Return to Main Menu', command= lambda: self.go_to_new_menu('Main_Screen'))
        main_menu_button.pack(pady=10)

    def display_options(self, root, options, selection_type):
        combo_box = self.ttk.Combobox(root, values=options)
        combo_box.set(f'Select an {selection_type}')
        combo_box.bind('<<ComboboxSelected>>', lambda event: self.on_box_select(event))
        combo_box.pack(pady=10)
        return combo_box

    def get_stored_case_names(self, data_base, root):
        names = data_base.get_case_names()
        self.case_selected = self.display_options(root, names, 'Case Name')

    def get_stored_attorney_names(self, data_base, root):
        names = data_base.get_attorney_names()
        self.attorney_selected = self.display_options(root, names, 'Attorney')


    def add_new_case_or_attorney_button(self, root):
        new_case_button = self.ttk.Button(root, text='Add New Case', command= lambda: self.on_new_case_select())
        new_case_button.pack(pady=10)
        new_attorney_button = self.ttk.Button(root, text='Add New Attorney', command= lambda: self.on_new_attorney_select())
        new_attorney_button.pack(pady=10)

    def on_new_attorney_select(self):
        self.add_attorney = True
        print('add attorney')
        self.refresh_screen()

    def on_new_case_select(self):
        self.add_case = True
        print('new case')
        self.refresh_screen()

    def submit_att(self):
        self.get_fields()

    def get_fields(self):
        for i, item in enumerate(self.att_fields):
            entry = item[1]
            text = entry.get()
            self.att_fields[i][1] = text
        self.sub_att = True

    def validate_att_fields():
        valid = True
        return valid

    def make_new_attorney_doc(self, editor):
        name = None
        path = None
        return name, path

    def create_new_attorney(self, data_base, editor):
        if not self.validate_att_fields():
            return
        name, path  = self.make_new_attorney_doc(editor)
        data_base.add_attorney_to_db(name, path)
        self.sub_att = False

    def add_attorney_fields(self, data_base, editor, root):
        if self.sub_att:
            self.create_new_attorney(data_base, editor)
        if not self.add_attorney:
            return
        append = True
        if self.att_fields:
            append = False
        for i, key in enumerate(attorney_info.keys()):
            label_text = f'{i+1}. {key}'
            label = self.ttk.Label(root, text = label_text)
            label.pack(pady=(3,0))
            entry = self.ttk.Entry(root)
            entry.pack()
            if not append:
                entry.insert(0,self.att_fields[i][1])
            if append:
                self.att_fields.append([key, entry])
            else:
                self.att_fields[i] = [key, entry]
        
        for item in self.att_fields:
            entry = item[1]
            print(entry)
            text = entry.get()
            print(text)
        
        submit_button = self.ttk.Button(root, text = "Submit Attorney info", command = lambda: self.submit_att() )
        submit_button.pack()

    def add_case_file(self, data_base, editor, root):
        if not self.add_case:
            return
        # Get new Case name
        # Make new case file with the given name
    
    def on_fill_in_dco(self):
        self.fill_in_doc = True
        self.refresh_screen()

    def fill_in_doc_button(self, root):
        fill_in_doc_button = self.ttk.Button(root, text='Add New Case', command= lambda: self.on_fiil_in_doc())
        fill_in_doc_button.pack(pady=10)

    def menu_main(self, root, input, editor):
        # Extract input data
        data_base = input[0]
        self.selected_template = input[1]
        
        # Make a copy of the selected pdf and get related scripts and files
        self.get_called_document(data_base, editor)
        header_frame = self.ttk.Frame(root)
        header_frame.pack()
        self.header_and_return_to_main(header_frame)
        first_frame = self.ttk.Frame(root)
        first_frame.pack()

        # If user selected to fill in Case or Attorny Data these functions run
        self.add_attorney_fields(data_base, editor, first_frame)
        self.add_case_file(data_base, editor, first_frame)
        if self.add_attorney or self.add_case:
            self.add_attorney, self.add_case = False, False
            return
        if self.sub_att or self.sub_case:
            self.sub_att, self.sub_case = False, False
            return            
        
        # Query the user for case info by case name via drop down box
        self.get_stored_case_names(data_base, first_frame)
        
        # Query the user for attorney info via drop down box
        self.get_stored_attorney_names(data_base, first_frame)

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
