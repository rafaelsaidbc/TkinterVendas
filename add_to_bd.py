import sqlite3
import tkinter
from tkinter import *
from tkinter import messagebox

conn = sqlite3.connect('C:\\Users\\Usuario\\PycharmProjects\\TkinterVendas\\Database\\store.db')
c = conn.cursor()

result = c.execute('SELECT MAX(id) from inventory')
for r in result:
    id = r[0]


class Database:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.heading = Label(master, text='Cadastro de Produtos', font=('arial 40 bold'), fg='steelblue')
        self.heading.place(x=400, y=0)
        # ========== LABEL ==========
        self.name_1 = Label(master, text='Nome do Produto: ', font=('arial 18 bold'))
        self.name_1.place(x=0, y=70)

        self.stock_1 = Label(master, text='Estoque: ', font=('arial 18 bold'))
        self.stock_1.place(x=0, y=120)

        self.cp_1 = Label(master, text='Preço de custo: ', font=('arial 18 bold'))
        self.cp_1.place(x=0, y=170)

        self.sp_1 = Label(master, text='Preço de venda: ', font=('arial 18 bold'))
        self.sp_1.place(x=0, y=220)

        self.vendor_1 = Label(master, text='Nome do fornecedor: ', font=('arial 18 bold'))
        self.vendor_1.place(x=0, y=270)

        self.vendor_phone_1 = Label(master, text='Telefone do fornecedor: ', font=('arial 18 bold'))
        self.vendor_phone_1.place(x=0, y=320)

        self.id_1 = Label(master, text='ID: ', font=('arial 18 bold'))
        self.id_1.place(x=0, y=370)

        # ========== CAIXAS DE TEXTO ==========
        self.name_e = Entry(master, width=25, font=('arial 18 bold'))
        self.name_e.place(x=380, y=70)

        self.stock_e = Entry(master, width=25, font=('arial 18 bold'))
        self.stock_e.place(x=380, y=120)

        self.cp_e = Entry(master, width=25, font=('arial 18 bold'))
        self.cp_e.place(x=380, y=170)

        self.sp_e = Entry(master, width=25, font=('arial 18 bold'))
        self.sp_e.place(x=380, y=220)

        self.vendor_e = Entry(master, width=25, font=('arial 18 bold'))
        self.vendor_e.place(x=380, y=270)

        self.vendor_phone_e = Entry(master, width=25, font=('arial 18 bold'))
        self.vendor_phone_e.place(x=380, y=320)

        self.id_e = Entry(master, width=25, font=('arial 18 bold'))
        self.id_e.place(x=380, y=370)

        # ========== BOTÕES ==========
        self.btn_add = Button(master, text='Cadastrar', font=('arial 10 bold'), width=25, height=2, bg='steelblue',
                              fg='white', command=self.get_items)
        self.btn_add.place(x=550, y=420)

        self.btn_clear = Button(master, text='Limpar', font=('arial 10 bold'), width=18, height=2, bg='orange',
                                fg='white', command=self.clear_all)
        self.btn_clear.place(x=370, y=420)

        # =========== TEXT BOX ==========
        self.tbox = Text(master, width=60, height=18)
        self.tbox.place(x=810, y=70)
        self.tbox.insert(END, 'Último cadastro ID: ')

        self.master.bind('<Return>', self.get_items)
        self.master.bind('<Up>', self.clear_all)


    #função para obter os itens
    def get_items(self, *args, **kwargs):
        self.name = self.name_e.get()
        self.stock = self.stock_e.get()
        self.cp = self.cp_e.get()
        self.sp = self.sp_e.get()
        self.vendor = self.vendor_e.get()
        self.vendor_phone = self.vendor_phone_e.get()

        # soma dos totais
        self.totalcp = float(self.cp) * float(self.stock)
        self.totalsp = float(self.sp) * float(self.stock)

        # lucro = total preço de venda - preço de custo
        self.assumed_profit = float(self.totalsp - self.totalcp)

        #validação dos campos
        if self.name == '' or self.stock == '' or self.cp == '' or self.sp == '':
            tkinter.messagebox.showinfo('rafasaid@gmail.com', 'Favor preencha todos os campos')
        else:
            sql = "INSERT INTO inventory (name, stock, cp, sp, totalcp, totalsp, assumed_profit, vendor, vendor_phoneno) VALUES (?,?,?,?,?,?,?,?,?)"
            c.execute(sql,(self.name, self.stock, self.cp, self.sp, self.totalcp, self.totalsp, self.assumed_profit, self.vendor, self.vendor_phone))
            conn.commit()
            self.tbox.insert(END, '\n\nCadastrado ' + str(self.name) + ' ' + 'No banco de dados com ID: ' + str(
                self.id_e.get()))
            tkinter.messagebox.showinfo('rafasaid@gmail.com', 'Cadastro realizado com sucesso!')

    # função para limpar os campos
    def clear_all(self, *args, **kwargs):
        num = id + 1
        self.name_e.delete(0, END)
        self.stock_e.delete(0, END)
        self.cp_e.delete(0, END)
        self.sp_e.delete(0, END)
        self.vendor_e.delete(0, END)
        self.vendor_phone_e.delete(0, END)




root = Tk()
b = Database(root)
root.geometry('1366x768+0+0')
root.title('FORMULÁRIO DE CADASTRO')
root.mainloop()