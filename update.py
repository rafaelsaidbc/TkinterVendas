import sqlite3
from tkinter import *
import tkinter
from tkinter import messagebox

conn = sqlite3.connect('C:\\Users\\Usuario\\PycharmProjects\\TkinterVendas\\Database\\store.db')
c = conn.cursor()

result = c.execute('SELECT MAX(id) from inventory')
for r in result:
    id = r[0]


class Database:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.heading = Label(master, text='Atualização de Produtos', font=('arial 40 bold'), fg='steelblue',
                             bg='darkseagreen')
        self.heading.place(x=400, y=0)

        # ========== LABEL ==========
        self.id_le = Label(master, text='Digite ID: ', font=('arial 18 bold'), bg='darkseagreen')
        self.id_le.place(x=0, y=70)

        self.id_leb = Entry(master, width=10, font=('arial 18 bold'))
        self.id_leb.place(x=380, y=70)

        self.btn_search = Button(master, text='Pesquisar', font=('arial 10 bold'), width=15, height=2, bg='orange',
                                 command=self.search)
        self.btn_search.place(x=550, y=70)

        self.name_1 = Label(master, text='Nome do Produto: ', font=('arial 18 bold'), bg='darkseagreen')
        self.name_1.place(x=0, y=120)

        self.stock_1 = Label(master, text='Estoque: ', font=('arial 18 bold'), bg='darkseagreen')
        self.stock_1.place(x=0, y=170)

        self.cp_1 = Label(master, text='Preço de custo: ', font=('arial 18 bold'), bg='darkseagreen')
        self.cp_1.place(x=0, y=220)

        self.sp_1 = Label(master, text='Preço de venda: ', font=('arial 18 bold'), bg='darkseagreen')
        self.sp_1.place(x=0, y=270)

        self.totalcp_1 = Label(master, text='Total do preço de custo: ', font=('arial 18 bold'), bg='darkseagreen')
        self.totalcp_1.place(x=0, y=320)

        self.totalsp_1 = Label(master, text='Total do preço de venda: ', font=('arial 18 bold'), bg='darkseagreen')
        self.totalsp_1.place(x=0, y=370)

        self.vendor_1 = Label(master, text='Nome do fornecedor: ', font=('arial 18 bold'), bg='darkseagreen')
        self.vendor_1.place(x=0, y=420)

        self.vendor_phone_1 = Label(master, text='Telefone do fornecedor: ', font=('arial 18 bold'), bg='darkseagreen')
        self.vendor_phone_1.place(x=0, y=470)

        # ========== CAIXAS DE TEXTO ==========
        self.name_e = Entry(master, width=25, font=('arial 18 bold'))
        self.name_e.place(x=380, y=120)

        self.stock_e = Entry(master, width=25, font=('arial 18 bold'))
        self.stock_e.place(x=380, y=170)

        self.cp_e = Entry(master, width=25, font=('arial 18 bold'))
        self.cp_e.place(x=380, y=220)

        self.sp_e = Entry(master, width=25, font=('arial 18 bold'))
        self.sp_e.place(x=380, y=270)

        self.totalcp_e = Entry(master, width=25, font=('arial 18 bold'))
        self.totalcp_e.place(x=380, y=320)

        self.totalsp_e = Entry(master, width=25, font=('arial 18 bold'))
        self.totalsp_e.place(x=380, y=370)

        self.vendor_e = Entry(master, width=25, font=('arial 18 bold'))
        self.vendor_e.place(x=380, y=420)

        self.vendor_phone_e = Entry(master, width=25, font=('arial 18 bold'))
        self.vendor_phone_e.place(x=380, y=470)

        # ========== BOTÕES ==========
        self.btn_add = Button(master, text='Atualizar', font=('arial 10 bold'), width=25, height=2, bg='steelblue',
                              fg='white', command=self.update)
        self.btn_add.place(x=550, y=520)


        # =========== TEXT BOX ==========
        self.tbox = Text(master, width=60, height=18, bg='moccasin')
        self.tbox.place(x=810, y=70)
        self.tbox.insert(END, 'Último cadastro ID: ' + str(id))

    def search(self, *args, **kwargs):
        sql = "SELECT * FROM inventory WHERE id=?"
        result = c.execute(sql, (self.id_leb.get(),))
        for r in result:
            self.n1 = r[1]
            self.n2 = r[2]
            self.n3 = r[3]
            self.n4 = r[4]
            self.n5 = r[5]
            self.n6 = r[6]
            self.n7 = r[7]
            self.n8 = r[8]
            self.n9 = r[9]
        conn.commit()
        self.name_e.delete(0, END)
        self.name_e.insert(0, str(self.n1))

        self.stock_e.delete(0, END)
        self.stock_e.insert(0, str(self.n2))

        self.cp_e.delete(0, END)
        self.cp_e.insert(0, str(self.n3))

        self.sp_e.delete(0, END)
        self.sp_e.insert(0, str(self.n4))

        self.vendor_e.delete(0, END)
        self.vendor_e.insert(0, str(self.n8))

        self.vendor_phone_e.delete(0, END)
        self.vendor_phone_e.insert(0, str(self.n9))

        self.totalcp_e.delete(0, END)
        self.totalcp_e.insert(0, str(self.n7))

        self.totalsp_e.delete(0, END)
        self.totalsp_e.insert(0, str(self.n8))

    # função para a atualização dos dados
    def update(self, *args, **kwargs):
        self.u1 = self.name_e.get()
        self.u2 = self.stock_e.get()
        self.u3 = self.cp_e.get()
        self.u4 = self.sp_e.get()
        self.u5 = self.totalcp_e.get()
        self.u6 = self.totalsp_e.get()
        self.u7 = self.vendor_e.get()
        self.u8 = self.vendor_phone_e.get()

        # cria a query com os dados a serem atualizados
        query = "UPDATE inventory SET name=?, stock=?, cp=?, sp=?, totalcp=?, totalsp=?, vendor=?, vendor_phoneno=? WHERE id=?"
        # executa a query e atualiza os dados no banco de dados
        c.execute(query, (self.u1, self.u2, self.u3, self.u4, self.u5, self.u6, self.u7, self.u8, self.id_leb.get()))
        conn.commit()
        tkinter.messagebox.showinfo('rafasaid@gmail.com', 'Cadastro atualizado com sucesso!')




root = Tk()
b = Database(root)
root.geometry('1366x768+0+0')
root.title('FORMULÁRIO DE ATUALIZAÇÃO DE PRODUTOS')
root.configure(background='darkseagreen')
root.mainloop()
