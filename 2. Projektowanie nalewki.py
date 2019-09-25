from tkinter import *
from tkinter import messagebox, filedialog
import pickle

#Funkcje Przycisków:
def sprawdz(stan_dalej):
    """Zmienia stan przycisku 'Dalej' jeśli użytkownik wybrał niezbędne opcje"""
    if stan_dalej == "0":
        button_dalej.configure(state=NORMAL)
    else: pass

def wyczysc_alko(moc_a, ilosc_a, docelowe_a):
    """"Funkcja opróżniająca pola wprowadzanie w ramce alkohol"""
    moc_a.delete(0, END)
    ilosc_a.delete(0, END)
    docelowe_a.delete(0, END)

def oblicz_alko( ramka, moc_a, ilosc_a, docelowe_a):
    """Funkcja dokonująca obliczeń na podstawie wprowadzonych do kalkulatora danych w ramce alkohol"""
    # Pobranie danych i zamiana na zmiennoprzecinkowe:
    moc = float(moc_a.get())
    ilosc = float(ilosc_a.get())
    docelowa = float(docelowe_a.get())
    # Obliczenia:
    stezenie = (moc * ilosc) / 100
    ilosc_calk = stezenie * 100 / docelowa
    ilosc_wody = ilosc_calk - ilosc
    # Umieszczenie obliczeń:
    label_wynik_woda = Label(ramka, text="{:.2f}".format(ilosc_wody), font=("Times New Roman", 11), relief=GROOVE)
    label_wynik_ilosc_calk = Label(ramka, text="{:.2f}".format(ilosc_calk), font=("Times New Roman", 11), relief=GROOVE)
    label_litr_woda = Label(ramka, text="L", justify=LEFT, font=("Times New Roman", 11))
    label_litr_ilosc_calk = Label(ramka, text="L", justify=LEFT, font=("Times New Roman", 11))

    label_wynik_woda.grid(row=3, column=2)
    label_wynik_ilosc_calk.grid(row=4, column=2)
    label_litr_woda.grid(row=3, column=3, sticky=W)
    label_litr_ilosc_calk.grid(row=4, column=3, sticky=W)

def oblicz_slodzenie(ramka, ilosc_nalewki, zmienna_radio_slodzenie, zmienna_radio_sub_slodzaca):
    """Funkcja obliczająca ilość substancji słodzącej na podstawie wyborów dokonanych przez użytkownika"""
    ilosc_n = float(ilosc_nalewki.get())
    zmienna_radio_slodzenie = int(zmienna_radio_slodzenie)
    zmienna_radio_sub_slodzaca = int(zmienna_radio_sub_slodzaca)
    if zmienna_radio_sub_slodzaca == 60:
        ilosc_gram = ilosc_n * zmienna_radio_slodzenie
        ilosc_ml = ilosc_gram / 100 * zmienna_radio_sub_slodzaca
        sub = 'cukru'
    elif zmienna_radio_sub_slodzaca == 75:
        ilosc_gram = ilosc_n * (zmienna_radio_slodzenie * 30 / 100)
        ilosc_ml = ilosc_gram * zmienna_radio_sub_slodzaca
        sub = 'miodu'
    elif zmienna_radio_sub_slodzaca == 0 or zmienna_radio_slodzenie == 0:
        komunikat_kalkulator = messagebox.showinfo(ramka, text="Nim przejdziesz dalej musisz wybrać typ nalewki i rodzaj substancji słodzącej")
    label_wynik_gram = Label(ramka, text="Należy dodać: {:.2f} gram {}".format(ilosc_gram, sub),
                             font=("Times New Roman", 11), relief=GROOVE)
    label_wynik_ml = Label(ramka,
                           text="Należy dodać: {:.2f} ml {}".format(ilosc_ml, sub),
                           font=("Times New Roman", 11), relief=GROOVE)
    label_wynik_gram.grid(row=5, column=2, columnspan=2, sticky=W)
    label_wynik_ml.grid(row=6, column=2, columnspan=2, sticky=W)

def wyczysc_slodzenie(ilosc_nalewki, zmienna_radio_slodzenie, zmienna_radio_sub_slodzaca):
    """Funkcja opróżniająca pola w ramce słodzenie"""
    ilosc_nalewki.delete(0, END)
    zmienna_radio_sub_slodzaca.set("0")
    zmienna_radio_slodzenie.set("0")

