from tkinter import *

pencere = Tk()

def metinAlF():
    alinan = "Merhaba " + metin.get()
    metin.delete(0, END)
    metin.insert(0, alinan)

def metinYazF():
    metin.insert(0, "Test Metni")

def metinSilF():
    metin.delete(0, END) #END ile tamamı temizleniyor.


metin = Entry(pencere, width=25, borderwidth=5)
metin.pack()

metinAl = Button(pencere, text="Metni Al!", command=metinAlF)
metinAl.pack()

metinYaz = Button(pencere, text="Meitn Ekle!", command=metinYazF)
metinYaz.pack()

metinSil = Button(pencere, text="Metin Sil!", command=metinSilF)
metinSil.pack()

pencere.mainloop()