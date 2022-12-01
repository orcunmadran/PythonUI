from tkinter import *

pencere = Tk()
pencere.title("Ana Pencere")
pencere.geometry("300x200")

def pencereA():
    pencere2 = Tk()
    pencere2.title("Pencere A")
    pencere2.geometry("300x200")
    buton2 = Button(pencere2, text="Kapat!", command=pencere2.destroy)
    buton2.pack()

def pencereB():
    pencere3 = Tk()
    pencere3.title("Pencere B")
    pencere3.geometry("300x200")
    buton3 = Button(pencere3, text="Kapat!", command=pencere3.destroy)
    buton3.pack()

etiket = Label(pencere, text="Menü")
etiket.pack()

butonA = Button(pencere, text="A Uygulaması!", command=pencereA)
butonA.pack()

butonB = Button(pencere, text="B Uygulaması!", command=pencereB)
butonB.pack()

pencere.mainloop()