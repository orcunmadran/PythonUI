from tkinter import *
from PIL import ImageTk, Image

pencere = Tk()
pencere.title("Otel Programı")
pencere.iconbitmap("ico/otel.ico")
pencere.geometry("750x650")

gorsel = ImageTk.PhotoImage(Image.open("img/otel.png"))

def fotoTutucu():
    gorselTutucu = Label(image=gorsel)
    gorselTutucu.pack()


butonum=Button(pencere, text="Foto Göster", command=fotoTutucu())
butonum.pack()

pencere.mainloop()