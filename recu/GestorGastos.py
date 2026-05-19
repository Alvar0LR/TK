import tkinter as tk
from tkinter import ttk, messagebox
import psycopg2
import re
from tkcalendar import DateEntry
from datetime import datetime
import os

ventana = tk.Tk()
ventana.title("Registro de Gastos Personales")
ventana.geometry("800x500")

frame_actual = None
id_editando = None
usuario_actual = None
gastos = []


REGEX_IMPORTE = re.compile(r"^\d+([.,]\d{1,2})?$")
REGEX_FECHA   = re.compile(r"^(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/\d{4}$")

class ErrorValidacion(Exception):
    pass

class ErrorBaseDatos(Exception):
    pass

## Conexion con postgressql
DB = {
    "host": "localhost",
    "port": 5432,
    "dbname": "gastos_db",
    "user": "postgres",
    "password": "nutrimed123"
}

def conectar():
    return psycopg2.connect(**DB)

def inicializar_bd():
    conn = conectar()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS gastos (
            id          SERIAL PRIMARY KEY,
            descripcion VARCHAR(200),
            importe     NUMERIC(10,2),
            categoria   VARCHAR(50),
            fecha       DATE
        )
    """)

    cur.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id       SERIAL PRIMARY KEY,
                usuario  VARCHAR(20) UNIQUE NOT NULL,
                password VARCHAR(100) NOT NULL
            )
        """)

    conn.commit()
    cur.close()
    conn.close()


def limpiar():
    global frame_actual
    if frame_actual:
        frame_actual.destroy()

def pantalla_inicio():
    global frame_actual
    limpiar()
    frame_actual = tk.Frame(ventana, bg="#f0f4f8")
    frame_actual.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    tk.Label(frame_actual, text="Registro de Gastos", font=("Helvetica", 22, "bold")).pack(anchor="w")
    tk.Label(frame_actual, text="Selecciona una opcion del menu para empezar", font=("Helvetica", 11)).pack(anchor="w", pady=(4,20))

    tk.Button(frame_actual, text="Nuevo gasto", command=pantalla_crear, width=18, pady=6, bg="#4a9e6b",fg="white").pack(anchor="w", pady=3)
    tk.Button(frame_actual, text="Ver gastos", command=pantalla_lista, width=18, pady=6, bg="#5b8dd9", fg="white").pack(anchor="w", pady=3)
    tk.Button(frame_actual, text="Exportar a CSV", command=pantalla_csv, width=18, pady=6, bg="#f0a500", fg="white").pack(anchor="w", pady=3)


