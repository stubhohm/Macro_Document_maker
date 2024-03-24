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
        self.selected_template = None

    def on_box_select(self, box):
        self.selected_template = box.get()
        self.go_to_new_menu('Add_Case_Info')

    def refresh_screen(self):
        self.target_menu = self.name
        self.call_update = True

    def go_to_new_menu(self, target_menu):
        self.target_menu = target_menu
        self.call_update = True
        print(self.target_menu, self.call_update)

    def on_new_template_select(self):
        self.target_menu = 'Add_Template'
        self.call_update = True
    

    def add_new_template_button(self, root):
        new_template_button = self.ttk.Button(root, text='Add New Template', command= lambda: self.on_new_template_select())
        new_template_button.pack(pady=10)
        
    def get_options(self, documents):
        self.options = documents.get_template_names()
        

    def display_doc_options(self, root):
        combo_box = self.ttk.Combobox(root, values=self.options)
        combo_box.set('Select an option')
        combo_box.bind('<<ComboboxSelected>>', lambda event: self.on_box_select(combo_box))
        combo_box.pack(pady=10)

    def menu_main(self, root, documents, editor):
        # Gets list of stored template names
        self.get_options(documents)
        # Makes button and on click makes a request to update to add a new template
        self.add_new_template_button(root)
        # Displays that list in a dropdown box
        self.display_doc_options(root)
