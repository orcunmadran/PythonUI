from tkinter import *
from PIL import ImageTk, Image

pencere = Tk()
pencere.title("Resim Albümü")
pencere.geometry("480x600")
pencere.wm_iconbitmap("ico/kitap.ico")

baslik = Label(pencere, text="Sabahattin Ali'nin Kitapları")
baslik.grid(row=0, column=0, padx= 10, pady=10)
baslik.config(font=("Arial", 30))

kapaklar = ["img/kitap_01.jpg", "img/kitap_02.jpg", "img/kitap_03.jpg", "img/kitap_04.jpg", "img/kitap_05.jpg"]

def goster(kapak):
    gorsel = ImageTk.PhotoImage(Image.open(kapaklar[kapak]))
    cerceve = Label(image=gorsel)
    cerceve.image = gorsel
    cerceve.grid(row=1, column=0, padx= 10, pady=10)
    kapak +=1
    print(kapak)

goster(0)

buton = Button(text="Yeni Kitap")
buton.grid(row=2, column=0, padx= 10, pady=10)
buton.config(font=("Arial", 20))

pencere.mainloop()