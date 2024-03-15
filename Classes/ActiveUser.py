class ActiveUser:
    def __init__(self, session, docs, ui_mngr):
        self.session = session
        self.docs = docs
        self.ui_mngr = ui_mngr
        self.input_data = None

    def init_menus(self, menus, tk, ttk, messagebox):
        uis = []
        ui_names = []
        for menu in menus:
            new_ui = menu(self.ui_mngr.display, tk, ttk, messagebox)
            uis.append(new_ui)
            ui_names.append(new_ui.name)
        self.ui_mngr.menus = uis
        self.ui_mngr.menu_names = ui_names

    def select_input(self):
        name = self.ui_mngr.active_menu.name
        if name == 'Main_Screen':
            self.input_data = self.docs