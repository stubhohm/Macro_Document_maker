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

    def update_menu(self, root, menu_names, documents, editor):
        # Gets list of stored template names
        self.get_options(documents)
        # Makes button and on click makes a request to update to add a new template
        self.add_new_template_button(root, menu_names)
        # Displays that list in a dropdown box
        self.display_doc_options(root)
