
"""""
                              SPA PIEL ORIGINAL
                              
3.Crear un reporte llamado "Reporte de Ingresos", el cual deberá contener
los costos que se han cobrado por los Servicios que se han realizado.
Donde deberás tener en cuenta que el Ingreso Neto es igual al
Costo - Porcentaje de descuento. Este informe deberá mostrarse así:
+ ------------------------------------------------- --------------------------------+
|                                    Titulo del Reporte                             |
+ ---- + --------- + ---------- + -------- + -------------- ------ + -------------- +
| NP | Nombre  |          | Costo  | Descuento Neto                  | Ingreso Neto |
|    | del     | Servicio | (en    | Aplicado (Cantidad              | (Cantidad en |
|    | Cliente |          | pesos) | en Pesos)                       |       Pesos) |
+ ---- + --------- + ---------- + -------- + -------------- ------ + -------------- +
"""""

#Importando la librerias
from tkinter import *
from tkinter import ttk,messagebox
import tkinter as tk

"""""
NP:str=field(default="")
cliente: str = field(default="")
servicio: str = field(default="")
precio: float = field(default=0.0)
descuento: float = field(default=0.0)
total: float = field(default=0.0)

def calcular():
      total = precio -descuento
"""""

#Funcion para cerrar la ventana a traves del button "Salir" 
def on_closing():
    if messagebox.askokcancel("Salir "," ¿Quieres salir?"):
        root1.destroy()

#Funcion para mostrar opciones de cerrado si se cierra la ventana desde la X    
class MyDialog:
    def __init__(self, parent):
        self.top = tk.Toplevel(parent)#creando una ventana secundaria
        self.parent = parent
        self.top.title("Salir")
        self.top.resizable(0,0)
        self.top.config(bg="cyan")

#Etiquetas
        l=Label(self.top, text="¿Está seguro?")
        l.config(bg="cyan",font=("arial black",9))
        l.grid(row=0, column=0, columnspan=2)
        
#Botones de opciones
        self.button1 = tk.Button(self.top, text="Si, salir .", command=self.salir)
        self.button2 = tk.Button(self.top, text="No, solo minimizar.", command=self.minimizar)
        self.button1.grid(row=1, column=0, padx=5, pady=5)
        self.button1.config(activebackground="red",bd=3)
        self.button2.grid(row=1, column=1, padx=5, pady=5)
#funcion para cerrar la ventana
    def salir(self):
        self.top.destroy()
        self.parent.destroy()
#funcion para minimizar la ventana
    def minimizar(self):
        self.top.destroy()
        self.parent.iconify()

class MyApp:
    def __init__(self, parent):
        self.parent = parent
        self.parent.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        d = MyDialog(root1)
        self.parent.wait_window(d.top)


#Iniciando ventana raiz

root1 = Tk()
#Personalizacion de la ventana Tk
root1.geometry("880x230")
root1.iconbitmap("SPA_1.ico") 
root1.title("                                                                                                                                              REPORTE DE INGRESOS         ")
#creando un scroll
scrollbar=Scrollbar(root1)
c=Canvas(root1, bg="NavajoWhite3", yscrollcommand=scrollbar.set)
scrollbar.config(command=c.yview)
scrollbar.pack(side=RIGHT,fill=Y)

root=Frame(c)
c.pack(side="left", fill="both", expand=True)
c.create_window(0,0,window=root,anchor="nw")

root.config(bg="NavajoWhite3")
root.config(cursor="cross")
label=Label(root,text="REPORTE DE INGRESOS ")
label.config(bg="NavajoWhite3",foreground="black",font=("Comic Sans MS",18))
label.grid(row=0,columnspan=10,sticky="n")
imagen=PhotoImage(file="SPA_2.png")
imagen=imagen.subsample(6)
Label(root, image=imagen, bd=0).grid(row=0,column=0, sticky="nw")
"""""
Tipo de cursores
"arrow","circle","clock","cross", 
"dotbox","exchange","fleur", 
"heart","man","mouse","pirate",
"plus","shuttle","sizing","spider", 
"spraycan","star", "target", 
"tcross","trek"
"""""
#Creando Entradas y Etiquetas
label7=Label(root, text ="NP")
label7.config(background="NavajoWhite3",foreground="black",font=("arial black",10))
label7.grid(row=5, column=0, sticky="w", padx=50, pady=0)

