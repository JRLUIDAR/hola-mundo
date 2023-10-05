from tkinter import *

saludar="Hola Mundo, desde Python !"

raiz=Tk()
raiz.title('Hola Mundo')
raiz.resizable(0,0)
raiz.geometry('500x400')

Label(raiz, text=saludar,fg='red', ).grid(row=0, column=0 ,padx=200, pady=200, )

raiz.mainloop()