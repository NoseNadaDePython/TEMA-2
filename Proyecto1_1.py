
#Importación de modulos y librerías
from tkinter import *
from tkinter import messagebox as MessageBox #importamos para crear un popup



#Iniciando ventana raiz
root = Tk()
root.title(       "R E P O R T E  D E I N G R E S O S")
root.geometry("600x400")


root.iconbitmap('imagen1.ico')

#Declarando Variables
genero, formato, bseller = IntVar(), IntVar(), IntVar()
e1,e2,e3,e4,e5 = StringVar(), StringVar(), StringVar(), StringVar(),StringVar()

#Creando widgets
label1=Label(root, text ="Proveedor:")
label1.grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry1 = Entry(root,textvariable=e1)
entry1.grid(row=0, column=1, padx=5, pady=5)
entry1.config(justify="right")

label2=Label(root, text ="Cliente:")
label2.grid(row = 1, column = 0, sticky = "e", padx = 5, pady = 5)
entry2 = Entry(root,textvariable = e2)
entry2.grid(row=1, column=1, padx=5, pady=5)
entry2.config(justify="left")

label3=Label(root, text ="Servicio:")
label3.grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry3 = Entry(root, textvariable = e3)
entry3.grid(row=2, column=1, padx=5, pady=5)
entry3.config(justify="left")

label4=Label(root, text ="Costos:")
label4.grid(row=3, column=0, sticky="e", padx=5, pady=5)
entry4 = Entry(root, textvariable = e4)
entry4.grid(row=3, column=1, padx=5, pady=5)
entry4.config(justify="left")

label5=Label(root, text ="Descuento:")
label5.grid(row=7, column=0, sticky="e", padx=5, pady=5)
entry5 = Entry(root, textvariable=e5)
entry5.grid(row=7, column=1, padx=5, pady=5)
entry5.config(justify="left")

label6=Label(root, text ="Ingreso:")
label6.grid(row=8, column=0, sticky="e", padx=5, pady=5)
entry6 = Entry(root, textvariable=e5)
entry6.grid(row=8, column=1, padx=5, pady=5)
entry6.config(justify="left")


root.mainloop()
