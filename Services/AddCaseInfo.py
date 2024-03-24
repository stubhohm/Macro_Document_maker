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
        self.selected_template = None
        self.required_fields = None
        self.case_name = None
        self.doc_inited = False
        self.add_case = True
        self.add_attorney = True
        self.attorney_selected = None
        self.case_selected = None

    def on_box_select(self, event):
        print(event)
        print(vars(event))
        
        print('selected a thing')

    def on_new_attorney_select(self):
        self.add_attorney = True
        self.refresh_screen()

    def on_new_case_select(self):
        self.add_case = True
        self.refresh_screen()

    def add_new_case_or_attorney_button(self, root):
        new_case_button = self.ttk.Button(root, text='Add New Case', command= lambda: self.on_new_case_select())
        new_case_button.pack(pady=10)
        new_attorney_button = self.ttk.Button(root, text='Add New Attorney', command= lambda: self.on_new_attorney_select())
        new_attorney_button.pack(pady=10)
   
    def display_options(self, root, options, selection_type):
        combo_box = self.ttk.Combobox(root, values=options)
        combo_box.set(f'Select an {selection_type}')
        combo_box.bind('<<ComboboxSelected>>', lambda event: self.on_box_select(event))
        combo_box.pack(pady=10)
        return combo_box

    def refresh_screen(self):
        self.target_menu = self.name
        self.call_update = True

    def go_to_new_menu(self, target_menu):
        self.target_menu = target_menu
        self.call_update = True

    def get_called_document(self, documents, editor):
        if self.doc_inited:
            return
        documents.get_local_doc_path(self.selected_template)
        documents.get_local_py_path(self.selected_template)
        editor.input_pdf_path = documents.destination_file
        editor.destination_file_py = documents.destination_file_py
        editor.doc_name = self.selected_template
        editor.open_pdf()
        editor.copy_pdf()
        editor.get_fields()
        editor.get_pdf_type()
        self.doc_inited = True

    def get_stored_case_names(self, documents, root):
        names = documents.get_case_names()
        self.case_selected = self.display_options(root, names, 'Case Name')

    def get_stored_attorney_names(self, documents, root):
        names = documents.get_attorney_names()
        self.attorney_selected = self.display_options(root, names, 'Attorney')

    def header_and_return_to_main(self, root):
        header = self.ttk.Label(root, text=f'Filling out {self.selected_template} template.')
        header.pack() 
        main_menu_button = self.ttk.Button(root, text='Return to Main Menu', command= lambda: self.go_to_new_menu('Main_Screen'))
        main_menu_button.pack(pady=10)

    def menu_main(self, root, input, editor):
        documents = input[0]
        self.selected_template = input[1]
        
        # Make a copy of the selected pdf and get related scripts and files
        self.get_called_document(documents, editor)
        header_frame = self.ttk.Frame(root)
        header_frame.pack()
        self.header_and_return_to_main(header_frame)
        first_frame = self.ttk.Frame(root)
        first_frame.pack()
        # Query the user for case info by case name via drop down box
        self.get_stored_case_names(documents, first_frame)
        
        # Query the user for attorney info via drop down box
        self.get_stored_attorney_names(documents, first_frame)

        second_frame = self.ttk.Frame(root)
        second_frame.pack(fill = 'x')
        self.add_new_case_or_attorney_button(second_frame)
        # Fill in doc button

        # Fill in is done find all boxes that have '' as their input and add them to a list
        # For each item in the list label = what type of case info it wants, checkbox to leave blank
        # update case info with filled in fields

        # publish doc
