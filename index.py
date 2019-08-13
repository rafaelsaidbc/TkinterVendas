from tkinter import *
import tkinter.messagebox as ttMessageBox
import sqlite3
import tkinter.ttk as ttk
from subprocess import call

root = Tk()
root.title('Supermercado Rafa Said')
width = 1000
height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)

root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)
root.configure(bg='lightsteelblue3')


def LoginForm():
    global lbl_result
    TopLoginForm = Frame(loginform, width=50, height=50, bd=1, relief=SOLID)
    TopLoginForm.pack(side=TOP, pady=2)

    lbl_text = Label(TopLoginForm, text='Seja bemivindo', bg='green', fg='yellow', font=('arial, 10, "bold"'),
                     width=100)
    lbl_text.pack(fill=x)

    MidLoginForm = Frame(loginform, width=600, bg='green')
    MidLoginForm.pack(side=TOP, pady=50)
    # ========== LABELS MidForm ==========
    lbl_username = Label(MidLoginForm, text='Usuário: ', bg='green', fg='blue', font=('arial, 15, "bold"'), bd=18)
    lbl_username.grid(row=0)

    lbl_password = Label(MidLoginForm, text='Senha: ', bg='green', fg='blue', font=('arial, 15, "bold"'), bd=18)
    lbl_password.grid(row=1)

    lbl_result = Label(MidLoginForm, text='', fg='blue', font=('arial, 18'))
    lbl_result.grid(row=3, columnspan=2)

    username = Entry(MidLoginForm, font=('arial, 14'), width=25)
    username.grid(row=0, column=1)

    password = Entry(MidLoginForm, font=('arial, 14'), width=25)
    password.grid(row=1, column=1)

    # ========== BOTÃO ==========
    btn_login = Button(MidLoginForm, text='login', font=('arial, 18'), width=30)
    btn_login.grid(row=2, columnspan=2, pady=20)
    btn_login.bind('return', Login)


if __name__ == '__main__':
    root.mainloop()