def kalkulator():
    """Okno kalkulatora z podziałęm na ramkę odpowiadającą za oblicznia związane z alkoholem i ramkę odpowiedzialną za
    obliczenia związane ze słodkością w nalewce."""
    okno_kalkulatora = Toplevel(padx=10, pady=10)
    # GUI kalkulatora - definiowanie:
        # GUI Alkohol:
    frame_alkohol = LabelFrame(okno_kalkulatora, text="Kalkulator rozcięczania:", padx=10, pady=10)
        # GUI Słodzenie:
    frame_slodzenie = LabelFrame(okno_kalkulatora, text="Kalkulator słodzenia:", padx=10, pady=10)
        # Tekst Alkohol
    label_moc_alko = Label(frame_alkohol, text="Moc rozcieńczanego alkoholu:", justify=LEFT,
                           font=("Times New Roman", 11))
    label_ilosc_alko = Label(frame_alkohol, text="Ilość alkoholu:", font=("Times New Roman", 11))
    label_stezenie = Label(frame_alkohol, text="Moc docelowa nalewki:", justify=LEFT, font=("Times New Roman", 11))
    label_woda = Label(frame_alkohol, text="Ilość wody, którą należy dodać:", justify=LEFT,
                       font=("Times New Roman", 11))
    label_ilosc_calk = Label(frame_alkohol, text="Ilość otrzymanej mieszaniny:", justify=LEFT,
                             font=("Times New Roman", 11))
    label_litr_ilosc_a = Label(frame_alkohol, text="L", justify=LEFT, font=("Times New Roman", 11))
    label_procent_moc = Label(frame_alkohol, text="%",  justify=LEFT, font=("Times New Roman", 11))
    laabel_procent_stezenie =Label(frame_alkohol, text="%", justify=LEFT, font=("Times New Roman", 11))

        # Tekst Słodzenie:
    label_wybierz_rodzaj_nalewki = Label(frame_slodzenie, text="Wybierz rodzaj przygotowywanej\nprzez Ciebie nalewki:",
                                         font=("Times New Roman", 11), padx=20, justify=LEFT)
    label_wybierz_sub_slodzaca = Label(frame_slodzenie, text="Wybierz czym słodzisz nalewkę:", font=("Times New Roman", 11), padx=20)
    label_ilosc_nalewki = Label(frame_slodzenie, text="Wprowadź ilość nalewki do osłodzenia", font=("Times New Roman", 11) )
    label_litr_ilosc_nalewki = Label(frame_slodzenie, text="L", font=("Times New Roman", 11))
        # Wprowadzane
    entry_moc_alko = Entry(frame_alkohol, width=3, relief=GROOVE, font=("Times New Roman", 11))
    entry_ilosc_alko = Entry(frame_alkohol, width=3, relief=GROOVE, font=("Times New Roman", 11))
    entry_moc_calk = Entry(frame_alkohol, width=3, relief=GROOVE, font=("Times New Roman", 11))
    entry_ilosc_nalewki = Entry(frame_slodzenie, width=3, relief=GROOVE, font=("Times New Roman", 11))

    moc_a = entry_moc_alko
    ilosc_a = entry_ilosc_alko
    docelowe_a = entry_moc_calk
    ilosc_nalewki = entry_ilosc_nalewki

        # Przyciski Radio słodzenie:
    zmienna_radio_sub_slodzaca = IntVar()
    zmienna_radio_sub_slodzaca.set("0")
    zmienna_radio_slodzenie = IntVar()
    zmienna_radio_slodzenie.set("0")
    radio_wytrawna = Radiobutton(frame_slodzenie, text = "wytrawna", font = ("Times New Roman", 11),
                                 variable=zmienna_radio_slodzenie, value=50)
    radio_polwytrawna = Radiobutton(frame_slodzenie, text = "półwytrawna", font = ("Times New Roman", 11),
                                    variable=zmienna_radio_slodzenie, value=100)
    radio_polslodka = Radiobutton(frame_slodzenie, text="półsłodka", font=("Times New Roman", 11),
                                    variable=zmienna_radio_slodzenie, value=200)
    radio_slodka = Radiobutton(frame_slodzenie, text="słodka", font=("Times New Roman", 11),
                                  variable=zmienna_radio_slodzenie, value=300)
    radio_likier = Radiobutton(frame_slodzenie, text="likier/krem", font=("Times New Roman", 11),
                                  variable=zmienna_radio_slodzenie, value=400 )
    radio_cukier = Radiobutton(frame_slodzenie, text="cukier",font=("Times New Roman", 11),
                               variable=zmienna_radio_sub_slodzaca, value=60)
    radio_miod = Radiobutton(frame_slodzenie, text="miód", font=("Times New Roman", 11),
                             variable=zmienna_radio_sub_slodzaca, value=75)
        # Przyciski
    button_oblicz_alkohol = Button(frame_alkohol, text="OBLICZ",
                           command=lambda: oblicz_alko(frame_alkohol, moc_a, ilosc_a, docelowe_a),
                           font=("Times New Roman", 10), relief=GROOVE)
    button_wyczysc_alkohol = Button(frame_alkohol, text="WYCZYŚĆ", command=lambda: wyczysc_alko(moc_a, ilosc_a, docelowe_a),
                            font=("Times New Roman", 10), relief=GROOVE)
    button_oblicz_slodzenie = Button(frame_slodzenie, text="OBLICZ",
                                     command= lambda: oblicz_slodzenie(frame_slodzenie, ilosc_nalewki, zmienna_radio_slodzenie.get(), zmienna_radio_sub_slodzaca.get()),
                             font=("Times New Roman", 10), relief=GROOVE)
    button_wyczysc_slodzenie = Button(frame_slodzenie, text="WYCZYŚĆ",
                                      command= lambda: wyczysc_slodzenie(ilosc_nalewki, zmienna_radio_slodzenie, zmienna_radio_sub_slodzaca),
                                      font=("Times New Roman", 10), relief=GROOVE)

    button_zamknij_kalkulator = Button(okno_kalkulatora, text="ZAMKNIJ", command=okno_kalkulatora.destroy, font=("Times New Roman", 10), relief=GROOVE)
    # GUI Kalkulatora - umieszczanie:

        # GUI Alkohol:
    frame_alkohol.grid(row=1, column=0)
        # GUI Słodzenie:
    frame_slodzenie.grid(row=2, column=0)
        # Tekst
    label_moc_alko.grid(row=0, column=1, sticky=W)
    label_ilosc_alko.grid(row=1, column=1, sticky=W)
    label_stezenie.grid(row=2, column=1, sticky=W)
    label_woda.grid(row=3, column=1, sticky=W)
    label_ilosc_calk.grid(row=4, column=1, sticky=W)
    label_litr_ilosc_a.grid(row=1, column=3, sticky=W)
    label_procent_moc.grid(row=0, column=3, sticky=W)
    laabel_procent_stezenie.grid(row=2, column=3, sticky=W)

    label_wybierz_rodzaj_nalewki.grid(row=1, column = 1, rowspan= 2, sticky= E)
    label_wybierz_sub_slodzaca.grid(row=1, column=2, columnspan=3, sticky=NE)
    label_ilosc_nalewki.grid(row=4, column=2, sticky=E)
    label_litr_ilosc_nalewki.grid(row=4, column=4, sticky=W)
        ##Wprowadzane
    entry_moc_alko.grid(row=0, column=2, padx=20)
    entry_ilosc_alko.grid(row=1, column=2, padx=20)
    entry_moc_calk.grid(row=2, column=2, padx=20)

    entry_ilosc_nalewki.grid(row=4, column=3)
        # Przyciski
    button_oblicz_alkohol.grid(row=5, column=4, sticky=E)
    button_wyczysc_alkohol.grid(row=5, column=0, sticky=W)

    button_oblicz_slodzenie.grid(row=8, column=5, sticky=E)
    button_wyczysc_slodzenie.grid(row=8, column=0, sticky=W)
        # Radio
    radio_wytrawna.grid(row=3, column=1, sticky=W)
    radio_polwytrawna.grid(row=4, column=1, sticky=W)
    radio_polslodka.grid(row=5, column=1, sticky=W)
    radio_slodka.grid(row=6, column=1, sticky=W)
    radio_likier.grid(row=7, column=1, sticky=W)

    radio_cukier.grid(row=2, column=2)
    radio_miod.grid(row=2, column=3)

    button_zamknij_kalkulator.grid(row=3, column=0, sticky=W, pady=5)

