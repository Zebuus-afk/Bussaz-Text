# coding: utf-8

from posixpath import split
from tkinter import *
import os
from tkinter import filedialog
from pathlib import Path
import tkinter.font as tkFont
from tkinter import messagebox

savedFile = { 1 : ""}


class textEditor :
    def __init__(self, master, content) :
        self.master = master
        self.content = content
        self.title = "BUSSAZ TEXT - v.1.2.0"
    
    ### ----- CRÉATION DE LA FENETRE PRINCIPALE ----- ###

    def create(self) :
        self.master = Tk()
        self.master.title(self.title)
        self.master.geometry("700x400")
        self.font = tkFont.Font(family="Lucida Grande", size=10)
    
    def add_text(self) :
        self.content = Text(self.master, undo=True, font=self.font)
        self.content.pack(expand=True, fill="both")
    
    def generate(self) :
        self.master.mainloop()
    
    ### ----- MENU FILE ----- ###

    def new(self) :
        path_past = __file__
        paths = path_past.split("lib\library.py")
        path = paths[0]
        d = ""
        for i in path.split("\\"):
            d = d + i + "/"
        os.popen("python " + d + "main.py")
    
    def open(self) :
        file = filedialog.askopenfilename(initialdir="/", title="Ouvrir", filetypes= (("Text File", "*.txt"), ("All Files", "*.*")))
        f = open(file, 'r')
        r = f.read()
        f.close()
        self.content.insert("1.0", r)
    
    def save_as(self) :
        file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="/", title="Enregistrer sous", filetypes=(("Text File", "*.txt"), ("XLS File", "*.xls"), ("All File", "*.*")))
        savedFile[1] = file
        f = open(file, 'w')
        s = self.content.get("1.0", END)
        f.write(s)
        f.close()

    def save(self) :
        if (savedFile[1] == "") :
            self.save_as()
        else :
            f = open(savedFile[1], 'w')
            s = self.content.get("1.0", END)
            f.write(s)
            f.close()

    ### ----- MENU EDITION ----- ###
   
    def copy(self) :
        self.content.clipboard_clear()
        self.content.clipboard_append(self.content.selection_get())

    def cut(self) :
        self.copy()
        self.content.delete('sel.first', 'sel.last')

    def paste(self) :
        self.content.insert(INSERT, self.content.clipboard_get())

    def cancel(self) :
        self.content.edit_undo()

    def restore(self) :
        self.content.edit_redo()

    ### ----- MENU WINDOW ----- ###

    def quit(self) :
        self.master.quit()
    
    ### ----- MENU ABOUT ----- ###

    def about(self) :
        self.error_101()
    
    def about_shell(self) :
        self.error_101()
    
    def about_error(self) :
        self.error_101()
    
    ### ----- MENU FONT ----- ###

    def f_font_helvetica(self) :
        self.content.configure(tkFont.Font(family="Helvetica", size=10))

    def f_font_lucida_grande(self) :
        #self.content.pack_forget()
        self.content.configure(font=tkFont.Font(family="Lucida Grande", size=10))

    def f_font_system(self) :
        self.content.configure(tkFont.Font(family="System", size=10))
    
    def f_font_terminal(self) :
        self.content.configure(tkFont.Font(family="Terminal", size=10))

    def f_font_times(self) :
        #self.content.pack_forget()
        self.content.configure(font=tkFont.Font(family="Times", size=10))

    ### ----- ERREUR ----- ###

    def error_101(self) :
        messagebox.showerror(self.title + " - ERREUR 101", "Cette fonctionnalité n'est pas encore disponible.")

    ### ----- CRÉATION DU MENU ----- ###

    def add_menu(self) :
        menu = Menu(self.master)        
        menu_file = Menu(menu, tearoff=False)
        menu_edition = Menu(menu, tearoff=False)
        menu_window = Menu(menu, tearoff=False)
        menu_about = Menu(menu, tearoff=False)
        menu_font = Menu(menu, tearoff=False)
        menu.add_cascade(label="Fichier", menu=menu_file)
        menu_file.add_command(label="Nouveau", command=self.new)
        menu_file.add_command(label="Ouvrir...", command=self.open)
        menu_file.add_command(label="Enregistrer", command=self.save)
        menu_file.add_command(label="Enregistrer sous...", command=self.save_as)
        menu.add_cascade(label="Édition", menu=menu_edition)
        menu_edition.add_command(label="Copier", command=self.copy)
        menu_edition.add_command(label="Couper", command=self.cut)
        menu_edition.add_command(label="Coller", command=self.paste)
        menu_edition.add_separator()
        menu_edition.add_command(label="Annuler", command=self.cancel)
        menu_edition.add_command(label="Rétablir", command=self.restore)
        menu.add_cascade(label="Fenêtre", menu=menu_window)
        menu_window.add_command(label="Quitter", command=self.quit)
        menu.add_cascade(label="A propos", menu=menu_about)
        menu_about.add_command(label="Généralité", command=self.about)
        menu_about.add_command(label="Console", command=self.about_shell)
        menu_about.add_command(label="Code erreur", command=self.about_error)
        menu.add_cascade(label="Police", menu=menu_font)
        #menu_font.add_command(label="Helvetica", command=self.f_font_helvetica)
        menu_font.add_command(label="Lucida Grande", command=self.f_font_lucida_grande)
        #menu_font.add_command(label="Terminal", command=self.f_font_terminal)
        menu_font.add_command(label="Times", command=self.f_font_times)
        #menu_font.add_command(label="System", command=self.f_font_system)

        self.master.config(menu=menu)