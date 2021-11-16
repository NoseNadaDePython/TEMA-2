
from tkinter import *
import tkinter as tk

root = Tk()
txt = Text(root)
txt.pack(padx=10, pady=10)
 


sb = Scrollbar(root)
sb.config(command=txt.yview)
sb.pack(side=RIGHT, fill=Y)
 
txt.config(yscrollcommand=sb.set)
txt.insert('1.0', 'Texto Insertado')
txt.get('1.0', END+'-1c')
root.mainloop()