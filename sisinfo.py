from tkinter import *

root = Tk()
tbox = Text(root, width=50, height=10, bg='powderblue')
tbox.place(x=15, y=5)
tbox.insert(END, ''' ESTE SISTEMA FOI CRIADO POR RAFASAID@GMAIL.COM ''')

root.geometry('500x200+0+0')
root.title('Formulário sobre o sistema')
root.config(background='lightpink')
root.mainloop()
