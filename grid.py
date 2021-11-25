from tkinter import *

pencere = Tk()

baslik = Label(pencere, text="[ Başlık Satırı ]")
etiket1 = Label(pencere, text="[ Birinci satır, birinci sütun ]")
etiket2 = Label(pencere, text="[ Birinci satır, ikinci sütun ]")
etiket3 = Label(pencere, text="[ İkinci satır, birinci sütun ]")
etiket4 = Label(pencere, text="[ İkinci satır, ikinci sütun ]")
buton = Button(pencere, text="<<< Buton >>>")

baslik.grid(row=0, columnspan=2)
etiket1.grid(row=1, column=0)
etiket2.grid(row=1, column=1)
etiket3.grid(row=2, column=0)
etiket4.grid(row=2, column=1)
buton.grid(row=3, columnspan=2)

pencere.mainloop()