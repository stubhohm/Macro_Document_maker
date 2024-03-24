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

    def on_box_select(self, event):
        print(event)
        print(vars(event))
        
        print('selected a thing')

    def on_new_template_select(self, menu_names):
        for name in menu_names:
            if name == 'Add_Template':
                self.target_menu = name
                self.call_update = True
                return
        print('Sorry, an Error Occured. Error Code: MSM2')

    def add_new_template_button(self, root, menu_names):
        new_template_button = self.ttk.Button(root, text='Add New Template', command= lambda: self.on_new_template_select(menu_names))
        new_template_button.pack(pady=10)
        
    def get_options(self, documents):
        self.options = documents.get_template_names()
        
    def display_doc_options(self, root):
        combo_box = self.ttk.Combobox(root, values=self.options)
        combo_box.set('Select an option')
        combo_box.bind('<<ComboboxSelected>>', lambda event: self.on_box_select(event))
        combo_box.pack(pady=10)

    def refresh_screen(self):
        self.target_menu = self.name
        self.call_update = True

    def go_to_new_menu(self, target_menu):
        self.target_menu = target_menu
        self.call_update = True

    def get_called_document(self, documents, editor):
        if self.doc_inited:
            return
        print(f'selected template {self.selected_template}')
        documents.get_local_doc_path(self.selected_template)
        documents.get_local_py_path(self.selected_template)
        editor.input_pdf_path = documents.destination_file
        editor.destination_file_py = documents.destination_file_py
        editor.doc_name = self.selected_template
        editor.open_pdf()
        print('open')
        editor.copy_pdf()
        print('copy')
        editor.get_fields()
        print('fields')
        editor.get_pdf_type()
        print('type')
        self.doc_inited = True
        print('opened and primed')

    def menu_main(self, root, menu_names, input, editor):
        documents = input[0]
        self.selected_template = input[1]
        # Make a copy of the selected pdf
        self.get_called_document(documents, editor)
        
        # Get that pdfs template filling script

        # Query the user for case info by case name via drop down box

        # Query the user for attorney info via drop down box

        # Fill in doc button

        # Fill in is done find all boxes that have '' as their input and add them to a list
        # For each item in the list label = what type of case info it wants, checkbox to leave blank
        # update case info with filled in fields

        # publish doc
        '''
        editor.get_fields()
        print('got fields')
        editor.add_existing_fields()
        print('added fields')
        editor.get_pdf_type(self.nt_name)
        print('got type')
        editor.copy_pdf()
        print('made copy')
        editor.update_form_fields(None)
        print('updated fields')
        editor.fill_in_form()
        print('filed in form')
        editor.test_pdf()
        editor.output_new_doc()
        print('output doc')
        self.template_submit = False
        self.go_to_new_menu('Main_Screen')
        print('returned to main menu')
        
        # Gets list of stored template names
        self.get_options(documents)
        # Makes button and on click makes a request to update to add a new template
        self.add_new_template_button(root, menu_names)
        # Displays that list in a dropdown box
        self.display_doc_options(root)
        '''
