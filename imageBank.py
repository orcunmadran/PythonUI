from tkinter import *
from PIL import ImageTk, Image

pencere = Tk()
pencere.title("Resim Albümü")
pencere.iconbitmap("ico/otel.ico")
pencere.geometry("750x650")

goster = 0
gorseller = ["img/a.png", "img/b.png"]
gorsel = ImageTk.PhotoImage(Image.open(gorseller[goster]))
gorselTutucu = Label(image=gorsel)
gorselTutucu.pack()

pencere.mainloop()