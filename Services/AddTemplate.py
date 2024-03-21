testing_name = 'test beach visit'
testing_text = "I went to the beach on .date#date of beach visit#, and I spend the day with .name#beach friend 1#, .name#beach friend 2# and .name#beach friend 3#."

class AddTemplate():
    name = 'Add_Template'
    
    def __init__(self, display, tk, ttk, messagebox, filedialog):
        self.display = display
        self.tk = tk
        self.ttk = ttk
        self.messagebox = messagebox
        self.filedialog = filedialog
        self.call_update = False
        self.target_menu = None
        self.show_help = False
        self.template_submit = False
        self.nt_label = None
        self.nt_file = None
        self.nt_name = None
        self.nt_file_path = None
        self.options = []
        self.validation_warnings = False

    def on_box_select(self):
        print('selected a thing')

    def refresh_screen(self):
        self.target_menu = self.name
        self.call_update = True

    def go_to_new_menu(self, target_menu):
        self.target_menu = target_menu
        self.call_update = True

    def new_template_submit(self, menu_names):
        for name in menu_names:
            if name == 'Add_Template':
                self.target_menu = name
                self.call_update = True
                break
        print('Sorry, an Error Occured. Error Code: MSAT2')
         
    def confirm_submit(self,):
        # Puts up a message box to confirm submission
        if self.messagebox.askokcancel('Submit New Template', 'Are you ready to submit?'):
            self.template_submit = True
            # Checks to ensure we are not overwriting an existing doc, and is so, asks for confirmation.
            self.get_new_template_data()
            self.check_for_doc_overwrite()
        else:
            self.template_submit = False

    def confirm_overwrite(self, name):
        if self.messagebox.askokcancel('Overwrite Existing Template', f'A template with the name {name} already exists. /n Are you sure you wish to overwrite that template?'):
            return True
        else:
            return False

    def submit_new_template_button(self, root):
        new_template_button = self.ttk.Button(root, text='Submit New Template', command= lambda: self.confirm_submit())
        new_template_button.pack(pady=10)

    def check_for_doc_overwrite(self):
        for option_name in self.options:
            if self.nt_name == option_name:
                if self.confirm_overwrite(option_name):
                    self.refresh_screen()
                    return
                else: 
                    self.template_submit = False
                    return
        self.call_update = True

    def get_new_template_data(self,):
        self.nt_name = self.nt_label.get()
        
    def get_options(self, documents):
        self.options = documents.get_template_names()

    def select_new_template_file(self, root, template_name):
        if self.nt_file_path:
            template_name = self.nt_name
        vspacing = (0,2)
        hspacing = (3,3)
        nt_frame = self.ttk.Frame(root)
        nt_frame.pack(side='top', fill='both', pady=10, expand=True)
        self.nt_label = self.ttk.Entry(nt_frame)
        self.nt_label.insert(0, template_name)
        self.nt_label.pack(pady=vspacing, padx=hspacing, anchor='w', fill='x')
        
        open_button = self.tk.Button(nt_frame, text='Open File', command= lambda: self.open_file_dialog())
        open_button.pack(padx=20, pady=20)
        selected_file_label = self.tk.Label(nt_frame, text=f'Selected File:{self.nt_file_path}')
        selected_file_label.pack()
        
        if self.nt_file_path:
            self.submit_new_template_button(nt_frame)

    def return_to_main_menu(self):
        self.template_submit = False
        self.go_to_new_menu('Main_Screen')

    def return_to_main_menu_button(self, root):
        nt_frame = self.ttk.Frame(root)
        nt_frame.pack(side='top', pady=10)       
        main_menu_button = self.tk.Button(nt_frame, text='Return to Main Menu', command= lambda: self.return_to_main_menu())
        main_menu_button.pack(padx=20, pady=20)

    def submit_current_template(self, documents, editor):
        if not self.template_submit:
            return
        self.get_new_template_data()    
        documents.set_to_db(self.nt_name, self.nt_file_path)
        editor.input_pdf_path, editor.destination_file_py = documents.destination_file, documents.destination_file_py
        editor.open_pdf()
        print('opened')
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
        editor.test_pdf(self.nt_name)
        editor.output_new_doc()
        print('output doc')
        self.template_submit = False
        self.go_to_new_menu('Main_Screen')
        print('returned to main menu')

    def open_file_dialog(self):
        self.nt_file_path = self.filedialog.askopenfilename(title="Select a File", filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")])
        self.get_new_template_data()
        self.refresh_screen()

    def update_menu(self, root, menu_names, documents, editor, template_name ='Enter New Template Name'):
        # Gets a list of stored template names, used to prevent accidental overwriting or making two docs with the same name
        self.get_options(documents)
        
        #button to return to main menu
        self.return_to_main_menu_button(root)
        
        # Field for entering new macro text and name 
        self.select_new_template_file(root, template_name)

        # If submition is valid and called, this function will run.
        self.submit_current_template(documents, editor)