def pantalla_crear():
    global frame_actual
    limpiar()
    frame_actual = tk.Frame(ventana, bg="#f0f4f8")
    frame_actual.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    tk.Label(frame_actual, text="Nuevo gasto", font=("Helvetica", 14, "bold")).pack(anchor="w")

    tk.Label(frame_actual, text="Descripcion:").pack(anchor="w", pady=(12, 0))
    entry_desc = tk.Entry(frame_actual, width=35)
    entry_desc.pack(anchor="w")

    tk.Label(frame_actual, text="Importe (€):").pack(anchor="w", pady=(8, 0))
    entry_imp = tk.Entry(frame_actual, width=15)
    entry_imp.pack(anchor="w")

    tk.Label(frame_actual, text="Fecha:").pack(anchor="w", pady=(8, 0))
    cal = DateEntry(frame_actual, width=15, date_pattern="dd/MM/yyyy")
    cal.pack(anchor="w")

    tk.Label(frame_actual, text="Categoria:").pack(anchor="w", pady=(8, 0))
    combo_cat = ttk.Combobox(frame_actual, width=20, state="readonly",
                             values=["Alimentacion", "Transporte", "Ocio", "Salud", "Hogar", "Otros"])
    combo_cat.current(0)
    combo_cat.pack(anchor="w")

    lbl_msg = tk.Label(frame_actual, text="")

    def guardar():
        desc = entry_desc.get().strip()
        imp = entry_imp.get().replace(",", ".").strip()
        fecha_raw = cal.get()  # DD/MM/YYYY para el regex
        cat = combo_cat.get()
        try:
            if not desc or not imp or not fecha_raw:
                raise ErrorValidacion("Rellena todos los campos")
            if not REGEX_IMPORTE.match(imp):
                raise ErrorValidacion("Importe no valido. Ejemplo: 12 o 12.50")
            if not REGEX_FECHA.match(fecha_raw):
                raise ErrorValidacion("Fecha no valida. Formato: DD/MM/AAAA")

            fecha = datetime.strptime(fecha_raw, "%d/%m/%Y").strftime("%Y-%m-%d")  # conversión aquí
            conn = conectar()
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO gastos (descripcion, importe, categoria, fecha) VALUES (%s, %s, %s, %s)",
                (desc, float(imp), cat, fecha)
            )
            conn.commit()
            cur.close()
            conn.close()
            lbl_msg.config(text=f'Gasto "{desc}" guardado correctamente', fg="green")

        except ErrorValidacion as e:
            lbl_msg.config(text=str(e), fg="red")
        except Exception as e:
            raise ErrorBaseDatos(f"Error en la base de datos: {e}")

    tk.Button(frame_actual, text="Guardar", command=guardar, width=12, pady=4, bg="#5b8dd9", fg="white").pack(anchor="w", pady=(14, 4))
    tk.Button(frame_actual, text="Volver", command=pantalla_inicio, width=12, pady=4, bg="#d0d7de").pack(anchor="w")
    lbl_msg.pack(anchor="w", pady=(8, 0))

def pantalla_lista():
    global frame_actual
    limpiar()
    frame_actual = tk.Frame(ventana, bg="#f0f4f8")
    frame_actual.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    tk.Label(frame_actual, text="Ver gastos", font=("Helvetica", 14, "bold")).pack(anchor="w")

    tk.Label(frame_actual, text="Buscar:").pack(anchor="w", pady=(8, 0))
    entry_buscar = tk.Entry(frame_actual, width=30)
    entry_buscar.pack(anchor="w")
    tk.Button(frame_actual, text="Buscar", command=lambda: cargar_lista(entry_buscar.get()), width=10).pack(anchor="w", pady=(4, 8))

    cols = ("ID", "Descripcion", "Importe", "Categoria", "Fecha")
    tree = ttk.Treeview(frame_actual, columns=cols, show="headings", height=8)

    tree.heading("ID", text="ID")
    tree.heading("Descripcion", text="Descripcion")
    tree.heading("Importe", text="Importe")
    tree.heading("Categoria", text="Categoria")
    tree.heading("Fecha", text="Fecha")

    tree.column("ID", width=40)
    tree.column("Descripcion", width=200)
    tree.column("Importe", width=80)
    tree.column("Categoria", width=100)
    tree.column("Fecha", width=90)

    tree.pack(anchor="w")

    frame_botones = tk.Frame(frame_actual)
    frame_botones.pack(anchor="w", pady=6)

    def on_selection(event):
        sel = tree.selection()
        if not sel:
            return
        btn_editar.config(state=tk.NORMAL)
        btn_eliminar.config(state=tk.NORMAL)

    def cargar_lista(filtro=""):
        for item in tree.get_children():
            tree.delete(item)
        conn = conectar()
        cur = conn.cursor()
        if filtro:
            cur.execute(
                "SELECT id, descripcion, importe, categoria, fecha FROM gastos WHERE descripcion ILIKE %s ORDER BY fecha DESC",
                (f"%{filtro}%",))
        else:
            cur.execute("SELECT id, descripcion, importe, categoria, fecha FROM gastos ORDER BY fecha DESC")
        datos = cur.fetchall()
        cur.close()
        conn.close()
        for g in datos:
            tree.insert("", tk.END, values=g)
        return datos

    def eliminar():
        sel = tree.selection()
        if not sel:
            return
        vals = tree.item(sel[0], "values")
        id_gasto = vals[0]
        if not messagebox.askyesno("Confirmar", "Seguro que quieres eliminar el gasto?"):
            return
        conn2 = conectar()
        cur2 = conn2.cursor()
        cur2.execute("DELETE FROM gastos WHERE id = %s", (id_gasto,))
        conn2.commit()
        cur2.close()
        conn2.close()
        pantalla_lista()

    def editar():
        global id_editando
        sel = tree.selection()
        if not sel:
            return
        vals = tree.item(sel[0], "values")
        id_editando = vals[0]
        pantalla_editar(vals)

    btn_editar = tk.Button(frame_botones, text="Editar", command=editar, state=tk.DISABLED, width=12, pady=4, bg="#4a9e6b", fg="white")
    btn_eliminar = tk.Button(frame_botones, text="Eliminar", command=eliminar, state=tk.DISABLED, width=12, pady=4, bg="#e57373", fg="white")
    btn_editar.pack(side=tk.LEFT, padx=(0, 6))
    btn_eliminar.pack(side=tk.LEFT)

    tree.bind("<<TreeviewSelect>>", on_selection)

    gastos_f = cargar_lista()

    tk.Button(frame_actual, text="Volver", command=pantalla_inicio, width=12, pady=4).pack(anchor="w", pady=10)

    cols2 = ("Numero", "Total")
    tree_info = ttk.Treeview(frame_actual, columns=cols2, show="headings", height=1)
    tree_info.heading("Numero", text="Numero de gastos")
    tree_info.heading("Total", text="Total")
    tree_info.column("Numero", width=120)
    tree_info.column("Total", width=90)

    total = 0
    for i in gastos_f:
        total += float(i[2])
    tree_info.insert("", tk.END, values=(len(gastos_f), f"{total}€"))
    tree_info.pack(anchor="w")


