from tkinter import *



m = Tk()
ilosc = 0
def generator_kilka(liczba, cos):
    ilosc_obecna = liczba
    ilosc_nowa =ilosc_obecna + int(cos.get())
    licznik = 0
    while licznik < (ilosc_nowa):
        label_2 = ilosc_obecna
        entry_2 = ilosc_obecna
        entry_licznik = entry_2 + licznik
        label_licznik = label_2 +licznik
        label_2 = Label(m, text="tekst")
        entry_2 = Entry(m,)
        label_2.grid(row =3+entry_licznik, column=0)
        entry_2.grid(row=3+label_licznik, column=1)
        licznik = licznik +1
    global ilosc
    ilosc = ilosc_nowa

def generator_poj():
    global ilosc
    ilosc = ilosc+1
    label = Label(m, text="tekst")
    entry_2 = Entry(m, )
    label.grid(row=3 + ilosc, column=0)
    entry_2.grid(row=3 + ilosc, column=1)

entry = Entry(m, width=3)
cos = entry
button = Button(m, text="pokaż", command= lambda: generator_kilka(ilosc, cos))
button_2 = Button(m, text="Dodaj", command= generator_poj)
entry.grid(row = 0, column = 0)
button.grid(row=1, column=0)
button_2.grid(row = 2, column = 0)
m.mainloop()
