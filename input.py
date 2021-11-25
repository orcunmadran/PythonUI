from tkinter import *

pencere = Tk()

def fonksiyon():
    etiket = Label(pencere, text="Merhaba " + metin.get())
    etiket.pack()


metin = Entry(pencere, width=25, borderwidth=5)
metin.pack()

buton = Button(pencere, text="Butona Tıkla!", command=fonksiyon)
buton.pack()

pencere.mainloop()