from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)

metin = Label(root,
    text="Hello, Tkinter",
    fg="white",
    bg="black",
    width=10,
    height=10
)

dugme = Button(root,
    text="Click me!",
    width=25,
    height=5,
    bg="white",
    fg="blue",
)

metin.pack()
dugme.pack()

root.mainloop()