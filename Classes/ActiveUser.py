class ActiveUser:
    def __init__(self, session, docs, ui_mngr, editor):
        self.session = session
        self.docs = docs
        self.ui_mngr = ui_mngr
        self.editor = editor
        self.input_data = None

    def init_menus(self, menus, tk, ttk, messagebox, filedialog):
        for menu in menus:
            new_ui = menu(display=self.ui_mngr.display, tk=tk, ttk=ttk, messagebox=messagebox, filedialog=filedialog)
            self.ui_mngr.menus.append(new_ui)
            self.ui_mngr.menu_names.append(new_ui.name)
        self.ui_mngr.menu_names.append(self.editor.name)
        print(f'init_menus {self.ui_mngr.menu_names}')

    def select_input(self):
        name = self.ui_mngr.active_menu.name
        if name == 'Main_Screen':
            self.input_data = self.docs