def pantalla_editar(vals):
    global frame_actual
    limpiar()
    frame_actual = tk.Frame(ventana, bg="#f0f4f8")
    frame_actual.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    tk.Label(frame_actual, text="Editar gasto", font=("Helvetica", 14, "bold")).pack(anchor="w")

    tk.Label(frame_actual, text="Descripcion:").pack(anchor="w", pady=(12, 0))
    entry_desc = tk.Entry(frame_actual, width=35)
    entry_desc.insert(0, vals[1])
    entry_desc.pack(anchor="w")

    tk.Label(frame_actual, text="Importe:").pack(anchor="w", pady=(8, 0))
    entry_imp = tk.Entry(frame_actual, width=15)
    entry_imp.insert(0, vals[2])
    entry_imp.pack(anchor="w")

    tk.Label(frame_actual, text="Categoria:").pack(anchor="w", pady=(8, 0))
    combo_cat = ttk.Combobox(frame_actual, values=["Alimentacion", "Transporte", "Ocio", "Salud", "Hogar", "Otros"],
                             state="readonly", width=20)
    combo_cat.set(vals[3])
    combo_cat.pack(anchor="w")

    tk.Label(frame_actual, text="Fecha:").pack(anchor="w", pady=(8, 0))
    cal = DateEntry(frame_actual, width=15, date_pattern="dd/MM/yyyy")
    fecha_obj = datetime.strptime(vals[4], "%Y-%m-%d")
    cal.set_date(fecha_obj)
    cal.pack(anchor="w")

    lbl_msg = tk.Label(frame_actual, text="")

    def actualizar():
        desc = entry_desc.get().strip()
        imp = entry_imp.get().replace(",", ".").strip()
        cat = combo_cat.get()
        fecha = datetime.strptime(cal.get(), "%d/%m/%Y").strftime("%Y-%m-%d")  # añade esto

        if not desc or not imp:
            lbl_msg.config(text="Rellena todos los campos", fg="red")
            return
        if not REGEX_IMPORTE.match(imp):
            lbl_msg.config(text="Importe invalido (numero entero o decimal)", fg="red")
            return

        con = conectar()
        cur = con.cursor()
        cur.execute(
            "update gastos set descripcion=%s, importe=%s, categoria=%s, fecha=%s WHERE id=%s",
            (desc, float(imp), cat, fecha, id_editando)
        )
        con.commit()
        cur.close()
        con.close()
        pantalla_lista()

    tk.Button(frame_actual, text="Guardar cambios", command=actualizar, width=15, pady=4, bg="#5b8dd9", fg="white").pack(anchor="w",pady=(14,4))
    tk.Button(frame_actual, text="Volver", command=pantalla_lista, width=15, pady=4, bg="#d0d7de").pack(anchor="w")
    lbl_msg.pack(anchor="w", pady=(8, 0))


