import sqlite3
from tkinter import *
from tkinter import messagebox
import datetime

# conexão com o banco de dados
conn = sqlite3.connect('C:\\Users\\Usuario\\PycharmProjects\\TkinterVendas\\Database\\store.db')
c = conn.cursor()

# data atual
date = datetime.datetime.now().date()


class Application:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.left = Frame(master, width=700, height=768, bg='white')
        self.left.pack(side=LEFT)
        self.right = Frame(master, width=666, height=768, bg='lightblue')
        self.right.pack(sid=RIGHT)

        # ========== LABELS ==========
        self.heading = Label(self.left, text='Supermercado Rafa Said', font=('arial 38 bold'), bg='lightblue')
        self.heading.place(x=0, y=0)

        self.date_1 = Label(self.right, text='Data: ' + str(date), font=('arial 16 bold'), bg='lightblue')
        self.date_1.place(x=0, y=0)

        self.tproduct = Label(self.right, text='Produto:', font=('arial 18 bold'), bg='lightblue', fg='white')
        self.tproduct.place(x=0, y=60)

        self.tquantity = Label(self.right, text='Quantidade:', font=('arial 18 bold'), bg='lightblue', fg='white')
        self.tquantity.place(x=300, y=60)

        self.tamount = Label(self.right, text='Valor:', font=('arial 18 bold'), bg='lightblue', fg='white')
        self.tamount.place(x=500, y=60)

        self.enterid = Label(self.left, text='Produto ID:', font=('arial 16 bold'), bg='white')
        self.enterid.place(x=0, y=80)

        self.productname = Label(self.left, text='Nome do produto: ', font=('arial 27 bold'), bg='white', fg='green')
        self.productname.place(x=0, y=250)

        self.pprice = Label(self.left, text='Preço do produto: ', font=('arial 27 bold'), bg='white', fg='green')
        self.pprice.place(x=0, y=310)

        self.total_1 = Label(self.right, text='Total: ', font=('arial 40 bold'), bg='lightblue', fg='lightsalmon')
        self.total_1.place(x=0, y=600)

        # ========== ENTRY ==========
        self.enterid_e = Entry(self.left, width=25, font=('arial 18 bold'), bd='0', bg='lemonchiffon')
        self.enterid_e.place(x=140, y=80)

        # ========== BOTÕES ==========
        self.search_btn = Button(self.left, text='Pesquisar', width=22, height=2, bg='royalblue', fg='white')
        self.search_btn.place(x=350, y=120)


root = Tk()
b = Application(root)
root.geometry('1366x768+0+0')
root.title("Supermercado Rafa Said")
root.mainloop()