def wyczysc_nowy(nazwa, moc, ilosc,typ, sub,sklad_1,sklad_2,sklad_3, sklad_4,sklad_5, s_ilosc_1, s_ilosc_2, s_ilosc_3,
           s_ilosc_4,s_ilosc_5,jed_1, jed_2,jed_3, jed_4, jed_5 ):
    """Funkcja opróżniająca pola w oknie nowego projektu"""
    nazwa.delete(0, END)
    moc.delete(0, END)
    ilosc.delete(0, END)
    typ.set("wytrawna")
    sub.set("cukier")
    sklad_1.delete(0, END)
    sklad_2.delete(0, END)
    sklad_3.delete(0, END)
    sklad_4.delete(0, END)
    sklad_5.delete(0, END)
    s_ilosc_1.delete(0, END)
    s_ilosc_2.delete(0, END)
    s_ilosc_3.delete(0, END)
    s_ilosc_4.delete(0, END)
    s_ilosc_5.delete(0, END)
    jed_1.set("szt.")
    jed_2.set("szt.")
    jed_3.set("szt.")
    jed_4.set("szt.")
    jed_5.set("szt.")

def zapis(okno, nazwa, moc, ilosc,typ, sub,sklad_1,sklad_2,sklad_3, sklad_4,sklad_5, s_ilosc_1, s_ilosc_2, s_ilosc_3,
          s_ilosc_4,s_ilosc_5,jed_1, jed_2,jed_3, jed_4, jed_5 ):
    """Przygotowuje dane do zapisu, a następnie je zapisuje za pomocą peklowania."""
    nazwa = str(nazwa.get())
    moc = str(moc.get())
    ilosc = str(ilosc.get())
    typ = str(typ.get())
    sub = str(sub.get())
    sklad_1 = str(sklad_1.get())
    sklad_2 = str(sklad_2.get())
    sklad_3 = str(sklad_3.get())
    sklad_4 = str(sklad_4.get())
    sklad_5 = str(sklad_5.get())
    s_ilosc_1 = str(s_ilosc_1.get())
    s_ilosc_2 = str(s_ilosc_2.get())
    s_ilosc_3 = str(s_ilosc_3.get())
    s_ilosc_4 = str(s_ilosc_4.get())
    s_ilosc_5 = str(s_ilosc_5.get())
    jed_1 = str(jed_1.get())
    jed_2 = str(jed_2.get())
    jed_3 = str(jed_3.get())
    jed_4 = str(jed_4.get())
    jed_5 = str(jed_5.get())
    magazyn = { 1:nazwa, 2:moc, 3:ilosc, 4:typ, 5:sub, 6:sklad_1+" "+s_ilosc_1+" "+jed_1, 7:sklad_2+" "+s_ilosc_2+" "+jed_2,
    8:sklad_3+" "+s_ilosc_3+" "+jed_3, 9:sklad_4+" "+s_ilosc_4+" "+jed_4, 10:sklad_5+" "+s_ilosc_5+" "+jed_5,}
    plik_magazyn = open(nazwa+".txt", "ab")
    pickle.dump(magazyn, plik_magazyn)
    plik_magazyn.close()
    messagebox.showinfo(okno, "Nalewka została zapisana!")

