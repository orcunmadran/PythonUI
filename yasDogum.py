from tkinter import *

pencere = Tk()
pencere.title("Yaş Doğum Tarihi Hesap")
pencere.iconbitmap("ico/kitap.ico")
pencere.geometry("550x350")

def hesapYap():
    girilenYas = int(yas.get())
    dogumGoster = 2022 - girilenYas
    sonuc = Label(pencere, text="Doğum tarihiniz " + str(dogumGoster))
    sonuc.pack()

baslik = Label(pencere, text="Yaş - Doğum Hesaplama")
yas = Entry(pencere, width=25, borderwidth=1)
hesapla = Button(pencere, text="Hesapla",command=hesapYap)
baslik.pack()
yas.pack()
hesapla.pack()

pencere.mainloop()