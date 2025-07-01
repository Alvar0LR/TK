import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# Conexión a la base de datos
def conectar_db():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="clientes_db",
        port=3307
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
    membresia = entry_membresia.get().strip()
    idi = entry_id.get().strip()

    valores = (nombre, apellido, membresia)
    valores2 = (nombre, apellido, membresia, idi)

    if not nombre or not apellido or not membresia:
        messagebox.showwarning("Campos Incompeltos", "Complete los campos vacios")
        return

    conn = conectar_db()
    cursor = conn.cursor()

    if idi == "":
        cursor.execute("INSERT INTO clientes (nombre, apellido, membresia) VALUES (%s, %s, %s)", valores)
    else:
        cursor.execute("UPDATE clientes SET nombre=%s, apellido=%s ,membresia=%s WHERE id=%s", valores2)

    conn.commit()
    conn.close()
    limpiar_campos()
    cargar_datos()

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
        entry_membresia.delete(0, tk.END)
        entry_membresia.insert(0, valores[3])

def eliminar_cliente():
    if entry_id.get == "":
        messagebox.showwarning("Campos Incompeltos", "No se encontrado")
        return
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE id=%s", (entry_id.get(),))
    conn.commit()
    conn.close()
    limpiar_campos()
    cargar_datos()

def limpiar_campos():
    entry_id.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_membresia.delete(0, tk.END)

# Interfaz
root = tk.Tk()
root.geometry("900x500")
root.title("CRUD de Clientes")

# ID oculto
entry_id = tk.Entry(root)
entry_id.pack_forget()


# Campos
tk.Label(root, text="Nombre").pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack()

tk.Label(root, text="Apellido").pack()
entry_apellido = tk.Entry(root)
entry_apellido.pack()

tk.Label(root, text="Membresía").pack()
entry_membresia = tk.Entry(root)
entry_membresia.pack()

# Botones
tk.Button(root, text="Guardar", command=guardar_clientes).pack(pady=5)
tk.Button(root, text="Eliminar", command=eliminar_cliente).pack()

# Tabla
tree = ttk.Treeview(root, columns=("ID", "Nombre", "Apellido", "Membresía"), show="headings")
for col in tree["columns"]:
     tree.heading(col, text=col)
tree.pack()
tree.bind("<<TreeviewSelect>>", seleccionar_file)

# Cargar datos
cargar_datos()

root.mainloop()
