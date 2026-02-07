import tkinter as tk
from tkinter import ttk
import webbrowser
import urllib.parse


def construir_url(busqueda):
    query = urllib.parse.quote(busqueda)
    return [
        ("Amazon", f"https://www.amazon.com/s?k={query}"),
        ("eBay", f"https://www.ebay.com/sch/i.html?_nkw={query}"),
        ("AliExpress", f"https://www.aliexpress.com/wholesale?SearchText={query}"),
        ("Etsy", f"https://www.etsy.com/search?q={query}"),
        ("Rakuten", f"https://www.rakuten.com/shop/?k={query}"),
        ("Wallapop", f"https://es.wallapop.com/app/search?keywords={query}"),
        ("MercadoLibre", f"https://www.mercadolibre.com/jm/search?as_word={query}"),
        ("Milanuncios", f"https://www.milanuncios.com/anuncios/{query}.htm"),
        ("Google Shopping", f"https://www.google.com/search?tbm=shop&q={query}"),
        ("Facebook Marketplace", f"https://www.facebook.com/marketplace/search/?query={query}"),
        ("Catawiki", f"https://www.catawiki.com/en/search/?q={query}"),
    ]

def abrir_url(event):
    selected_item = tree.focus()
    if selected_item:
        item_data = tree.item(selected_item)
        url = item_data["values"][2]
        webbrowser.open_new_tab(url)


def buscar_producto():
    termino = entry_p.get()
    if not termino:
        return

    for item in tree.get_children():
        tree.delete(item)

    resultados = construir_url(termino)
    for item, termino in resultados:
        tree.insert("", "end", )


#UI principal
root = tk.Tk()
root.geometry("900x500")
root.title("MultiSearhc")

#Buscador
frame_top = tk.Frame(root)
frame_top.pack(side="top")

entry_p = tk.Entry(frame_top, width=50)
entry_p.pack(side=tk.LEFT, padx=5)

btn_buscar = tk.Button(frame_top, text="Buscar", command=buscar_producto)
btn_buscar.pack(side=tk.LEFT)

tree = ttk.Treeview(root, columns=("Producto", "Sitio", "URL"), show="headings")
tree.heading("Producto", text="Producto")
tree.heading("Sitio", text="Sitio")
tree.heading("URL", text="URL"),

tree.column("Producto", width=200)
tree.column("Sitio", width=100)
tree.column("URL", width=400)

tree.pack(pady=5)


tree.bind("<Double-1>", abrir_url)

root.mainloop()

