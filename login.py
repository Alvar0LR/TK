import tkinter as tk
from tkinter import ttk, Message, messagebox

# Propiedades de la ventana
ventana = tk.Tk()
ventana.geometry("300x130")
ventana.title("TK")
ventana.iconbitmap("virus.ico")
ventana.resizable(False,False)

# Config del grid
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=3)

#Metodos

usuario_valido = "Juan"
password_valido = 1234


def evento_login():
    usuario1 = usuario_entrada.get().strip()
    password1 = contrasease_entrada.get().strip()
    if usuario1 == usuario_valido and password1 == str(password_valido):
        messagebox.showinfo("Datos Login", f"Usuario: {usuario_entrada.get()} Constraseña: {contrasease_entrada.get()}\n")
    else:
        messagebox.showerror("Datos Login", "Acceso denegado")

# Usuario
usuario = ttk.Label(ventana, text="Usuario: ")
usuario.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
usuario_entrada = ttk.Entry(ventana)
usuario_entrada.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
# Contraseña
contrasea = ttk.Label(ventana, text="Password: ")
contrasea.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
contrasease_entrada = ttk.Entry(ventana, show="*")
contrasease_entrada.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
# Boton
boton = ttk.Button(ventana, text="Iniciar Sesion", command=evento_login)
boton.grid(row=2, column=1, sticky=tk.W, padx=15, pady=15)

# Ejecutar la ventana
ventana.mainloop()