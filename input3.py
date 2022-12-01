from tkinter import *

pencere = Tk()

def metinAlF():
    alinan = "Merhaba " + metin.get(0.0, END)
    metin.delete(0.0, END)
    metin.insert(0.0, alinan)

def metinYazF():
    metin.insert(0.0, "Test Metni \n")

def metinSilF():
    metin.delete(0.0, END)


metin = Text(pencere)
metin.pack()

metinAl = Button(pencere, text="Metni Al!", command=metinAlF)
metinAl.pack()

metinYaz = Button(pencere, text="Meitn Ekle!", command=metinYazF)
metinYaz.pack()

metinSil = Button(pencere, text="Metin Sil!", command=metinSilF)
metinSil.pack()

pencere.mainloop()