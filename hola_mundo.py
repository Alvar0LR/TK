import tkinter as tk
from tkinter import ttk

#creamos un obj usando la clase TK
ventana = tk.Tk()
#modificamos el tamaño de la ventana
ventana.geometry("600x400")


#le añadimos componentes a la ventana
ventana.title("Ventana 1")
ventana.iconbitmap("virus.ico")

# evento del boton
def evento_click():
    boton1.config(text="Boton presionado")
    print("Evento clicked")
    boton2 = ttk.Button(ventana, text="Boton 2")
    boton2.pack()

#Boton
boton1 = ttk.Button(ventana, text="Clicame", command=evento_click)
boton1.pack(side="top")

#Iniciamos la ventana, si la ejecutamos antes no se muestran los cambios anteriores
ventana.mainloop()