def pantalla_csv():
    global frame_actual
    limpiar()
    frame_actual = tk.Frame(ventana, bg="#f0f4f8")
    frame_actual.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    tk.Label(frame_actual, text="Exportar gastos a CSV", font=("Helvetica", 14, "bold")).pack(anchor="w")
    tk.Label(frame_actual, text="Se guardara un archivo gastos.csv en la carpeta del proyecto.").pack(anchor="w",pady=(6, 20))

    lbl_msg = tk.Label(frame_actual, text="")

    def exportar():
        try:
            conn = conectar()
            cur = conn.cursor()
            cur.execute(
                "select id, descripcion, importe, categoria, fecha from gastos order by fecha desc"
            )
            t_gastos = cur.fetchall()
            cur.close()
            conn.close()

            numero_gastos = len(t_gastos)

            if not t_gastos:
                messagebox.showwarning("Aviso", "No hay datos que exportar")
                return

            ruta = os.path.join(os.path.expanduser("~"), "Downloads", "gastos.csv")

            with open(ruta, "w", encoding="utf-8") as f:
                f.write("ID,Descripcion,Importe,Categoria,Fecha\n")
                for g in t_gastos:
                    f.write(f"{g[0]},{g[1]},{g[2]},{g[3]},{g[4]}\n")
            lbl_msg.config(text=f"Exportado correctamente a csv [{numero_gastos} gastos guardados]", fg="green")


        except ErrorValidacion as e:
            lbl_msg.config(text=str(e), fg="red")
        except Exception as e:
            lbl_msg.config(text=f"Error: {e}", fg="red")

    tk.Button(frame_actual, text="Exportar CSV", command=exportar, width=15, pady=4, bg="#4a9e6b" ).pack(anchor="w", pady=(0, 6))
    tk.Button(frame_actual, text="Volver", command=pantalla_inicio, width=12, pady=4, bg="#d0d7de").pack(anchor="w")
    lbl_msg.pack(anchor="w", pady=(8, 0))



def pantalla_login():
    global frame_actual
    limpiar()
    frame_actual = tk.Frame(ventana, bg="#f0f4f8")
    frame_actual.pack(fill=tk.BOTH, expand=True, padx=40, pady=40)

    tk.Label(frame_actual, text="Registro de Gastos", font=("Helvetica", 18, "bold")).pack(anchor="w")
    tk.Label(frame_actual, text="Inicia sesion para continuar").pack(anchor="w", pady=(4, 20))

    tk.Label(frame_actual, text="Usuario:").pack(anchor="w")
    entry_user = tk.Entry(frame_actual, width=30)
    entry_user.pack(anchor="w")

    tk.Label(frame_actual, text="Contrasena:").pack(anchor="w", pady=(8, 0))
    entry_pass = tk.Entry(frame_actual, width=30, show="*")
    entry_pass.pack(anchor="w")

    lbl_msg = tk.Label(frame_actual, text="", fg="red")

    def hacer_login():
        global usuario_actual
        user = entry_user.get().strip()
        pwd  = entry_pass.get()
        try:
            if not user or not pwd:
                raise ErrorValidacion("Rellena todos los campos.")
            conn = conectar()
            cur = conn.cursor()
            cur.execute("SELECT id FROM usuarios WHERE usuario=%s AND password=%s", (user, pwd))
            fila = cur.fetchone()
            cur.close()
            conn.close()
            if fila is None:
                raise ErrorValidacion("Usuario o contrasena incorrectos.")
            usuario_actual = user
            pantalla_inicio()
        except ErrorValidacion as e:
            lbl_msg.config(text=str(e))

    entry_pass.bind("<Return>", lambda e: hacer_login())

    tk.Button(frame_actual, text="Entrar", command=hacer_login, width=12, pady=4).pack(anchor="w", pady=(16, 4))
    tk.Button(frame_actual, text="Registrarse", command=pantalla_register, width=12, pady=4, bg="#4a9e6b" ).pack(anchor="w")
    lbl_msg.pack(anchor="w", pady=(8, 0))