def nowy_projekt():
    """Okno projektu, umożliwiające dobór składników i zapis skomponowanej przez siebię nalewki."""
    #Definiowanie zmiennych z list:
    zmienna_typ_nalewki = StringVar()
    zmienna_typ_nalewki.set("wytrawna")
    typ = zmienna_typ_nalewki
    zmienna_sub_slodzaca = StringVar()
    zmienna_sub_slodzaca.set("cukier")
    sub = zmienna_sub_slodzaca
    zmienna_jednostki_1 = StringVar()
    zmienna_jednostki_1.set("")
    jed_1 = zmienna_jednostki_1
    zmienna_jednostki_2 = StringVar()
    zmienna_jednostki_2.set("")
    jed_2 = zmienna_jednostki_2
    zmienna_jednostki_3 = StringVar()
    zmienna_jednostki_3.set("")
    jed_3 = zmienna_jednostki_3
    zmienna_jednostki_4 = StringVar()
    zmienna_jednostki_4.set("")
    jed_4 = zmienna_jednostki_4
    zmienna_jednostki_5 = StringVar()
    zmienna_jednostki_5.set("")
    jed_5 = zmienna_jednostki_5

    okno_nowego_projektu = Toplevel(padx=10, pady=10)

    #Pola w oknie
    label_nazwa = Label(okno_nowego_projektu, text="Nazwa nalewki:", font=("Times New Roman", 11))
    entry_nazwa = Entry(okno_nowego_projektu, relief=GROOVE, font=("Times New Roman", 11))
    label_moc = Label(okno_nowego_projektu, text="Zawartość alkoholu(%):", font=("Times New Roman", 11))
    entry_moc = Entry(okno_nowego_projektu, width=2, relief=GROOVE, font=("Times New Roman", 11))
    label_ilosc = Label(okno_nowego_projektu, text="Ilość(L):", font=("Times New Roman", 11))
    entry_ilosc = Entry(okno_nowego_projektu, width=2, relief=GROOVE, font=("Times New Roman", 11))
    label_typ = Label(okno_nowego_projektu, text="Typ nalewki:",  font=("Times New Roman", 11))
    optionm_typ = OptionMenu(okno_nowego_projektu, zmienna_typ_nalewki, "wytrawna", "półwytrawna", "półsłodka", "słodka",
                        "likier/krem" )
    label_sub_slodzaca = Label(okno_nowego_projektu, text="Sub. słodząca:", font=("Times New Roman", 11))
    optionm_sub_slodzaca = OptionMenu(okno_nowego_projektu, zmienna_sub_slodzaca, "cukier", "miód")
    button_zamknij_nowy = Button(okno_nowego_projektu, text="ZAMKNIJ", command=okno_nowego_projektu.destroy,
                                       font=("Times New Roman", 10), relief=GROOVE)
    button_wyczysc_nowy = Button(okno_nowego_projektu, text="WYCZYŚĆ", font=("Times New Roman", 10), relief=GROOVE,
                                command=lambda:wyczysc_nowy(nazwa, moc, ilosc,typ, sub,sklad_1,sklad_2,sklad_3, sklad_4,
                                                      sklad_5, s_ilosc_1, s_ilosc_2, s_ilosc_3,s_ilosc_4,s_ilosc_5,
                                                      jed_1, jed_2,jed_3, jed_4, jed_5 ))
    button_zapisz_nowy = Button(okno_nowego_projektu, text="ZAPISZ", font=("Times New Roman", 10), relief=GROOVE,
                                command=lambda:zapis(okno_nowego_projektu,nazwa, moc, ilosc,typ, sub,sklad_1,sklad_2,
                                                     sklad_3, sklad_4,sklad_5, s_ilosc_1, s_ilosc_2, s_ilosc_3,
                                                     s_ilosc_4,s_ilosc_5,jed_1, jed_2,jed_3, jed_4, jed_5 ))
    #Utworzenie zmiennych z pol w oknie - bardziej przyjaznych w użytkowaniu:
    nazwa = entry_nazwa
    moc = entry_moc
    ilosc= entry_ilosc


    ramka_lista_składnikow = LabelFrame(okno_nowego_projektu, text="Dodatki", padx=10, pady=10)

    #Pola w ramce
        #1
    label_sladnik_1 = Label(ramka_lista_składnikow, text="1. Składnik:", font=("Times New Roman", 11))
    entry_skladnik_1 = Entry(ramka_lista_składnikow, relief=GROOVE, font=("Times New Roman", 11))
    label_sladnik_1_ilosc = Label(ramka_lista_składnikow, text="Ilość:", font=("Times New Roman", 11))
    entry_skladnik_1_ilosc = Entry(ramka_lista_składnikow, width=4, relief=GROOVE, font=("Times New Roman", 11))
    optionm_skladnik_1 = OptionMenu(ramka_lista_składnikow, zmienna_jednostki_1, "l", "ml", "kg", "dag", "g","szt.")
        #2
    label_sladnik_2 = Label(ramka_lista_składnikow, text="2. Składnik:", font=("Times New Roman", 11))
    entry_skladnik_2 = Entry(ramka_lista_składnikow, relief=GROOVE, font=("Times New Roman", 11))
    label_sladnik_2_ilosc = Label(ramka_lista_składnikow, text="Ilość:", font=("Times New Roman", 11))
    entry_skladnik_2_ilosc = Entry(ramka_lista_składnikow, width=4, relief=GROOVE, font=("Times New Roman", 11))
    optionm_skladnik_2 = OptionMenu(ramka_lista_składnikow, zmienna_jednostki_2, "l", "ml", "kg", "dag", "g","szt.")
        #3
    label_sladnik_3 = Label(ramka_lista_składnikow, text="3. Składnik:", font=("Times New Roman", 11))
    entry_skladnik_3 = Entry(ramka_lista_składnikow, relief=GROOVE, font=("Times New Roman", 11))
    label_sladnik_3_ilosc = Label(ramka_lista_składnikow, text="Ilość:", font=("Times New Roman", 11))
    entry_skladnik_3_ilosc = Entry(ramka_lista_składnikow, width=4, relief=GROOVE, font=("Times New Roman", 11))
    optionm_skladnik_3 = OptionMenu(ramka_lista_składnikow, zmienna_jednostki_3, "l", "ml", "kg", "dag", "g","szt.")
        #4
    label_sladnik_4 = Label(ramka_lista_składnikow, text="4. Składnik:", font=("Times New Roman", 11))
    entry_skladnik_4 = Entry(ramka_lista_składnikow, relief=GROOVE, font=("Times New Roman", 11))
    label_sladnik_4_ilosc = Label(ramka_lista_składnikow, text="Ilość:", font=("Times New Roman", 11))
    entry_skladnik_4_ilosc = Entry(ramka_lista_składnikow, width=4, relief=GROOVE, font=("Times New Roman", 11))
    optionm_skladnik_4 = OptionMenu(ramka_lista_składnikow, zmienna_jednostki_4, "l", "ml", "kg", "dag", "g","szt.")
        #5
    label_sladnik_5 = Label(ramka_lista_składnikow, text="5. Składnik:", font=("Times New Roman", 11))
    entry_skladnik_5 = Entry(ramka_lista_składnikow, relief=GROOVE, font=("Times New Roman", 11))
    label_sladnik_5_ilosc = Label(ramka_lista_składnikow, text="Ilość:", font=("Times New Roman", 11))
    entry_skladnik_5_ilosc = Entry(ramka_lista_składnikow, width=4, relief=GROOVE, font=("Times New Roman", 11))
    optionm_skladnik_5 = OptionMenu(ramka_lista_składnikow, zmienna_jednostki_5, "l", "ml", "kg", "dag", "g","szt.")

    #Utworzenie zmiennych z pól w ramce:
    sklad_1 = entry_skladnik_1
    s_ilosc_1 = entry_skladnik_1_ilosc
    sklad_2 = entry_skladnik_2
    s_ilosc_2 = entry_skladnik_2_ilosc
    sklad_3 = entry_skladnik_3
    s_ilosc_3 = entry_skladnik_3_ilosc
    sklad_4 = entry_skladnik_4
    s_ilosc_4 = entry_skladnik_4_ilosc
    sklad_5 = entry_skladnik_5
    s_ilosc_5 = entry_skladnik_5_ilosc

    #Umieszczanie:
    label_nazwa.grid(row=0, column=1, pady=10)
    entry_nazwa.grid(row=0, column = 2,pady=10, sticky = W)
    label_moc.grid(row=1, column= 1, pady=10)
    entry_moc.grid(row=1, column=2, pady=10, sticky=W)
    label_ilosc.grid(row=1, column=3, pady=10)
    entry_ilosc.grid(row=1, column=4, pady=10, sticky=W)
    label_typ.grid(row=2, column=1, pady=10)
    optionm_typ.grid(row=2, column=2,pady=10, sticky=W)
    label_sub_slodzaca.grid(row=2, column=3, pady=10)
    optionm_sub_slodzaca.grid(row=2, column=4,pady=10, sticky=W)
    button_zamknij_nowy.grid(row = 8, column = 0, padx=5, pady=5)
    button_wyczysc_nowy.grid(row = 8, column=3, padx=5, pady=5)
    button_zapisz_nowy.grid(row = 8, column=5, padx=5, pady=5)

    ramka_lista_składnikow.grid(row=3, column=1, columnspan = 4)
        #1
    label_sladnik_1.grid(row=3, column=1, padx= 10, pady = 10)
    entry_skladnik_1.grid(row=3, column=2,padx= 10, pady = 10)
    label_sladnik_1_ilosc.grid(row=3, column=3,padx= 10, pady = 10)
    entry_skladnik_1_ilosc.grid(row=3, column=4,padx= 10, pady = 10)
    optionm_skladnik_1.grid(row=3, column=5,padx= 10, pady = 10)
        #2
    label_sladnik_2.grid(row=4, column=1,padx= 10, pady = 10)
    entry_skladnik_2.grid(row=4, column=2)
    label_sladnik_2_ilosc.grid(row=4, column=3,padx= 10, pady = 10)
    entry_skladnik_2_ilosc.grid(row=4, column=4,padx= 10, pady = 10)
    optionm_skladnik_2.grid(row=4, column=5,padx= 10, pady = 10)
        #3
    label_sladnik_3.grid(row=5, column=1,padx= 10, pady = 10)
    entry_skladnik_3.grid(row=5, column=2,padx= 10, pady = 10)
    label_sladnik_3_ilosc.grid(row=5, column=3,padx= 10, pady = 10)
    entry_skladnik_3_ilosc.grid(row=5, column=4,padx= 10, pady = 10)
    optionm_skladnik_3.grid(row=5, column=5,padx= 10, pady = 10)
        #4
    label_sladnik_4.grid(row=6, column=1,padx= 10, pady = 10)
    entry_skladnik_4.grid(row=6, column=2,padx= 10, pady = 10)
    label_sladnik_4_ilosc.grid(row=6, column=3,padx= 10, pady = 10)
    entry_skladnik_4_ilosc.grid(row=6, column=4,padx= 10, pady = 10)
    optionm_skladnik_4.grid(row=6, column=5)
        #5
    label_sladnik_5.grid(row=7, column=1,padx= 10, pady = 10)
    entry_skladnik_5.grid(row=7, column=2,padx= 10, pady = 10)
    label_sladnik_5_ilosc.grid(row=7, column=3,padx= 10, pady = 10)
    entry_skladnik_5_ilosc.grid(row=7, column=4,padx= 10, pady = 10)
    optionm_skladnik_5.grid(row=7, column=5,padx= 10, pady = 10)

