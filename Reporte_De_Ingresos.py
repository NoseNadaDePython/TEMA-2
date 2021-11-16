
"""""
Crear un reporte llamado "Reporte de Ingresos", el cual deberá contener
los costos que se han cobrado por los Servicios que se han realizado.
Donde deberás tener en cuenta que el Ingreso Neto es igual al
Costo - Porcentaje de descuento. Este informe deberá mostrarse así:
+ ------------------------------------------------- --------------------- ----------+
|                           Titulo del Reporte                            |
+ ---- + --------- + ---------- + -------- + -------------- ------ + -------------- +
| NP | Nombre  |          | Costo  | Descuento Neto                  | Ingreso Neto |
|    | del     | Servicio | (en    | Aplicado (Cantidad              | (Cantidad en |
|    | Cliente |          | pesos) | en Pesos)                       |       Pesos) |
+ ---- + --------- + ---------- + -------- + -------------- ------ + -------------- +
"""""
import csv 
import pandas as pd
from dataclasses import dataclass
from dataclasses import dataclass, field, asdict
from tkinter import Frame, Tk, Label, Entry, Button


@dataclass
class Reporte:
    NP:str=field(default="")
    cliente: str = field(default="")
    servicio: str = field(default="")
    precio: float = field(default=0.0)
    descuento: float = field(default=0.0)
    total: float = field(default=0.0)
    
    def calcular_total(self):
        self.total = self.precio - self.descuento

    def generar(self):
        return asdict(self)


class App(Frame):
    
    def __init__(self):
        self.root = Tk()

    def setup(self):
        self.root.title("Reporte de ingresos")
        self.root.geometry("250x260")
        self.data = []

    def widgets(self):
        for i, label in enumerate(
            ("NP", "Nombre del Cliente", "Servicio", "Precio", "Descuento Neto\nAplicado")):
            Label(self.root, text=label).grid(row=i, column=0, sticky="e")
        self.txt_NP=Entry(self.root)
        self.txt_Cliente = Entry(self.root)
        self.txt_servicio = Entry(self.root)
        self.txt_precio = Entry(self.root)
        self.txt_descuento = Entry(self.root)
        self.btn_guardar = Button(self.root, text="Guardar")
        self.btn_salir = Button(self.root, text="Generar y Salir")

    def layout(self):
        self.txt_NP.grid(row=0, column=1, padx=5, pady=5)
        self.txt_Cliente.grid(row=1, column=1, padx=5, pady=5)
        self.txt_servicio.grid(row=2, column=1, padx=5, pady=5)
        self.txt_precio.grid(row=3, column=1, padx=5, pady=5)
        self.txt_descuento.grid(row=4, column=1, padx=5, pady=5)
        self.btn_guardar.grid(row=5, column=1, padx=5, pady=5, sticky="we")
        self.btn_salir.grid(row=6, column=1, padx=5, pady=5, sticky="we")

    def generar_reporte(self, event):
        reporte1 = Reporte()
        reporte1.NP=self.txt_NP.get()
        reporte1.cliente = self.txt_Cliente.get()
        reporte1.servicio = self.txt_servicio.get()
        reporte1.precio = float(self.txt_precio.get())
        reporte1.descuento = float(self.txt_descuento.get())
        reporte1.calcular_total()
        self.data.append(reporte1.generar())
        self._clear_entries()

    def salir(self, event):
        self._export_to_excel()
        self.root.destroy()

    def _clear_entries(self):
        self.txt_NP.delete(0,"end")
        self.txt_Cliente.delete(0,"end")
        self.txt_servicio.delete(0, "end")
        self.txt_precio.delete(0, "end")
        self.txt_descuento.delete(0, "end")

    def _export_to_excel(self):
        df = pd.DataFrame(self.data)
        df.to_excel("Reporte.xlsx")

    def run(self):
        self.setup()
        self.widgets()
        self.layout()
        self.btn_guardar.bind("<Button-1>", self.generar_reporte)
        self.btn_salir.bind("<Button-1>", self.salir)
        self.root.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()