def pantalla_register():
    global frame_actual
    limpiar()
    frame_actual = tk.Frame(ventana, bg="#f0f4f8")
    frame_actual.pack(fill=tk.BOTH, expand=True, padx=40, pady=40)

    tk.Label(frame_actual, text="Crear cuenta", font=("Helvetica", 18, "bold")).pack(anchor="w")

    tk.Label(frame_actual, text="Usuario:").pack(anchor="w", pady=(16, 0))
    entry_user = tk.Entry(frame_actual, width=30)
    entry_user.pack(anchor="w")

    tk.Label(frame_actual, text="Contrasena:").pack(anchor="w", pady=(8, 0))
    entry_pass = tk.Entry(frame_actual, width=30, show="*")
    entry_pass.pack(anchor="w")

    tk.Label(frame_actual, text="Repetir contrasena:").pack(anchor="w", pady=(8, 0))
    entry_pass2 = tk.Entry(frame_actual, width=30, show="*")
    entry_pass2.pack(anchor="w")

    lbl_msg = tk.Label(frame_actual, text="", fg="red")

    def hacer_register():
        user  = entry_user.get().strip()
        pwd   = entry_pass.get()
        pwd2  = entry_pass2.get()
        try:
            if not user or not pwd or not pwd2:
                raise ErrorValidacion("Rellena todos los campos.")
            if pwd != pwd2:
                raise ErrorValidacion("Las contrasenas no coinciden.")
            conn = conectar()
            cur = conn.cursor()
            cur.execute("INSERT INTO usuarios (usuario, password) VALUES (%s, %s)", (user, pwd))
            conn.commit()
            cur.close()
            conn.close()
            messagebox.showinfo("Listo", "Cuenta creada. Ya puedes iniciar sesion.")
            pantalla_login()
        except ErrorValidacion as e:
            lbl_msg.config(text=str(e))
        except Exception as e:
            lbl_msg.config(text="Ese usuario ya existe.", fg="red")

    tk.Button(frame_actual, text="Registrarse", command=hacer_register, width=12, pady=4, bg="#4a9e6b").pack(anchor="w", pady=(16, 4))
    tk.Button(frame_actual, text="Volver", command=pantalla_login, width=12, pady=4).pack(anchor="w")
    lbl_msg.pack(anchor="w", pady=(8, 0))


menubar = tk.Menu(ventana)

m_archivo = tk.Menu(menubar, tearoff=0)
m_archivo.add_command(label="Salir", command=ventana.quit)
menubar.add_cascade(label="Archivo", menu=m_archivo)

m_gastos = tk.Menu(menubar, tearoff=0)
m_gastos.add_command(label="Nuevo gasto", command=pantalla_crear)
m_gastos.add_command(label="Ver gastos", command=pantalla_lista)
m_gastos.add_separator()
m_gastos.add_command(label="Exportar CSV", command=pantalla_csv)
menubar.add_cascade(label="Gastos", menu=m_gastos)

m_ayuda = tk.Menu(menubar, tearoff=0)
m_ayuda.add_command(label="Acerca de", command=lambda: messagebox.showinfo("Acerca de", "Registro de Gastos v1.0"))
menubar.add_cascade(label="Ayuda", menu=m_ayuda)

ventana.config(menu=menubar)
ventana.configure(bg="#f0f4f8")

inicializar_bd()
pantalla_login()
ventana.mainloop()