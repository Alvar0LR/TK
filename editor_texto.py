import os
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename


class Editor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.archivo_abierto = None
        self.title("Editor de Texto")
        self.rowconfigure(0, minsize=600, weight=1)
        self.columnconfigure(1, minsize=600, weight=1)

        self.campo_texto = tk.Text(self, wrap=tk.WORD)
        self._crear_componentes()
        self._crear_menu()


    def _abrir_archivo(self):
        ruta = askopenfilename(
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
            defaultextension=".txt"
        )
        if not ruta:
            return

        if not os.path.isfile(ruta):
            messagebox.showerror("Error", f"Archivo no existe {ruta}")
            return
        try:

            with open (ruta, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
        except Exception as e :
            messagebox.showerror("Error al leer", f"Archivo no existe {str(e)}")
            return

        self.campo_texto.delete("1.0", tk.END)
        self.campo_texto.insert("1.0", contenido)
        self.archivo_abierto = ruta
        self.title(f"Editor de Texto - {os.path.basename(ruta)}")


    def _guardar_como(self):
        ruta = asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
        )
        if not ruta:
            return  # usuario canceló

        try:
            texto = self.campo_texto.get("1.0", tk.END)
            with open (ruta, "w", encoding="utf-8") as archivo:
                archivo.write(texto)
        except Exception as e:
            messagebox.showerror("Error", f"Archivo no existe {str(e)}")
            return
        self.archivo_abierto = ruta
        self.title(f"Editor de Texto - {os.path.basename(ruta)}")

    def _guardar(self):
        if not self.archivo_abierto:
            return self._guardar_como()

        try:
            texto = self.campo_texto.get("1.0", tk.END)
            with open(self.archivo_abierto, "w", encoding="utf-8") as archivo:
                archivo.write(texto)
        except Exception as e:
            messagebox.showerror("Error", f"Archivo no existe {str(e)}")
            return None

        self.title(f"Editor de Texto - {os.path.basename(self.archivo_abierto)}")
        return None

    def _crear_componentes(self):
        frame_botones = tk.Frame(self, relief=tk.RAISED, bd=2)
        tk.Button(frame_botones, text="Abrir", command=self._abrir_archivo).grid(row=0, column=0, sticky="we", padx=5, pady=5)
        tk.Button(frame_botones, text="Guardar",command=self._guardar).grid(row=1, column=0, sticky="we", padx=5, pady=5)
        tk.Button(frame_botones, text="Guardar como",command=self._guardar_como).grid(row=2, column=0, sticky="we", padx=5, pady=5)
        frame_botones.grid(row=0, column=0, sticky="ns")
        self.campo_texto.grid(row=0, column=1, sticky="nswe", padx=5, pady=5)

    def _crear_menu(self):
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        menu_archivo = tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label="Archivo", menu=menu_archivo)
        # aquí usas command= en lugar de comando=
        menu_archivo.add_command(label="Abrir", command=self._abrir_archivo)
        menu_archivo.add_command(label="Guardar", command=self._guardar)
        menu_archivo.add_command(label="Guardar como",command=self._guardar_como)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir",command=self.quit)

if __name__ == "__main__":
    app = Editor()
    app.mainloop()
