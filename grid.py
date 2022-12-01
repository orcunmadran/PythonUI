#Grid Sistemi
from tkinter import *

pencere = Tk()
pencere.title("Grid Uygulaması")

baslik = Label(pencere, text="Başlık Satırı")
etiket1 = Label(pencere, text="[ Birinci satır, birinci sütun ]")
etiket2 = Label(pencere, text="[ Birinci satır, ikinci sütun ]")
etiket3 = Label(pencere, text="[ İkinci satır, birinci sütun ]")
etiket4 = Label(pencere, text="[ İkinci satır, ikinci sütun ]")
buton1 = Button(pencere, text="<<< Buton >>>", fg="red", bg="green")
buton2 = Button(pencere, text="<<< Buton >>>", fg="black", bg="green")
buton3 = Button(pencere, text="<<< Çıkış >>>", fg="black", bg="red", command=pencere.quit)

baslik.grid(row=0, columnspan=2, padx=50, pady=25)
baslik.config(font=("Times New Roman", 30))
etiket1.grid(row=1, column=0, padx= 10, pady=20)
etiket2.grid(row=1, column=1, padx= 10, pady=20)
etiket3.grid(row=2, column=0, padx= 10, pady=20)
etiket4.grid(row=2, column=1, padx= 10, pady=20)
buton1.grid(row=3, column=0, padx=50, pady=10)
buton2.grid(row=3, column=1, padx=50, pady=10)
buton3.grid(row=4, columnspan=2, padx=5, pady=10)

pencere.mainloop()
