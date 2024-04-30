class MainScreen():
    name = 'Main_Screen'
    
    def __init__(self, display, tk, ttk, messagebox, filedialog):
        self.display = display
        self.tk = tk
        self.ttk = ttk
        self.messagebox = messagebox
        self.filedialog = filedialog
        self.call_update = False
        self.target_menu = None
        self.options = []
        self.template_selected = None
        self.attorney_selected = None
        self.case_selected = None
        self.templates = []

    def on_box_select(self, box):
        self.template_selected = box.get()
        self.go_to_new_menu('Add_Case_Info')

    def refresh_screen(self):
        self.target_menu = self.name
        self.call_update = True

    def go_to_new_menu(self, target_menu):
        self.target_menu = target_menu
        self.call_update = True

    def on_new_template_select(self):
        self.target_menu = 'Add_Template'
        self.call_update = True
    
    def add_new_template_button(self, root):
        new_template_button = self.ttk.Button(root, text='Add New Template', command= lambda: self.on_new_template_select())
        new_template_button.pack(pady=10)
        
    def get_options(self, documents):
        self.options = documents.get_template_names()
        holder = []
        for option in self.options:
            option = option[0]
            option = option.strip('{')
            option = option.strip('}')
            holder.append(option)
        self.options = holder

    def on_check(self, item, checkbox_var):
        if checkbox_var.get() == 1:
            self.templates.append(item)
            print(self.templates)
        else:
            self.templates.remove(item)
            print(self.templates)
        
    def display_doc_options(self, root):
        box_label = self.ttk.Label(root, text='Select an Existing Template')
        box_label.pack(pady=(2,0))
        combo_box = self.ttk.Combobox(root, values=self.options)
        combo_box.set('Select an option')
        combo_box.bind('<<ComboboxSelected>>', lambda event: self.on_box_select(combo_box))
        combo_box.pack()
        checkbox_vars = []
        for option in self.options:
            var = self.tk.IntVar()
            checkbox_vars.append(var)
            row = self.ttk.Frame(root)
            row.pack()
            check = self.ttk.Checkbutton(row, text = option, variable=var, command=lambda item=option, var=var: self.on_check(item, var))
            check.pack(side = 'left')

    def menu_main(self, root, documents, editor):
        # Gets list of stored template names
        self.get_options(documents)
        # Makes button and on click makes a request to update to add a new template
        self.add_new_template_button(root)
        # Displays that list in a dropdown box
        options_frame = self.ttk.Frame(root)
        options_frame.pack()
        self.display_doc_options(options_frame)