def wskaz_plik(ramka_wczytanego):
    """Funkcja wczytująca projekt i umieszczająca go w oknie wczytawania projektu, w oddzielnej ramce."""
    otworz = filedialog.askopenfilename(initialdir="*/", title="Wybierz projekt:",
                           filetypes=(("pliki txt", "*.txt"), ("wszystkie pliki", "*.*")))

    plik_magazyn = open(file=otworz, mode="rb")
    magazyn = pickle.load(plik_magazyn)


    label_nazwa = Label(ramka_wczytanego, text=magazyn[1], font=("Times New Roman", 16, "bold italic"), justify=CENTER)
    label_moc_i_ilosc = Label(ramka_wczytanego, text="Moc nalewki: "+magazyn[2]+"\t Ilość: "+magazyn[3],
                              font=("Times New Roman", 11))
    label_typ_i_sub = Label(ramka_wczytanego, text="Typ : "+magazyn[4]+"\t Sub. słodząca: "+magazyn[5],
                              font=("Times New Roman", 11))
    label_skladniki = Label(ramka_wczytanego, text="SKŁADNIKI:", font=("Times New Roman", 11, "bold"))
    label_sklad_1 = Label(ramka_wczytanego, text=magazyn[6], font=("Times New Roman", 11), justify = LEFT)
    label_sklad_2 = Label(ramka_wczytanego, text=magazyn[7], font=("Times New Roman", 11), justify = LEFT,)
    label_sklad_3 = Label(ramka_wczytanego, text=magazyn[8], font=("Times New Roman", 11), justify = LEFT,)
    label_sklad_4 = Label(ramka_wczytanego, text=magazyn[9], font=("Times New Roman", 11), justify = LEFT,)
    label_sklad_5 = Label(ramka_wczytanego, text=magazyn[10], font=("Times New Roman", 11), justify = LEFT,)

    label_nazwa.grid(row=0, column=0,columnspan=3, padx=10, pady=10)
    label_moc_i_ilosc.grid(row=1, column=0,columnspan=3,sticky=W)
    label_typ_i_sub.grid(row=2, column= 0,columnspan=3,sticky=W)
    label_skladniki.grid(row=3, column=0, sticky=W,pady=10)
    label_sklad_1.grid(row=4, column=1,sticky=W)
    label_sklad_2.grid(row=5, column=1,sticky=W)
    label_sklad_3.grid(row=6, column=1,sticky=W)
    label_sklad_4.grid(row=7, column=1,sticky=W)
    label_sklad_5.grid(row=8, column=1,sticky=W)


