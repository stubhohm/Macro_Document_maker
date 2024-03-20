import tkinter as tk 
import sqlite3
import re
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from tkinter import Tk, ttk, messagebox, filedialog
from Classes.ActiveUser import ActiveUser
from Classes.Query import Query, tags
from Classes.Session import Session
from Classes.Documents import Documentsdb
from Classes.CaseInformation import CaseInformation
from Classes.DocumentEditor import DocumentEditor
from Services.GUIManager import GUIManager
from Services.MainScreen import MainScreen
from Services.AddTemplate import AddTemplate
menus = [MainScreen, AddTemplate]

def init_instances():
    # UI Mngr houses the other screens and handles clearing and switching between screen displays
    ui_mngr = GUIManager(Tk(), messagebox)
    ui_mngr.init_display('Macro Document Maker')
    docs_db = Documentsdb(sqlite3, re)
    docs_db.init_db()
    doc_editor = DocumentEditor(PdfReader, PdfWriter, canvas, letter)
    # User is the root variable that all the other objects and instances will branch from
    user = ActiveUser(Session(), docs_db, ui_mngr, doc_editor)
    return user

def close_application(user):
    user.docs.close_db()

def main():
    user = init_instances()
    user.init_menus(menus, tk, ttk, messagebox, filedialog)

    # This is here to pick the starting screen for the ui_manager, the input coresponds to the '.name' in the screens in Services
    user.ui_mngr.select_menu('Main_Screen')
    print(type(user.ui_mngr.active_menu))
    while user.session.active:
        # Function looks at the active menu, and decides what input data that menu requests and returns that input
        user.select_input()

        # Handles GUI updates, requests for switching and input handling
        user.ui_mngr.update_GUI(user.session, user.input_data, user.editor)

        # Validates GUI screen switches and initates that action
        user.ui_mngr.select_menu(user.ui_mngr.active_menu.target_menu)
    close_application(user)
        

if __name__ == "__main__":
    
    main()
    print(
        "this main only runs if this file is ran, not if another program executes it: Macro_maker"
    )