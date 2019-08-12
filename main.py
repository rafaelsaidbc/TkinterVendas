import sqlite3
import tkinter
from tkinter import *
from tkinter import messagebox
import datetime
import math

# conexão com o banco de dados
conn = sqlite3.connect('C:\\Users\\Usuario\\PycharmProjects\\TkinterVendas\\Database\\store.db')
c = conn.cursor()

# data atual
date = datetime.datetime.now().date()

# listas vazias
products_list = []
product_price = []
product_quantity = []
product_id = []
labels_list = []


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

        self.productname = Label(self.left, text='', font=('arial 20 bold'), bg='white', fg='green')
        self.productname.place(x=0, y=250)

        self.pprice = Label(self.left, text='', font=('arial 20 bold'), bg='white', fg='green')
        self.pprice.place(x=0, y=310)

        self.total_1 = Label(self.right, text='Total: ', font=('arial 40 bold'), bg='lightblue', fg='lightsalmon')
        self.total_1.place(x=0, y=600)

        # ========== ENTRY ==========
        self.enterid_e = Entry(self.left, width=25, font=('arial 18 bold'), bd='0', bg='lemonchiffon')
        self.enterid_e.place(x=140, y=80)

        # ========== BOTÕES ==========
        self.search_btn = Button(self.left, text='Pesquisar', width=22, height=2, bg='royalblue', fg='white',
                                 command=self.jx)
        self.search_btn.place(x=350, y=120)

    # função para receber os dados do banco de dados
    def jx(self, *args, **kwargs):
        self.get_id = self.enterid_e.get()
        query = "SELECT * FROM inventory WHERE id=?"
        result = c.execute(query, (self.get_id,))
        for self.r in result:
            self.get_id = self.r[0]
            self.get_name = self.r[1]
            self.get_stock = self.r[2]
            self.get_price = self.r[4]

        self.productname.configure(text='Nome do produto: ' + str(self.get_name))
        self.pprice.configure(text='Preço: R$' + str(self.get_price))

        self.quantity_1 = Label(self.left, text='Quantidade: ', font=('arial 18 bold'), bg='white')
        self.quantity_1.place(x=0, y=370)

        self.quantity_e = Entry(self.left, width=25, bd='0', font=('arial 18 bold'), bg='lightgray')
        self.quantity_e.place(x=190, y=370)
        self.quantity_e.focus()

        self.discunt_1 = Label(self.left, text='Desconto: ', font=('arial 18 bold'), bg='white')
        self.discunt_1.place(x=0, y=410)

        self.discunt_e = Entry(self.left, width=25, bd='0', font=('arial 18 bold'), bg='lightgray')
        self.discunt_e.place(x=190, y=410)
        self.discunt_e.insert(END, 0)

        self.car_btn = Button(self.left, text='Carrinho', width=22, height=2, bg='royalblue', fg='white',
                              command=self.Car)
        self.car_btn.place(x=350, y=450)

        self.change_1 = Label(self.left, text='Total a pagar: ', font=('arial 18 bold'), bg='white')
        self.change_1.place(x=0, y=550)

        self.change_e = Entry(self.left, width=25, bd='0', font=('arial 18 bold'), bg='bisque')
        self.change_e.place(x=190, y=550)

        self.change_btn = Button(self.left, text='Troco', width=22, height=2, bg='tomato', fg='white')
        self.change_btn.place(x=350, y=590)

        self.gerarrec_btn = Button(self.left, text='Recibo', width=22, height=2, bg='yellow')
        self.gerarrec_btn.place(x=350, y=640)

        # ========== FUNÇÕES ==========

    def Car(self, *args, **kwargs):
        self.quantity_value = int(self.quantity_e.get())
        if self.quantity_value > int(self.get_stock):
            tkinter.messagebox.showinfo('rafasaid@gmail.com', 'Quantidade não disponível no estoque!')
        else:
            self.final_price = (float(self.quantity_value) * float(self.get_price)) - (float(self.discunt_e.get()))
        products_list.append(self.get_name)
        product_price.append(self.final_price)
        product_quantity.append(self.quantity_value)
        product_id.append(self.get_id)

        self.x_index = 0
        self.y_index = 100
        self.counter = 0

        for self.p in products_list:
            self.tempname = Label(self.right, text=str(products_list[self.counter]), font=('arial 18 bold'),
                                  bg='lightblue', fg='darkviolet')
            self.tempname.place(x=0, y=self.y_index)
            labels_list.append(self.tempname)

            self.tempqt = Label(self.right, text=str(product_quantity[self.counter]), font=('arial 18 bold'),
                                bg='lightblue', fg='darkviolet')
            self.tempqt.place(x=300, y=self.y_index)
            labels_list.append(self.tempqt)

            self.tempprice = Label(self.right, text='R$' + str(product_price[self.counter]), font=('arial 18 bold'),
                                   bg='lightblue', fg='darkviolet')
            self.tempprice.place(x=500, y=self.y_index)
            labels_list.append(self.tempprice)

            self.y_index += 40
            self.counter += 1

            self.total_1.configure(text='Total: R$ ' + str(sum(product_price)))



root = Tk()
b = Application(root)
root.geometry('1366x768+0+0')
root.title("Supermercado Rafa Said")
root.mainloop()
