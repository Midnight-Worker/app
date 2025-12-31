from tkinter import *
import ttkbootstrap as tb

app = tb.Window(size=(300, 200))

def pushed():
    print("Button pushed")

btn = tb.Button(app, text="Push me", command=pushed)
btn.pack(pady=5)

app.mainloop()
