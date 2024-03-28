class GUIManager():
    def __init__(self, display, messagebox):
        self.display = display
        self.messagebox = messagebox
        self.menus = []
        self.menu_names = []
        self.active_menu = None
        self.update_menu = True
        self.confirm_close_init = False
        self.selected_template = None
        self.selected_case = None
        self.selected_attorney = None

    def clear_window(self):
        for widget in self.display.winfo_children():
            widget.destroy()

    def init_display(self, name = 'default', scale_x = 0.4, scale_y = 0.6, centered = True):
        if centered:
            self.center_window(self.display, scale_x, scale_y)
        self.display.title(f'{name}')

    def init_confirm_close(self, session):
        if not self.confirm_close_init:
            self.display.protocol('WM_DELETE_WINDOW', lambda: self.close_window(session))
            self.confirm_close_init = True

    def center_window(self, window, scale_x, scale_y):
        window.update_idletasks()
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        window_width = int(screen_width * scale_x)
        window_height = int(screen_height * scale_y)
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 4
        window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def close_window(self, session):
        if self.messagebox.askokcancel('Quit', 'Do you really want to quit?'):
            session.active = False
            self.display.destroy()

    def select_menu(self, menu_name):
        if self.update_menu:
            for menu in self.menus:
                if menu.name == menu_name:
                    break
            self.active_menu = menu

    def set_menu(self, display, input, editor):
        if self.update_menu:
            self.update_menu = False
            self.active_menu.call_update = False
            self.clear_window()
            self.active_menu.menu_main(display, input, editor)

    def update_GUI(self, session, input, editor):
        # Init Confirmation box to prevent accidental closing the app early
        self.init_confirm_close(session)
        
        # Sets the menu and after an update is called, refreshes the display format
        self.set_menu(self.display, input, editor)
        
        # Checks to see if an update was called in the window and reports that to the manager
        if isinstance(self.active_menu.call_update, bool):
            self.update_menu = self.active_menu.call_update
        if isinstance(self.active_menu.selected_template, str) and self.active_menu.selected_template:
            self.selected_template = self.active_menu.selected_template
        
        self.display.update()
        
        
        

