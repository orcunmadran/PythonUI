from tkinter import *
from PIL import ImageTk, Image

pencere = Tk()
pencere.title("Resim Albümü")
pencere.iconbitmap("ico/otel.ico")
pencere.geometry("750x650")

goster = 0
gorseller = ["img/kitap_01.jpg", "img/kitap_02.jpg", "img/kitap_03.jpg", "img/kitap_04.jpg", "img/kitap_05.jpg"]
gorsel = ImageTk.PhotoImage(Image.open(gorseller[goster]))
gorselTutucu = Label(image=gorsel)
gorselTutucu.pack()

pencere.mainloop()