entry7 = Entry(root)
entry7.config(insertbackground="red",bd="3",highlightcolor="green")
entry7.grid(row=6,column=0,padx=10,pady=10,ipady=2)
entry7.config(justify="left")

label8=Label(root, text ="Nombre del \nCliente")
label8.config(background="NavajoWhite3",foreground="black",font=("arial black",10))
label8.grid(row=5, column=1, sticky="w", padx=25, pady=5)

entry8 = Entry(root)
entry8.config(insertbackground="blue",bd="3",highlightcolor="green")
entry8.grid(row=6, column=1, padx=5, pady=5,ipady=2)
entry8.config(justify="left")

label9=Label(root, text ="Servicio")
label9.config(background="NavajoWhite3",foreground="black",font=("arial black",10))
label9.grid(row=5, column=2, sticky="w", padx=35, pady=5)

entry9 = Entry(root)
entry9.config(insertbackground="blue",bd="3",highlightcolor="green")
entry9.grid(row=6, column=2, padx=5, pady=5,ipady=2)
entry9.config(justify="left")

label10=Label(root, text ="Costo")
label10.config(background="NavajoWhite3",foreground="black",font=("arial black",10))
label10.grid(row=5, column=3, sticky="w", padx=40, pady=5)

entry10 = Entry(root)
entry10.config(insertbackground="blue",bd="3",highlightcolor="green")
entry10.grid(row=6, column=3, padx=5, pady=5,ipady=2)
entry10.config(justify="left")


label11=Label(root, text ="Descuento")
label11.config(background="NavajoWhite3",foreground="black",font=("arial black",10))
label11.grid(row=5, column=4, sticky="w", padx=30, pady=5)

entry11 = Entry(root)
entry11.config(insertbackground="blue",bd="3",highlightcolor="green")
entry11.grid(row=6, column=4, padx=4, pady=5,ipady=2)
entry11.config(justify="left")

label13=Label(root, text ="Ingreso Neto")
label13.config(background="NavajoWhite3",foreground="black",font=("arial black",10))
label13.grid(row=5, column=6, sticky="w", padx=15, pady=5)

entry13 = Entry(root)
entry13.config(insertbackground="red",bd="3",highlightcolor="green")
entry13.grid(row=6, column=6, padx=5, pady=5,ipady=2)
entry13.config(justify="left")

#Etiquetas monitoras
#Para entry 1#
monitor01 = Label(root,text ="1")
monitor01.grid(row=7, column=0,  padx=50, pady=5)
monitor02 = Label(root,text ="M")
monitor02.grid(row=8, column=0,  padx=50, pady=5)
monitor03 = Label(root,text ="H")
monitor03.grid(row=9, column=0,  padx=50, pady=5)
monitor04 = Label(root,text ="Juan G")
monitor04.grid(row=10, column=0, padx=50, pady=5)
monitor2 = Label(root)
monitor2.grid(row=11, column=0, padx=50, pady=5)
monitor3 = Label(root)
monitor3.grid(row=12, column=0,  padx=50, pady=5)
monitor4 = Label(root)
monitor4.grid(row=13, column=0,  padx=50, pady=5)