def wczytaj_projekt():
    """Okno wczytywanie uprzednio przygotowanego projektu"""
    okno_wczytywnia_projektu = Toplevel(padx=10, pady=10)
    ramka_wskaz_plik = LabelFrame(okno_wczytywnia_projektu, text="Wybierz projekt:")
    ramka_wczytanego = LabelFrame(okno_wczytywnia_projektu, text="Wczytany projekt:")
    button_zamknij = Button(okno_wczytywnia_projektu, text="ZAMKNIJ", command=okno_wczytywnia_projektu.destroy,
                                       font=("Times New Roman", 10), relief=GROOVE)
    button_wyczysc = Button(okno_wczytywnia_projektu, text="WYCZYŚ", font=("Times New Roman", 10), relief=GROOVE,
                            command=ramka_wczytanego.destroy)

    label_wybor = Label(ramka_wskaz_plik, text="Wskaż projekt nalewki, któy chcesz załadować.", justify = LEFT,
                        font=("Times New Roman",11))
    button_zaladuj= Button(ramka_wskaz_plik, text="WYBIERZ PLIK", font=("Times New Roman", 10), relief=GROOVE,
                           command=lambda:wskaz_plik(ramka_wczytanego))

    button_wyczysc.grid(row = 5, column=2, padx=5, pady=5)
    button_zamknij.grid(row= 5, column=0, padx=5, pady=5)

    ramka_wskaz_plik.grid(row=0, column=1)
    ramka_wczytanego.grid(row=3, column=1)

    label_wybor.grid(row=0, column=1, columnspan=3)
    button_zaladuj.grid(row=2, column=2, padx=5, pady=5)

