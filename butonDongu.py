from tkinter import *
from tkinter import ttk

pencere = Tk()
pencere.title("Ana Pencere")
pencere.geometry("300x200")

def test():
    print("test")

menuOgeleri = ["Ana Sayfa", "Fonk A", "Fonk B", "Yeni Öğe"]
menuFonksiyonlari = [quit, test, "quit", "quit"]

for idx, oge in enumerate(menuOgeleri):
    ttk.Button(pencere, text= "Button " +oge, command=menuFonksiyonlari[idx]).pack()

pencere.mainloop()