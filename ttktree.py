import sqlite3
import ttkbootstrap as tb
from ttkbootstrap.constants import *

DB_PATH = "meine_db.sqlite"

def fetch_rows():
    with sqlite3.connect(DB_PATH) as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("SELECT id, name, email FROM users ORDER BY id DESC")
        return cur.fetchall()

app = tb.Window(themename="darkly", size=(800, 400), title="SQLite Tabelle")

cols = ("id", "name", "email")
tree = tb.Treeview(app, columns=cols, show="headings", bootstyle="info")
tree.pack(fill=BOTH, expand=YES, padx=10, pady=10)

# Spaltenköpfe + Breiten
tree.heading("id", text="ID")
tree.heading("name", text="Name")
tree.heading("email", text="E-Mail")

tree.column("id", width=80, anchor=W)
tree.column("name", width=200, anchor=W)
tree.column("email", width=300, anchor=W)

# Scrollbar
scroll = tb.Scrollbar(app, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scroll.set)
scroll.pack(side=RIGHT, fill=Y)

# Daten rein
for r in fetch_rows():
    tree.insert("", "end", values=(r["id"], r["name"], r["email"]))

app.mainloop()