def dalej(zmienna_radio_menu):
    """Funkcja obsługująca wybór dokonany przez użytkowanika w menu"""
    if zmienna_radio_menu  == "kalkulator":
        kalkulator()
    elif zmienna_radio_menu  == "nowy":
        nowy_projekt()
    elif zmienna_radio_menu  == "wczytaj":
        wczytaj_projekt()


#GUI:

root = Tk()
root.title("Tincture")
zmienna_radio_menu = StringVar()
zmienna_radio_menu.set("0")
stan_dalej = zmienna_radio_menu.get()
#GUI Menu Główne - definiowanie:

label_powitanie = Label(root, relief = RIDGE, text = "Witaj w Tincture!\nJest to program przeznaczony zarówno do wykonywania obliczeń koniecznych\n"
                         "do stworzenia nalewki, jak również pozwalający je projektować od zera\n"
                         "oraz otwierać wcześniej zrealizowane i zapisane projekty.\nWybierz co chcesz zrobić:", justify = LEFT, font = ("Times New Roman", 11))
radio_kalkulator = Radiobutton(root, text = "Kalkulator",font = ("Times New Roman", 11),  variable = zmienna_radio_menu , value = "kalkulator", command=lambda: sprawdz(stan_dalej))
radio_nowy_projekt = Radiobutton(root, text = "Nowy projekt", font = ("Times New Roman", 11), variable = zmienna_radio_menu , value = "nowy", command=lambda: sprawdz(stan_dalej) )
radio_wczytaj_projekt = Radiobutton(root, text = "Wczytaj projekt", font = ("Times New Roman", 11),  variable = zmienna_radio_menu , value = "wczytaj", command=lambda: sprawdz(stan_dalej))
button_dalej = Button(root, text = "DALEJ", font = ("Times New Roman", 10), command = lambda: dalej(zmienna_radio_menu.get()), relief = GROOVE, state=DISABLED)
button_zakoncz = Button(root, text = "ZAMKNIJ", font = ("Times New Roman", 10), command = root.quit, relief = GROOVE)

#GUI Menu Główne - umieszczanie:

label_powitanie.grid(row= 0, column = 1, columnspan = 3, padx = 10, pady = 10)
radio_kalkulator.grid(row = 1, column = 1, padx = 10)
radio_nowy_projekt.grid(row = 1, column = 2, padx = 10)
radio_wczytaj_projekt.grid(row = 1, column = 3, padx = 10, pady = 5)
button_dalej.grid(row = 3, column = 4, padx = 10, pady = 10)
button_zakoncz.grid(row = 3, column = 0, padx = 10, pady = 10)

root.mainloop()