#Para entry 2#
monitor51 = Label(root,text="A")
monitor51.grid(row=7, column=1,  padx=5, pady=5)
monitor52 = Label(root,text="B")
monitor52.grid(row=8, column=1, padx=5, pady=5)
monitor53 = Label(root,text="C")
monitor53.grid(row=9, column=1, padx=5, pady=5)
monitor54 = Label(root,text="B")
monitor54.grid(row=10, column=1, padx=5, pady=5)
monitor5 = Label(root)
monitor5.grid(row=11, column=1, padx=5, pady=5)
monitor6 = Label(root)
monitor6.grid(row=12, column=1, padx=5, pady=5)
monitor7 = Label(root)
monitor7.grid(row=13, column=1, padx=5, pady=5)
#para entry 3
monitor61 = Label(root,text="A")
monitor61.grid(row=7, column=2,  padx=5, pady=5)
monitor62 = Label(root,text="B")
monitor62.grid(row=8, column=2,  padx=5, pady=5)
monitor63 = Label(root,text="C")
monitor63.grid(row=9, column=2,  padx=5, pady=5)
monitor64 = Label(root,text="D")
monitor64.grid(row=10, column=2,  padx=5, pady=5)
monitor71 = Label(root)
monitor71.grid(row=11, column=2,  padx=5, pady=5)
monitor72 = Label(root)
monitor72.grid(row=12, column=2,  padx=5, pady=5)
monitor73 = Label(root)
monitor73.grid(row=13, column=2,  padx=5, pady=5)
#para entry 4
monitor81 = Label(root,text="A")
monitor81.grid(row=7, column=3, padx=5, pady=5)
monitor82 = Label(root,text="B")
monitor82.grid(row=8, column=3,  padx=5, pady=5)
monitor83 = Label(root,text="C")
monitor83.grid(row=9, column=3,  padx=5, pady=5)
monitor84 = Label(root,text="D")
monitor84.grid(row=10, column=3, padx=5, pady=5)
monitor91 = Label(root)
monitor91.grid(row=11, column=3,  padx=5, pady=5)
monitor92 = Label(root)
monitor92.grid(row=12, column=3,  padx=5, pady=5)
monitor93 = Label(root)
monitor93.grid(row=13, column=3,  padx=5, pady=5)
#para entry 5
monitor12 = Label(root,text="A")
monitor12.grid(row=7, column=4, padx=5, pady=5)
monitor22 = Label(root,text="B")
monitor22.grid(row=8, column=4,padx=5, pady=5)
monitor32 = Label(root,text="C")
monitor32.grid(row=9, column=4,  padx=5, pady=5)
monitor42 = Label(root)
monitor42.grid(row=10, column=4, padx=5, pady=5)
monitor13 = Label(root)
monitor13.grid(row=11, column=4,  padx=5, pady=5)
monitor23 = Label(root)
monitor23.grid(row=12, column=4,  padx=5, pady=5)
monitor33 = Label(root)
monitor33.grid(row=13, column=4, padx=5, pady=5)

#para entry 6
monitorb = Label(root,text="A")
monitorb.grid(row=7, column=6, padx=5, pady=5)
monitorb = Label(root,text="B")
monitorb.grid(row=8, column=6,padx=5, pady=5)
monitorb = Label(root,text="C")
monitorb.grid(row=9, column=6,  padx=5, pady=5)
monitorb = Label(root)
monitorb.grid(row=10, column=6, padx=5, pady=5)
monitorb = Label(root)
monitorb.grid(row=11, column=6,  padx=5, pady=5)
monitorb = Label(root)
monitorb.grid(row=12, column=6,  padx=5, pady=5)
monitorb = Label(root)
monitorb.grid(row=13, column=6, padx=5, pady=5)

#Creando boton para guardar los datos (Inhabilitado)
btt=Button(root,text="Guardar datos")
btt.config(activebackground="yellow")
btt.grid(row=14,columnspan=6)
#Crendo boton para cerra laventana
btt1=Button(root,text="Salir")
btt1.config(activebackground="red",command=on_closing)
btt1.grid(row=14,columnspan=9,pady=40)

root1.update()
c.config(scrollregion=c.bbox("all"))


if __name__ == "__main__":
   
    app = MyApp(root1)
#creando ciclo final 
root.mainloop()

