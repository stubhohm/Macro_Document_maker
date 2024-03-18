testing_name = 'test beach visit'
testing_text = "I went to the beach on .date#date of beach visit#, and I spend the day with .name#beach friend 1#, .name#beach friend 2# and .name#beach friend 3#."

class AddTemplate():
    name = 'Add_Template'
    
    def __init__(self, display, tk, ttk, messagebox):
        self.display = display
        self.tk = tk
        self.ttk = ttk
        self.messagebox = messagebox
        self.call_update = False
        self.target_menu = None
        self.show_help = False
        self.template_submit = False
        self.nt_label = None
        self.nt_entry = None
        self.nt_name = None
        self.nt_text = None
        self.options = []
        self.validation_warnings = False

    def on_box_select(self):
        print('selected a thing')

    def new_template_submit(self, menu_names):
        for name in menu_names:
            if name == 'Add_Template':
                self.target_menu = name
                self.call_update = True
                break
        print('Sorry, an Error Occured. Error Code: MSAT2')

    def error_notify(self, ):
        self.messagebox.askokcancel('Formatting Error(s) Were Found', 'They have been flagged. \nPlease fix these and resubmit')
           
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
        
    def toggle_help(self):
        if self.show_help:
            self.show_help = False
            self.target_menu = self.name
            self.call_update = True
        else:
            self.show_help = True
            self.target_menu = self.name
            self.call_update = True

    def display_formatting(self, root):
        vspacing = (0,0)
        hspacing = (0,0)
        text_side = 'top'
        top_frame = self.ttk.Frame(root)
        top_frame.pack(side='top', fill='x', pady=10)
        help_button = self.ttk.Button(top_frame, text='Toggle Help Tips', command= lambda: self.toggle_help())
        help_button.pack(padx = 10, pady = vspacing, side ='right',)
        if not self.show_help:
            return
        help_frame = self.ttk.Frame(root)
        help_frame.pack(side='top', pady=10)
        instructions_text_box = self.ttk.Label(help_frame, text=f'Place a "." before a format type to add that to the document.')
        instructions_text_box.pack(pady=vspacing, side=text_side, padx=hspacing, anchor='w')
        comment_text_box = self.ttk.Label(help_frame, text=f'Place a "#" immediately after a querry to add a description of a querry, finish with another #, these can be edited later. \n The space inside the ## is a free space so enter whatever you feel helps')
        comment_text_box.pack(pady=vspacing, side=text_side, padx=hspacing, anchor='w')
        format_text_box = self.ttk.Label(help_frame, text=f'Formats include .date, .time, .name, .number, .w as wildcard. For a complete list of format types, type --help-- into the box and hit submit.')
        format_text_box.pack(pady=vspacing, side=text_side, padx=hspacing, anchor='w')
        example_text_box = self.ttk.Label(help_frame, text=f'Example: I went to the park on .date # Date of park visit #, and met with .name # Person met at park #.')
        example_text_box.pack(pady=vspacing, side=text_side, padx=hspacing, anchor='w')

    def check_for_doc_overwrite(self):
        for option_name in self.options:
            if self.nt_name == option_name:
                if self.confirm_overwrite(option_name):
                    self.call_update = True
                    self.target_menu = self.name
                    return
                else: 
                    self.template_submit = False
                    return
        self.call_update = True

    def get_new_template_data(self,):
        self.nt_name = self.nt_label.get()
        self.nt_text = self.nt_entry.get('1.0', "end-1c")
        
    def get_options(self, documents):
        self.options = documents.get_template_names()

    def enter_new_template_text(self, root, template_name, template_text = ''):
        if self.nt_entry:
            template_name = self.nt_name
            template_text = self.nt_text
        vspacing = (0,2)
        hspacing = (3,3)
        nt_frame = self.ttk.Frame(root)
        nt_frame.pack(side='top', fill='both', pady=10, expand=True)
        self.nt_label = self.ttk.Entry(nt_frame)
        self.nt_label.insert(0,template_name)
        self.nt_label.pack(pady=vspacing, padx=hspacing, anchor='w', fill='x')
        self.nt_entry = self.tk.Text(nt_frame, )
        self.nt_entry.insert('1.0', template_text)
        self.nt_entry.pack(pady=vspacing, padx=hspacing, anchor='w', fill='both', expand=True)

    def notify_tag_error(self, tag, re):
        tag_error = 'ERROR: NOT A RECOGNIZED TAG'
        content = re.search(tag, self.nt_text).group(1)
        self.nt_text = re.sub(tag,f'{tag_error} {content}')

    def notify_description_error(self, description, re):
        description_error = 'ERROR: DESCRIPTION TOO LONG, ENSURE IT IS CLOSED WITH "#"'
        content = re.search(description, self.nt_text).group(1)
        self.nt_text = re.sub(description,f'{description_error} {content}')

    def display_validation_errors(self, new_doc, re):
        error_present = False
        for i in range(len(new_doc.queries)):
            if not new_doc.valid_tags[i]:
                self.notify_tag_error(new_doc.queries[i][0], re)
                error_present = True
            if not new_doc.valid_description[i]:
                self.notify_description_error(new_doc.queries[i][1], re)
                error_present = True
        if error_present:
            self.error_notify()

    def submit_current_template(self, documents):
        if not self.template_submit:
            return
        self.get_new_template_data()    
        documents.validate_template_for_db(self.nt_name, self.nt_text)
        self.display_validation_errors(self, documents.new_doc, documents.re)

    def update_menu(self, root, menu_names, documents, editor, template_name ='Enter New Template Name'):
        
        # Gets a list of stored template names, used to prevent accidental overwriting or making two docs with the same name
        self.get_options(documents)
        
        # Shows a general list of format options and can be toggled on an off
        #self.display_formatting(root)
        
        # Field for entering new macro text and name 
        #self.enter_new_template_text(root, template_name=testing_name, template_text=testing_text)

        # If submition is valid and called, this function will run.
        #self.submit_current_template(documents)

        # Button to begin submittion of a created macro. Includes confirmation request and checks for overwrite with a second confirmation
        
        #self.submit_new_template_button(root)

