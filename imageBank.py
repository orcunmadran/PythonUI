from tkinter import *
from PIL import ImageTk, Image

pencere = Tk()
pencere.title("Resim Albümü")
pencere.geometry("750x600")
pencere.wm_iconbitmap("ico/kitap.ico")

baslik = Label(pencere, text="Sabahattin Ali'nin Kitapları")
baslik.pack(padx=20, pady=20)
baslik.config(font=("Arial", 30))

goster = 0
gorseller = ["img/kitap_01.jpg", "img/kitap_02.jpg", "img/kitap_03.jpg", "img/kitap_04.jpg", "img/kitap_05.jpg"]
gorsel = ImageTk.PhotoImage(Image.open(gorseller[goster]))
gorselTutucu = Label(pencere, image=gorsel)
gorselTutucu.pack()

buton = Button(pencere, text="Yeni Görsel")
buton.pack(padx=20, pady=20)
buton.config(font=("Arial", 20))

pencere.mainloop()