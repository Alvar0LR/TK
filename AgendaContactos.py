#Interfaz root
import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

def conectar_db():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="agenda_contactos",
        port=3306
    )


def cargar_datos():
    for row in tree.get_children():
        tree.delete(row)
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clientes ORDER BY id")
        items = cursor.fetchall()
    for row in items:
        tree.insert("", tk.END, values=row)
    conn.close()



def guardar_clientes():
    nombre = entry_nombre.get().strip()
    apellido = entry_apellido.get().strip()
    correo = entry_correo.get().strip()


def eliminar_clientes():
    pass


def limpiar_campos():
    entry_id.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_correo.delete(0, tk.END)

def seleccionar_file(event):
    item = tree.focus()
    valores = tree.item(item, "values")
    if valores:
        entry_id.delete(0, tk.END)
        entry_id.insert(0, valores[0])
        entry_nombre.delete(0, tk.END)
        entry_nombre.insert(0, valores[1])
        entry_apellido.delete(0, tk.END)
        entry_apellido.insert(0, valores[2])
        entry_correo.delete(0, tk.END)
        entry_correo.insert(0, valores[3])

#UI
root = tk.Tk()
root.geometry("900x500")
root.title("Agenda De Contactos")

#Frame_top
frame_top = tk.Frame(root)
frame_top.pack(side="top")

#Buscador
entry_buscador = tk.Entry(frame_top, width=50)
entry_buscador.pack(side=tk.LEFT, padx=5)

#Botones
tk.Button(text="Buscar", command=guardar_clientes).pack(side=tk.LEFT)
tk.Button(text="Guardar", command=guardar_clientes).pack(side=tk.LEFT)
tk.Button(text="Eliminar", command=eliminar_clientes).pack(side=tk.LEFT)


#id
entry_id = tk.Entry(root)
entry_id.pack_forget()

# Campos
tk.Label(root, text="Nombre").pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack()

tk.Label(root, text="Apellido").pack()
entry_apellido = tk.Entry(root)
entry_apellido.pack()

tk.Label(root, text="Correo").pack()
entry_correo = tk.Entry(root)
entry_correo.pack()

# Tabla
tree = ttk.Treeview(root, columns=("ID", "Nombre", "Apellido", "Membresía"), show="headings")
for col in tree["columns"]:
     tree.heading(col, text=col)
tree.pack()
tree.bind("<<TreeviewSelect>>", seleccionar_file)

# Cargar datos
cargar_datos()

#Ejecutar app
root.mainloop()
