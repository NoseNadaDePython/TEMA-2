from tkinter import *

def SelectGenero():
    if genero.get()==1:
         monitor1.config(text="Suspenso")
    elif genero.get()==2:
         monitor1.config(text="Técnico")
    elif genero.get()==3:
         monitor1.config(text="Narrativa")
    elif genero.get()==4:
         monitor1.config(text="Fantasía")
    elif genero.get()==5:
         monitor1.config(text="Poesía")
    elif genero.get()==6:
         monitor1.config(text="Ciencia Ficción")
     
def SelectFormato():
    if formato.get() == 1:
         monitor2.config(text="Físico")
    elif formato.get() == 2:
         monitor2.config(text="Digital")
     
def SelectBestSeller():
    if bseller.get():
         monitor3.config(text="Si")
    else:
         monitor3.config(text="No")
     
def agregar():
    SelectGenero()
    SelectFormato()
    SelectBestSeller()
    monitor4.config(text="{}".format(entry1.get()))
    monitor5.config(text="{}".format(entry2.get()))
    monitor6.config(text="{}".format(entry3.get()))
    

#Iniciando ventana raiz
root = Tk()

#Personalizacion de la vetana
root.geometry("600x400")
root.title("Biblioteca Virtual")
root.iconbitmap('imagen1.ico')

genero = IntVar()
formato = IntVar()
bseller = IntVar()

#Creando widgets
label1=Label(root, text ="Nombre del Libro:")
label1.grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry1 = Entry(root)
entry1.grid(row=0, column=1, padx=5, pady=5)
entry1.config(justify="left")

label2=Label(root, text ="Autor 1:")
label2.grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry2 = Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)
entry2.config(justify="left")

label3=Label(root, text ="Autor 2:")
label3.grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry3 = Entry(root)
entry3.grid(row=2, column=1, padx=5, pady=5)
entry3.config(justify="left")

label4=Label(root, text ="ISBN:")
label4.grid(row=3, column=0, sticky="e", padx=5, pady=5)
entry4 = Entry(root)
entry4.grid(row=3, column=1, padx=5, pady=5)
entry4.config(justify="left")

label5=Label(root, text ="Precio:")
label5.grid(row=7, column=0, sticky="e", padx=5, pady=5)
entry5 = Entry(root)
entry5.grid(row=7, column=1, padx=5, pady=5)
entry5.config(justify="left")

label6=Label(root, text ="Genero:")
label6.grid(row=8, column=0, sticky="e", padx=5, pady=5)
#Opciones de Genero
op1 = Radiobutton(root,text="Suspenso", variable=genero, value=1)
op1.grid(row=8, column=1, padx=5, pady=5)
op2 = Radiobutton(root,text="Técnico", variable=genero, value=2)
op2.grid(row=8, column=2, padx=5, pady=5)
op3 = Radiobutton(root,text="Narrativa", variable=genero, value=3)
op3.grid(row=8, column=3, padx=5, pady=5)
op4 = Radiobutton(root,text="Fantasía", variable=genero, value=4)
op4.grid(row=9, column=1, padx=5, pady=5)
op5 = Radiobutton(root,text="Poesía", variable=genero, value=5)
op5.grid(row=9, column=2, padx=5, pady=5)
op6 = Radiobutton(root,text="Ciencia Ficción", variable=genero, value=6)
op6.grid(row=9, column=3, padx=5, pady=5)


label7=Label(root, text ="Formato:")
label7.grid(row=10, column=0, sticky="e", padx=5, pady=5)
#Opciones de Formato
f1 = Radiobutton(root,text="Físico", variable=formato, value=1)
f1.grid(row=10, column=1, padx=5, pady=5)
f2 = Radiobutton(root,text="Digital", variable=formato, value=2)
f2.grid(row=10, column=2, padx=5, pady=5)


label8=Label(root, text ="Best Seller:")
label8.grid(row=11, column=0, sticky="e", padx=5, pady=5)
#Opciones de BestSeller
bs1 = Radiobutton(root,text="Si", variable=bseller, value=1)
bs1.grid(row=11, column=1, padx=5, pady=5)
bs2 = Radiobutton(root,text="No", variable=bseller, value=2)
bs2.grid(row=11, column=2, padx=5, pady=5)

#Boton
boton1=Button(root, text="Agregar", command=agregar, bd=3)
boton1.grid(row=13, column=2, padx=5, pady=5)

#Etiquetas monitoras
monitor1 = Label(root)
monitor1.grid(row=0, column=4, sticky="e", padx=5, pady=5)

monitor2 = Label(root)
monitor2.grid(row=1, column=4, sticky="e", padx=5, pady=5)

monitor3 = Label(root)
monitor3.grid(row=2, column=4, sticky="e", padx=5, pady=5)

monitor4 = Label(root)
monitor4.grid(row=0, column=3, sticky="e", padx=5, pady=5)
monitor5 = Label(root)
monitor5.grid(row=1, column=3, sticky="e", padx=5, pady=5)
monitor6 = Label(root)
monitor6.grid(row=2, column=3, sticky="e", padx=5, pady=5)


#Ciclo final de la app
root.mainloop()