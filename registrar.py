from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import tkinter.ttk as ttk
from subprocess import call


class Database:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.heading = Label(master, text='Cadastro de usuários', font=('arial 40 bold'), fg='white',
                             bg='cornflowerblue')
        self.heading.place(x=200, y=100)

        # ========== LABELS ==========
        self.name_1 = Label(master, text='Nome do usuário: ', font=('arial 18 bold'), bg='cornflowerblue')
        self.name_1.place(x=50, y=320)

        self.senha_1 = Label(master, text='Senha: ', font=('arial 18 bold'), bg='cornflowerblue')
        self.senha_1.place(x=190, y=370)

        # ========== CAIXAS DE TEXTO (ENTRY) ==========
        self.name_e = Entry(master, width=25, font=('arial 18 bold'))
        self.name_e.place(x=300, y=320)

        self.senha_e = Entry(master, width=25, font=('arial 18 bold'))
        self.senha_e.place(x=300, y=370)

        # ========== BOTÕES ==========
        self.btn_cadastrar = Button(master, text='Cadastrar', font=('arial 10 bold'), width=20, height=2,
                                    bg='steelblue', fg='white')
        self.btn_cadastrar.place(x=300, y=420)

        self.btn_sair = Button(master, text='Sair', font=('arial 10 bold'), width=20, height=2,
                               bg='orange', fg='white')
        self.btn_sair.place(x=500, y=420)

        # ========== TEXT BOX ==========
        self.tbox = Text(master, width=30, height=15, bg='powderblue')
        self.tbox.place(x=720, y=250)


root = Tk()
b = Database(root)

root.geometry('1000x600+0+0')
root.title('Formulário de cadastro de usuários')
root.config(background='cornflowerblue')
root.mainloop()
