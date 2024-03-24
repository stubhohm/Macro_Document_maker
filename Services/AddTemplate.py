testing_name = 'test beach visit'
testing_text = "I went to the beach on .date#date of beach visit#, and I spend the day with .name#beach friend 1#, .name#beach friend 2# and .name#beach friend 3#."
from Classes.Case_fields import attorney_info, applicant_info, filing_info, decedent_info, interested_person
case_fields = ['None', 'Attorney', 'Applicant', 'Filing', 'Decenent', 'Interested Person']


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
        self.entries =[]
        self.define_fields = False
        self.submit_fields = False

    def clear_window(self, root):
        for widget in root.winfo_children():
            widget.destroy()

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
        documents.set_to_db(self.nt_name, self.nt_file_path)
        editor.input_pdf_path, editor.destination_file_py = documents.destination_file, documents.destination_file_py
        editor.doc_name = self.nt_name
        editor.open_pdf()
        print('opened')
        editor.get_fields()
        print('got fields')
        editor.add_existing_fields()
        print('added fields')
        editor.get_pdf_type()
        print(editor.pdf_type)
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
        self.define_fields = True
        self.refresh_screen()

    def field_submit_click(self):
        self.submit_fields = True
        self.refresh_screen()

    def field_submit_button(self, root):
        field_submit_button = self.tk.Button(root, text='Submit Field Definitions', command= lambda: self.field_submit_click())
        field_submit_button.pack(padx=20, pady=20, anchor='se')

    def add_case_info_options(self, sublist, dictionary, var, info_type):
        if info_type == 'None':
            sublist.add_command(label = 'None', command= lambda k='None': var.set(f'None'))
            return
        if info_type in ['Attorney', 'Applicant', 'Decedent', 'Interested Person']:
            sublist.add_command(label = 'Full Name', command= lambda k='Full Name': var.set(f'{info_type} {k}'))
            sublist.add_command(label = 'Full Address', command= lambda k='Full Address': var.set(f'{info_type} {k}'))
        if info_type == 'Applicant':
            sublist.add_command(label = 'Full Name, Address and Phone', command= lambda k='Full Name, Addrress and Phone': var.set(f'{info_type} {k}'))
        if info_type == 'Attorney':
            sublist.add_command(label = 'Full Name, Bar No, Address and Phone', command= lambda k='Full Name, Bar No, Address and Phone': var.set(f'{info_type} {k}'))
        if info_type == 'Filing':
            sublist.add_command(label = 'Full Address', command= lambda k='Full Address': var.set(f'{info_type} {k}'))
        for key in list(dictionary.keys()):
            sublist.add_command(label = key, command= lambda k=key: var.set(f'{info_type} {k}'))
        
    def add_cascades(self, menu, info_type, dictionary, var):
        sub_list = self.tk.Menu(menu, tearoff=False)
        menu.add_cascade(label = f'{info_type} Information', menu = sub_list)
        self.add_case_info_options(sub_list, dictionary, var, info_type)

    def make_field_entries(self, root, fields):
        canvas = self.tk.Canvas(root)
        scrollbar = self.ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        frame = self.ttk.Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor="nw")
        self.entries = []
        i = 0
        for field in fields:
            
            field_text = fields[field]
            if '/Kids' in field_text or field_text['/FT'] == '/Btn':
                continue
            # Make Label 
            label_text = f'{i+1}. Field Name: {field}'
            label = self.ttk.Label(frame, text = label_text)
            label.pack(fill='x', padx=(0, 10), pady=(5,0))
            row_frame = self.ttk.Frame(frame)
            row_frame.pack(fill = 'x')
            # Make Check Box
            check_false = self.tk.BooleanVar(value=False)
            check_text = 'Leave blank by default'
            check_box = self.ttk.Checkbutton(row_frame, text=check_text, variable=check_false)
            check_box.pack(side='left', padx=(0,0))
            # Make an drop down 
            var = self.tk.StringVar()
            option_menu = self.ttk.OptionMenu(row_frame, var, 'Case Information Fields')
            option_menu.pack()
            menu = option_menu['menu']
            self.add_cascades(menu, 'None', None, var)
            self.add_cascades(menu, 'Attorney', attorney_info, var)
            self.add_cascades(menu, 'Applicant', applicant_info, var)
            self.add_cascades(menu, 'Filing', filing_info, var)
            self.add_cascades(menu, 'Decedent', decedent_info, var)
            self.add_cascades(menu, 'Interested Person', interested_person, var)
            entry = {'field' : field,'var' : var, 'selection' : option_menu}
            self.entries.append(entry)
            i += 1
            
    def define_template_fields(self, root, documents, editor):
        if self.define_fields:
            # get our new local doc and py script for the new doc
            documents.get_local_doc_path(self.nt_name)
            documents.get_local_py_path(self.nt_name)
            
            # get new doc fields
            editor.input_pdf_path = documents.destination_file
            editor.open_pdf()
            editor.get_fields()
            self.clear_window(root)

            # Make an entry for each field that is not a button or has children
            self.make_field_entries(root, editor.existing_fields)
            # button to submit field definitions
            self.field_submit_button(root)
            return
        
    def open_file_dialog(self):
        self.nt_file_path = self.filedialog.askopenfilename(title="Select a File", filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")])
        self.get_new_template_data()
        self.refresh_screen()

    def submit_defined_fields(self, root, documents, editor):
        if not self.submit_fields:
            return
        please_wait = self.ttk.Label(root, text='Updating your Documents. Please Wait. \nOnce Finished, you will be returned to the Main Menu.')
        please_wait.pack()
        len_of_bar = len(self.entries) + int(len(self.entries) >> 2 )
        progress_bar = self.ttk.Progressbar(root, orient='horizontal', length = len_of_bar, mode='determinate')
        progress_bar.pack()
        # Get the script path
        documents.get_local_py_path(self.nt_name)
        editor.input_pdf_path = documents.destination_file_py
        # Open Script doc
        editor.open_py_file()
        
        # Find replace text with inputs given in self.entries
        editor.replace_place_holders(self.entries, progress_bar, len_of_bar)

    def menu_main(self, root, menu_names, documents, editor, template_name ='Enter New Template Name'):
        # If submition is valid and called, these functions will run.
        self.submit_defined_fields(root, documents, editor)
        if self.submit_fields:
            self.return_to_main_menu()
            self.submit_fields = False
            return
        self.define_template_fields(root, documents, editor)
        if self.define_fields:
            self.define_fields = False
            return
        self.submit_current_template(documents, editor)
        
        # Gets a list of stored template names, used to prevent accidental overwriting or making two docs with the same name
        self.get_options(documents)
        
        #button to return to main menu
        self.return_to_main_menu_button(root)
        
        # Field for entering new macro text and name 
        self.select_new_template_file(root, template_name)

        


