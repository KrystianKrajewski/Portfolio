from tkinter import *
from  tkinter import messagebox
import sqlite3

baza_logowania = sqlite3.connect("baza_logowania.db")
kursor_logowania = baza_logowania.cursor()

#Utworznie bazy logownia, jeśli nie istnieje wraz z tabelą:
kursor_logowania.execute("""CREATE TABLE IF NOT EXISTS baza_logowania (
login text,
password text)
""")
##Wprowadznie domyślnego użytkownika:
#kursor_logowania.execute("INSERT INTO baza_logowania VALUES (:login, :password)",
#                            {'login': 'deflaut',
#                              'password': 'deflaut01'
#                             })
#baza_logowania.commit()

baza_klientow=sqlite3.connect("baza_klientow.db")
kursor_klienci=baza_klientow.cursor()
#Utworzenie bazy klientów, jeśil nie istnieje w raz z tabelą
kursor_klienci.execute("""CREATE TABLE IF NOT EXISTS baza_klientow (
imie text,
nazwisko text,
miasto text,
kod_pocztowy text,
ulica text,
nr_domu text,
nr_mieszkania text,
e_mail text,
nr_tel integer
)""")

def wyczysc(imie, nazwisko, miasto, kod_1, kod_2, ulica, dom, mieszkanie, email, tel):
    """Funkcja opróżniająca wszystkie pola wprowadzania."""
    imie.delete(0,END)
    nazwisko.delete(0, END)
    miasto.delete(0, END)
    kod_1.delete(0, END)
    kod_2.delete(0, END)
    ulica.delete(0, END)
    dom.delete(0, END)
    mieszkanie.delete(0, END)
    email.delete(0, END)
    tel.delete(0, END)

def dodaj_klienta(imie, nazwisko, miasto, kod_1, kod_2, ulica, dom, mieszkanie, email, tel):
    """Funkcja wprowadzająca rekord zawierający dane nowego kilenta do bazy"""
    baza_klientow = sqlite3.connect("baza_klientow.db")
    kursor_klienci = baza_klientow.cursor()
    kursor_klienci.execute("INSERT INTO baza_klientow VALUES (:imie, :nazwisko, :miasto, :kod_pocztowy, :ulica, :nr_domu, :nr_mieszkania, :e_mail, :nr_tel)",
                           {
                               'imie': imie.get(),
                               'nazwisko': nazwisko.get(),
                               'miasto': miasto.get(),
                               'kod_pocztowy': kod_1.get()+"-"+kod_2.get(),
                               'ulica': ulica.get(),
                               'nr_domu': dom.get(),
                               'nr_mieszkania': mieszkanie.get(),
                               'e_mail': email.get(),
                               'nr_tel': tel.get()
                           })
    baza_klientow.commit()
    messagebox.showinfo("Sukces!", "Klient został dodany!")

def wprowadzana_liczbowa(inp):
    """"Funkcja pozwalająca na wprowadzanie do pola jedynie liczb."""
    if inp.isdigit():
        return TRUE
    elif inp is "":
        return TRUE
    else: return FALSE

def wprowadzana_tekstowa(inp):
    """Funkcja pozwalająca na wprowadzanie jedynie znaków alfabetycznych."""
    if inp.isalpha():
        return TRUE
    elif inp is "":
        return TRUE
    else: return False

def potwierdz(id):
    """Funkcja żądająca od użytkownika potwierdzenia usunięcia rekordu z bazy, a następni go usuwająca w przypadku
    otrzymania odpowiedzi pozytywnej."""
    odp = messagebox.askyesno("Potwierdź", "Czy jesteś pewien, że chcesz usunąć rekord o id {}?".format(id.get()))
    if odp == 'yes':
        baza_klientow = sqlite3.connect("baza_klientow.db")
        kursor_klienci = baza_klientow.cursor()
        kursor_klienci.execute("DELETE FROM baza_klientow WHERE oid = " + id.get())
        id.delete(0, END)
    else: pass

def aktualizuj(imie, nazwisko, miasto, kod, ulica, dom, mieszkanie, email, tel, id):
    baza_klientow = sqlite3.connect("baza_klientow.db")
    kursor_klienci = baza_klientow.cursor()
    kursor_klienci.execute("""UPDATE baza_klientow SET
    imie = :imie,
    nazwisko = :nazwisko,
    miasto = :miasto,
    kod_pocztowy = :kod,
    ulica = :ulica,
    nr_domu = :dom,
    nr_mieszkania = :mieszkanie,
    e_mail = :email,
    nr_tel = :tel
    WHERE oid= :oid""", {
        'imie': imie.get(),
        'nazwisko': nazwisko.get(),
        'miasto': miasto.get(),
        'kod': kod.get(),
        'ulica': ulica.get(),
        'dom': dom.get(),
        'mieszkanie': mieszkanie.get(),
        'email': email.get(),
        'tel': tel.get(),
        'oid': id

    })
    baza_klientow.commit()

def szukanie_rekordu_bazie(ramka, parametr_1, parametr_2, id, id_or_wybrany, wybrane_parametry):
    """Funkcja szukająca rekordu w bazie, a następnie wypisująca wynik w ramce."""
    baza_klientow = sqlite3.connect("baza_klientow.db")
    kursor_klienci = baza_klientow.cursor()
    if id_or_wybrany.get() == "id":
        kursor_klienci.execute('SELECT *, oid FROM baza_klientow WHERE oid = ?', (id.get(),))
        baza_klientow.commit()
    elif id_or_wybrany.get() == "wybrany":
        if wybrane_parametry.get() == "imię i nazwisko:":
            kursor_klienci.execute('SELECT *, oid FROM baza_klientow WHERE imie = ? AND nazwisko = ?',(parametr_1.get(),
                                                                                                  parametr_2.get(),))
            baza_klientow.commit()
        elif wybrane_parametry.get() == "miasto:":
            kursor_klienci.execute('SELECT * ,oid FROM baza_klientow WHERE miasto = ?', (parametr_1.get(),))
            baza_klientow.commit()
        elif wybrane_parametry.get() == "e-mail:":
            kursor_klienci.execute('SELECT *, oid FROM baza_klientow WHERE e_mail = ?', (parametr_1.get(),))
            baza_klientow.commit()
        elif wybrane_parametry.get() == "nr tel.:":
            kursor_klienci.execute('SELECT *, oid FROM baza_klientow WHERE nr_tel = ?', (parametr_1.get(),))
            baza_klientow.commit()
        else:pass
    else: pass
    rekordy_klientow = kursor_klienci.fetchall()

    label_id_naglowek = Label(ramka, text="ID:", font=("Times New Roman", 12, "bold italic"))
    label_imie_naglowek = Label(ramka, text="IMIE:", font=("Times New Roman", 12, "bold italic"))
    label_nazwisko_naglowek = Label(ramka, text="NAZWISKO:", font=("Times New Roman", 12, "bold italic"))
    label_miasto_naglowek = Label(ramka, text="MIASTO:", font=("Times New Roman", 12, "bold italic"))
    label_kod_naglowek = Label(ramka, text="KOD POCZTOWY:", font=("Times New Roman", 12, "bold italic"))
    label_ulica_naglowek = Label(ramka, text="ULICA:", font=("Times New Roman", 12, "bold italic"))
    label_dom_naglowek = Label(ramka, text="NR DOMU:", font=("Times New Roman", 12, "bold italic"))
    label_mieszkanie_naglowek = Label(ramka, text="NR MIESZKANIA:", font=("Times New Roman", 12, "bold italic"))
    label_email_naglowek = Label(ramka, text="E-MAIL:", font=("Times New Roman", 12, "bold italic"))
    label_tel_naglowek = Label(ramka, text="NR TEL.:", font=("Times New Roman", 12, "bold italic"))

    id_klienta=""
    imie_klienta=""
    nazwisko_klienta = ""
    miasto_klienta = ""
    kod_klienta = ""
    ulica_klienta = ""
    dom_klienta = ""
    mieszkanie_klienta = ""
    email_klienta = ""
    tel_klienta = ""

    for rekord_klienta in rekordy_klientow:
        id_klienta += str(rekord_klienta[9])+"\n"
        imie_klienta += str(rekord_klienta[0])+"\n"
        nazwisko_klienta += str(rekord_klienta[1])+"\n"
        miasto_klienta += str(rekord_klienta[2])+"\n"
        kod_klienta += str(rekord_klienta[3])+"\n"
        ulica_klienta += str(rekord_klienta[4])+"\n"
        dom_klienta += str(rekord_klienta[5])+"\n"
        mieszkanie_klienta += str(rekord_klienta[6])+"\n"
        email_klienta += str(rekord_klienta[7])+"\n"
        tel_klienta += str(rekord_klienta[8])+"\n"

        label_id = Label(ramka, text=id_klienta,font=("Times New Roman", 12), justify=LEFT)
        label_imie = Label(ramka, text=imie_klienta,font=("Times New Roman", 12), justify=LEFT)
        label_nazwisko = Label(ramka, text=nazwisko_klienta,font=("Times New Roman", 12), justify=LEFT)
        label_miasto = Label(ramka, text=miasto_klienta,font=("Times New Roman", 12), justify=LEFT)
        label_kod = Label(ramka, text=kod_klienta,font=("Times New Roman", 12), justify=LEFT)
        label_ulica = Label(ramka, text=ulica_klienta,font=("Times New Roman", 12), justify=LEFT)
        label_dom = Label(ramka, text=dom_klienta,font=("Times New Roman", 12), justify=LEFT)
        label_mieszkanie = Label(ramka, text=mieszkanie_klienta,font=("Times New Roman", 12), justify=LEFT)
        label_email = Label(ramka, text=email_klienta,font=("Times New Roman", 12), justify=LEFT)
        label_tel = Label(ramka, text=tel_klienta,font=("Times New Roman", 12), justify=LEFT)

        label_id.grid(row=1, column=0, rowspan=10, padx=5)
        label_imie.grid(row=1, column=1, rowspan=10, padx=5)
        label_nazwisko.grid(row=1, column=2, rowspan=10, padx=5)
        label_miasto.grid(row=1, column=3, rowspan=10, padx=5)
        label_kod.grid(row=1, column=4, rowspan=10, padx=5)
        label_ulica.grid(row=1, column=5, rowspan=10, padx=5)
        label_dom.grid(row=1, column=6, rowspan=10, padx=5)
        label_mieszkanie.grid(row=1, column=7, rowspan=10, padx=5)
        label_email.grid(row=1, column=8, rowspan=10, padx=5)
        label_tel.grid(row=1, column=9, rowspan=10, padx=5)


    label_id_naglowek.grid(row=0, column=0, padx=5, pady=10)
    label_imie_naglowek.grid(row=0, column=1, padx=5, pady=10)
    label_nazwisko_naglowek.grid(row=0, column=2, padx=5, pady=10)
    label_miasto_naglowek.grid(row=0, column=3, padx=5, pady=10)
    label_kod_naglowek.grid(row=0, column=4, padx=5, pady=10)
    label_ulica_naglowek.grid(row=0, column=5, padx=5, pady=10)
    label_dom_naglowek.grid(row=0, column=6, padx=5, pady=10)
    label_mieszkanie_naglowek.grid(row=0, column=7, padx=5, pady=10)
    label_email_naglowek.grid(row=0, column=8, padx=5, pady=10)
    label_tel_naglowek.grid(row=0, column=9, padx=5, pady=10)
    baza_klientow.commit()

def odblokowanie_wprowadzania(parametr_1, parametr_2, id,id_or_wybrany, wybrane_parametry, button_szukaj):
    """Okno blokujące możliwość wprowadzenia danych i wyszukania rekordu nim użytkownik wybierze parametr wyszukiwania."""
    if id_or_wybrany.get() == "wybrany":
        if wybrane_parametry.get() == "imię i nazwisko:":
            parametr_1.configure(state=NORMAL)
            parametr_2.configure(state=NORMAL)
            button_szukaj.configure(state=NORMAL)
        elif wybrane_parametry.get() != "0":
            parametr_1.configure(state=NORMAL)
            parametr_2.configure(state=DISABLED)
            button_szukaj.configure(state=NORMAL)
        else: pass
    elif id_or_wybrany.get() == "id":
        id.configure(state=NORMAL)
        button_szukaj.configure(state=NORMAL)
    else: pass

def okno_szukania_rekordu():
    """Funkcja tworząca okno pozwalające na wybór parametrów wyszykiwania i wprowadzenia poszukiwanej wartości,
    a następnie wywołująca funkcję przeszukującą bazę"""
    okno_szukania = Toplevel()
    okno_szukania.title("Szukaj rekordu")
    ramka_wprowadz = LabelFrame(okno_szukania, text="Wprowadź dane do wyszukania:")
    ramka_znaleziony = LabelFrame(okno_szukania, text="Znaleziony rekord:")
    parametry = ["imię i nazwisko:", "miasto:","e-mail:","nr tel.:"]
    wybrane_parametry = StringVar()
    wybrane_parametry.set(parametry[1])
    id_or_wybrany =StringVar()
    id_or_wybrany.set("0")

    entry_parametry_1 = Entry(ramka_wprowadz, font=("Times New Roman", 12), relief=GROOVE, state=DISABLED)
    entry_parametry_2 = Entry(ramka_wprowadz, font=("Times New Roman", 12), relief=GROOVE, state=DISABLED)
    label_lub = Label(ramka_wprowadz, text="lub", font=("Times New Roman", 12))

    entry_id = Entry(ramka_wprowadz, font=("Times New Roman", 12), relief=GROOVE, state=DISABLED)
    parametr_1 = entry_parametry_1
    parametr_2 = entry_parametry_2
    id = entry_id
    button_szukaj = Button(ramka_wprowadz, text="SZUKAJ", font=("Times New Roman", 12), state=DISABLED,
                           command=lambda: szukanie_rekordu_bazie(ramka_znaleziony, parametr_1, parametr_2, id,
                                                                  id_or_wybrany,  wybrane_parametry) )
    button_zamknij = Button(ramka_wprowadz, text="ZAMKNIJ", font=("Times New Roman", 12), command=okno_szukania.destroy)
    radio_wybrany = Radiobutton(ramka_wprowadz, text="Wybierz własny parametr:", variable=id_or_wybrany,
                                value="wybrany", font=("Times New Roman", 12),
                                command=lambda: odblokowanie_wprowadzania(parametr_1, parametr_2, id,id_or_wybrany,
                                                                          wybrane_parametry, button_szukaj))
    radio_id = Radiobutton(ramka_wprowadz, text="Szukaj po id:", variable=id_or_wybrany, value="id",
                           font=("Times New Roman", 12),
                           command=lambda: odblokowanie_wprowadzania(parametr_1, parametr_2, id,id_or_wybrany,
                                                                     wybrane_parametry, button_szukaj))
    om_wybierz = OptionMenu(ramka_wprowadz, wybrane_parametry, *parametry)
    ramka_wprowadz.grid(row=0, column=0)
    ramka_znaleziony.grid(row=1, column=0)
    radio_wybrany.grid(row=0, column=0, sticky=W)
    label_lub.grid(row=1, column=0)
    radio_id.grid(row=2, column=0, sticky=W)
    om_wybierz.grid(row=0, column=1, padx=1)
    entry_parametry_1.grid(row=0, column=2, padx=5, sticky=W)
    entry_parametry_2.grid(row=0, column=3, padx=5, sticky=W)
    entry_id.grid(row=2, column=1, sticky=W)
    button_szukaj.grid(row = 3, column=3, pady= 20)
    button_zamknij.grid(row=3, column=0, pady= 20)

def okno_aktualizacji_rekordu_wypelnij(id, okno):
    """Funkcja tworzy dodatkową ramkę w oknie aktualizacji, umieszczanie w niej pola tekstowe i pola wprowadzania,
     a następnie wypełnia je pobraną z bazy zawartością."""
    id = id.get()

    baza_klientow = sqlite3.connect("baza_klientow.db")
    kursor_klienci = baza_klientow.cursor()
    kursor_klienci.execute("SELECT * FROM baza_klientow WHERE oid=" +id)
    rekordy = kursor_klienci.fetchall()


    frame_dane = LabelFrame(okno, text="Dane rekordu:")
    label_imie_edycja = Label(frame_dane, text="Imię:", font=("Times New Roman", 12))
    entry_imie_edycja = Entry(frame_dane, font=("Times New Roman", 12), relief=GROOVE)
    label_nazwisko_edycja = Label(frame_dane, text="Nazwisko:", font=("Times New Roman", 12))
    entry_nazwisko_edycja = Entry(frame_dane, font=("Times New Roman", 12), relief=GROOVE)
    label_miasto_edycja = Label(frame_dane, text="Miasto:", font=("Times New Roman", 12))
    entry_miasto_edycja = Entry(frame_dane, font=("Times New Roman", 12), relief=GROOVE)
    label_kod_pocztowy_edycja = Label(frame_dane, text="Kod pocztowy:", font=("Times New Roman", 12))
    entry_kod_pocztowy_edycja = Entry(frame_dane, font=("Times New Roman", 12), relief=GROOVE, widt=6)
    label_ulica_edycja = Label(frame_dane, text="Ulica:", font=("Times New Roman", 12))
    entry_ulica_edycja = Entry(frame_dane, font=("Times New Roman", 12), relief=GROOVE)
    label_nr_domu_edycja = Label(frame_dane, text="Nr domu:", font=("Times New Roman", 12))
    entry_nr_domu_edycja = Entry(frame_dane, font=("Times New Roman", 12), relief=GROOVE, width=5)
    label_nr_mieszkania_edycja = Label(frame_dane, text="Nr mieszkania:", font=("Times New Roman", 12))
    entry_nr_mieszkania_edycja = Entry(frame_dane, font=("Times New Roman", 12), relief=GROOVE, width=5)
    label_e_mail_edycja = Label(frame_dane, text="E-mail:", font=("Times New Roman", 12))
    entry_e_mail_edycja = Entry(frame_dane, font=("Times New Roman", 12), relief=GROOVE)
    label_nr_tel_edycja = Label(frame_dane, text="Nr tel.:", font=("Times New Roman", 12))
    entry_nr_tel_edycja = Entry(frame_dane, font=("Times New Roman", 12), relief=GROOVE, width=9)

    imie = entry_imie_edycja
    nazwisko = entry_nazwisko_edycja
    miasto = entry_miasto_edycja
    kod = entry_kod_pocztowy_edycja
    ulica = entry_ulica_edycja
    dom = entry_nr_domu_edycja
    mieszkanie = entry_nr_mieszkania_edycja
    email = entry_e_mail_edycja
    tel = entry_nr_tel_edycja

    button_aktualizuj = Button(frame_dane, text="AKTUALIZUJ", font=("Times New Roman", 12),
                               command=lambda:aktualizuj(imie,nazwisko,miasto,kod,ulica,dom,mieszkanie,email,tel, id))

    frame_dane.grid(row=1, column=1, columnspan=2, padx=5, pady=5)
    label_imie_edycja.grid(row=0, column=1, pady=10, padx=5, sticky=W)
    entry_imie_edycja.grid(row=0, column=2, pady=10, padx=5, sticky=W)
    label_nazwisko_edycja.grid(row=1, column=1, pady=10, padx=5, sticky=W)
    entry_nazwisko_edycja.grid(row=1, column=2, pady=10, padx=5, sticky=W)
    label_miasto_edycja.grid(row=2, column=1, pady=10, padx=5, sticky=W)
    entry_miasto_edycja.grid(row=2, column=2, pady=10, padx=5, sticky=W)
    label_kod_pocztowy_edycja.grid(row=3, column=1, pady=10, padx=5, sticky=W)
    entry_kod_pocztowy_edycja.grid(row=3, column=2, pady=10, padx=5, sticky=W)
    label_ulica_edycja.grid(row=4, column=1, pady=10, padx=5, sticky=W)
    entry_ulica_edycja.grid(row=4, column=2, pady=10, padx=5, sticky=W)
    label_nr_domu_edycja.grid(row=5, column=1, pady=10, padx=5, sticky=W)
    entry_nr_domu_edycja.grid(row=5, column=2, pady=10, padx=5, sticky=W)
    label_nr_mieszkania_edycja.grid(row=6, column=1, pady=10, padx=5, sticky=W)
    entry_nr_mieszkania_edycja.grid(row=6, column=2, pady=10, padx=5, sticky=W)
    label_e_mail_edycja.grid(row=7, column=1, pady=10, padx=5, sticky=W)
    entry_e_mail_edycja.grid(row=7, column=2, pady=10, padx=5, sticky=W)
    label_nr_tel_edycja.grid(row=8, column=1, pady=10, padx=5, sticky=W)
    entry_nr_tel_edycja.grid(row=8, column=2, pady=10, padx=5, sticky=W)
    button_aktualizuj.grid(row=9, column=3, padx=5, pady=5)

    for rekord in rekordy:
        entry_imie_edycja.insert(0, rekord[0])
        entry_nazwisko_edycja.insert(0, rekord[1])
        entry_miasto_edycja.insert(0, rekord[2])
        entry_kod_pocztowy_edycja.insert(0, rekord[3])
        entry_ulica_edycja.insert(0, rekord[4])
        entry_nr_domu_edycja.insert(0, rekord[5])
        entry_nr_mieszkania_edycja.insert(0, rekord[6])
        entry_e_mail_edycja.insert(0, rekord[7])
        entry_nr_tel_edycja.insert(0, rekord[8])

def okno_aktualizacji_rekordu_wskaz():
    """Funkcja pozwalająca na wyszukanie danych po wprowadzonym identyfikatorze"""
    okno_aktualizacji = Toplevel()
    okno_aktualizacji.title("Aktualizacja rekordu")
    frame_wskaz_rekord = LabelFrame(okno_aktualizacji, text="Wskaż identyfikator aktualizowanego rekordu:")
    label_id = Label(frame_wskaz_rekord, text="Identyfikator:", font=("Times New Roman", 12))
    entry_id = Entry(frame_wskaz_rekord, font=("Times New Roman", 12), relief=GROOVE)
    id=entry_id
    button_szukaj = Button(frame_wskaz_rekord, text="SZUKAJ", font=("Times New Roman", 12),
                           command=lambda: okno_aktualizacji_rekordu_wypelnij(id, okno_aktualizacji))
    button_zamknij = Button(okno_aktualizacji, text="ZAMKNIJ", font=("Times New Roman", 12),
                           command=okno_aktualizacji.destroy)
    frame_wskaz_rekord.grid(row=0, column=1, columnspan=2, padx=5, pady=5)
    label_id.grid(row=0, column=0)
    entry_id.grid(row=0, column=1)
    button_szukaj.grid(row=1, column=1, padx=5, pady=5)
    button_zamknij.grid(row=2, column=1, padx=5, pady=5, sticky=E)

def okno_usuwania_rekordu():
    """Funkcja tworząca okno, pozwalające na wprowadzenie id rekordu, a następnie wywołanie funkcji, która usunie go z bazy danych"""
    okno_usuwania = Toplevel()
    okno_usuwania.title("Usuwanie rekordu z bazy klientów")
    label_info = Label(okno_usuwania, text="Wprowadź identyfikator usuwanego klienta:",
                       font=("Times New Roman", 14, "bold italic"))
    entry_rekord_id = Entry(okno_usuwania, font=("Times New Roman", 12), relief=GROOVE)
    rekord_id = entry_rekord_id
    button_zamknij = Button(okno_usuwania, text="ZAMKNIJ", font=("Times New Roman", 12), command=okno_usuwania.destroy)
    button_usun_rekord = Button(okno_usuwania,text="USUŃ", font=("Times New Roman", 12),
                                command=lambda: potwierdz(rekord_id))
    label_info.grid(row=0, column=1, padx=10, pady=10)
    entry_rekord_id.grid(row=1, column=1)
    button_zamknij.grid(row=2, column=0, padx=5, pady=5)
    button_usun_rekord.grid(row=2, column=2, padx=5, pady=5)

    reg_liczbowa = root.register(wprowadzana_liczbowa)
    entry_rekord_id.config(validate="key", validatecommand=(reg_liczbowa, '%P'))

def okno_wprowadzania_rekordu():
    """Funkcja tworząca okno, pozwalające na wprowadzenie danych nowego klienta, a następnie wywołująca funkcję wprowadzania do bazy"""

    okno_wprowadzania = Toplevel()
    okno_wprowadzania.title("Wprowadzanie nowego klienta do bazy")
    label_info = Label(okno_wprowadzania, text="Wprowadź dane nowego klienta:",
                       font=("Times New Roman", 14, "bold italic"))
    label_imie = Label(okno_wprowadzania, text="Imię:", font=("Times New Roman", 12))
    entry_imie = Entry(okno_wprowadzania, font=("Times New Roman", 12), relief=GROOVE)
    label_nazwisko = Label(okno_wprowadzania, text="Nazwisko:", font=("Times New Roman", 12))
    entry_nazwisko = Entry(okno_wprowadzania, font=("Times New Roman", 12), relief=GROOVE)
    label_miasto = Label(okno_wprowadzania, text="Miasto:", font=("Times New Roman", 12))
    entry_miasto = Entry(okno_wprowadzania, font=("Times New Roman", 12), relief=GROOVE)
    label_kod_pocztowy = Label(okno_wprowadzania, text="Kod pocztowy:", font=("Times New Roman", 12))
    entry_kod_pocztowy_1 = Entry(okno_wprowadzania, font=("Times New Roman", 12), relief=GROOVE, widt=2)
    label_lacznik_kod = Label(okno_wprowadzania,text="-", font=("Times New Roman", 12))
    etry_kod_pocztowy_2  = Entry(okno_wprowadzania, font=("Times New Roman", 12), relief=GROOVE, width=3)
    label_ulica = Label(okno_wprowadzania, text="Ulica:", font=("Times New Roman", 12))
    entry_ulica = Entry(okno_wprowadzania, font=("Times New Roman", 12), relief=GROOVE)
    label_nr_domu = Label(okno_wprowadzania, text="Nr domu:", font=("Times New Roman", 12))
    entry_nr_domu= Entry(okno_wprowadzania, font=("Times New Roman", 12), relief=GROOVE, width=5)
    label_nr_mieszkania = Label(okno_wprowadzania, text="Nr mieszkania:", font=("Times New Roman", 12))
    entry_nr_mieszkania = Entry(okno_wprowadzania, font=("Times New Roman", 12), relief=GROOVE, width=5)
    label_e_mail = Label(okno_wprowadzania, text="E-mail:", font=("Times New Roman", 12))
    entry_e_mail  = Entry(okno_wprowadzania, font=("Times New Roman", 12), relief=GROOVE)
    label_nr_tel = Label(okno_wprowadzania, text="Nr tel.:", font=("Times New Roman", 12))
    entry_nr_tel  = Entry(okno_wprowadzania, font=("Times New Roman", 12), relief=GROOVE, width=9)

    reg_liczbowa = root.register(wprowadzana_liczbowa)
    reg_tekstowa = root.register(wprowadzana_tekstowa)

    entry_nr_tel.config(validate="key", validatecommand=(reg_liczbowa, '%P'))
    entry_imie.config(validate="key", validatecommand=(reg_tekstowa, '%P'))
    entry_kod_pocztowy_1.config(validate="key", validatecommand=(reg_liczbowa, '%P'))
    etry_kod_pocztowy_2.config(validate="key", validatecommand=(reg_liczbowa, '%P'))
    entry_nazwisko.config(validate="key", validatecommand=(reg_tekstowa, '%P'))
    entry_miasto.config(validate="key", validatecommand=(reg_tekstowa, '%P'))

    imie = entry_imie
    nazwisko = entry_nazwisko
    miasto = entry_miasto
    kod_1 = entry_kod_pocztowy_1
    kod_2 = etry_kod_pocztowy_2
    ulica = entry_ulica
    dom = entry_nr_domu
    mieszkanie = entry_nr_mieszkania
    email = entry_e_mail
    tel = entry_nr_tel

    button_zamknij =  Button(okno_wprowadzania, text="ZAMKNIJ", font=("Times New Roman", 12),
                            command=okno_wprowadzania.destroy)
    button_wyczysc = Button(okno_wprowadzania, text="WYCZYSĆ", font=("Times New Roman", 12),
                            command=lambda:wyczysc(imie, nazwisko, miasto, kod_1, kod_2, ulica, dom,
                                                   mieszkanie, email, tel))
    button_dodaj= Button(okno_wprowadzania, text="DODAJ", font=("Times New Roman", 12),
                         command=lambda: dodaj_klienta(imie, nazwisko, miasto, kod_1, kod_2, ulica, dom,
                                                 mieszkanie, email, tel))

    label_info.grid(row=0, column=1, columnspan=5, pady=10)
    label_imie.grid(row=1, column=1, pady=10, padx=5, sticky=W)
    entry_imie.grid(row=1, column=2, pady=10, padx=5, sticky=W, columnspan=3)
    label_nazwisko.grid(row=2, column=1, pady=10, padx=5, sticky=W)
    entry_nazwisko.grid(row=2, column=2, pady=10, padx=5, sticky=W, columnspan=3)
    label_miasto.grid(row=3, column=1, pady=10, padx=5, sticky=W)
    entry_miasto.grid(row=3, column=2, pady=10, padx=5, sticky=W, columnspan=3)
    label_kod_pocztowy.grid(row=4, column=1, pady=10, padx=5, sticky=W)
    entry_kod_pocztowy_1.grid(row=4, column=2, pady=10, padx=5, sticky=W)
    label_lacznik_kod.grid(row=4, column=3, pady=10, sticky=W)
    etry_kod_pocztowy_2.grid(row=4, column=4, pady=10, sticky=W)
    label_ulica.grid(row=5, column=1, pady=10, padx=5, sticky=W)
    entry_ulica.grid(row=5, column=2, pady=10, padx=5, sticky=W, columnspan=3)
    label_nr_domu.grid(row=6, column=1, pady=10, padx=5, sticky=W)
    entry_nr_domu.grid(row=6, column=2, pady=10, padx=5, sticky=W, columnspan=3)
    label_nr_mieszkania.grid(row=7, column=1, pady=10, padx=5, sticky=W)
    entry_nr_mieszkania.grid(row=7, column=2, pady=10, padx=5, sticky=W, columnspan=3)
    label_e_mail.grid(row=8, column=1, pady=10, padx=5, sticky=W)
    entry_e_mail.grid(row=8, column=2, pady=10, padx=5, sticky=W, columnspan=3)
    label_nr_tel.grid(row=9, column=1, pady=10, padx=5, sticky=W)
    entry_nr_tel.grid(row=9, column=2, pady=10, padx=5, sticky=W, columnspan=3)
    button_zamknij.grid(row=10, column=0, pady=5, padx=10, sticky=W)
    button_wyczysc.grid(row=10, column=5, pady=5, padx=10)
    button_dodaj.grid(row=10, column=6, pady=5, padx=10, sticky=E)

def rejestracja_w_bazie(pole_login, pole_haslo, pole_potw_haslo, okno):
    """Funkcja weryfikująca poprawność danych wprowadzonych podczas rejestracji i umieszczająca je w bazie logowania"""
    login = pole_login.get()
    haslo = pole_haslo.get()
    potw_haslo = pole_potw_haslo.get()
    if haslo == "" or login== "" or potw_haslo == "":
        messagebox.showinfo("BŁĄD!", "Żadne z pól nie może być puste!")
    elif haslo == potw_haslo:
        baza_logowania = sqlite3.connect("baza_logowania.db")
        kursor_logowania = baza_logowania.cursor()
        kursor_logowania.execute("INSERT INTO baza_logowania VALUES (:login, :password)",
                                 {'login': login,
                                  'password': haslo})
        baza_logowania.commit()
        messagebox.showinfo("SUKCES!", "Użytkownik został zarejestrowany!" )
    else:
        messagebox.showinfo("BŁĄD!", "Pola 'hasło' i 'potwierdź hasło' nie są takie same!")

def okno_zarejestruj():
    """Funkcja tworząca okno pozwalające na wprowadzenie danych nowego użytkownika i wywołująca funkcję rejestracji w bazie."""
    okno_rejestracji = Toplevel()
    okno_rejestracji.title("Zarejestruj nowego użytkownika")
    label_rejestracja = Label(okno_rejestracji, text="Rejestracja", font=("Times New Roman", 14, "bold italic"))
    label_login = Label(okno_rejestracji, text="Wprowadź login:", font=("Times New Roman", 12))
    entry_login = Entry(okno_rejestracji, font=("Times New Roman", 12), relief=GROOVE)
    label_password= Label(okno_rejestracji, text="Wprowadź hasło:", font=("Times New Roman", 12))
    entry_password= Entry(okno_rejestracji, font=("Times New Roman", 12), relief=GROOVE, show="*")
    label_potwierdz_pass=Label(okno_rejestracji, text="Potwierdź hasło:", font=("Times New Roman", 12))
    entry_potwierdz_pass = Entry(okno_rejestracji, font=("Times New Roman", 12), relief=GROOVE, show="*")
    login = entry_login
    password = entry_password
    pot_password = entry_potwierdz_pass
    button_zarejestruj = Button(okno_rejestracji,text="ZAREJESTRUJ", font=("Times New Roman", 12),
                                command=lambda:rejestracja_w_bazie(login, password, pot_password, okno_rejestracji))
    button_zamknij = Button(okno_rejestracji, text="ZAMKNIJ", font=("Times New Roman", 12),
                            command=okno_rejestracji.destroy)

    label_rejestracja.grid(row=0, column=0, columnspan=3, pady=10)
    label_login.grid(row=1, column=0, pady=10, padx=5)
    entry_login.grid(row=1, column=1, pady=10, padx=5)
    label_password.grid(row=2, column=0, pady=10, padx=5)
    entry_password.grid(row=2, column=1, pady=10, padx=5)
    label_potwierdz_pass.grid(row=3, column=0, pady=10, padx=5)
    entry_potwierdz_pass.grid(row=3, column=1, pady=10, padx=5)
    button_zarejestruj.grid(row=4, column=1, sticky=E, pady=5, padx=5)
    button_zamknij.grid(row=4, column=0, sticky=W, pady=5, padx=5)

def okno_glowne_udane_log(ramka):
    """Funkcja niszcząca ramkę logowania i zastępująca ją ramką z menu głównym, po udanej weryfikacji loginu i hasłą."""
    ramka.destroy()

    ramka_okno_glowne_menu = LabelFrame(root)
    label_info_ogolne = Label(ramka_okno_glowne_menu,
                              text="Witaj,\n"
                                   "w bazie danych zawierającej rekordy klientów.\n"
                                   "Pozwala ona na zarejestrowanie nowego użytkownika,\n"
                                   "szukanie rekordów klientów w bazie, ich modyfikację oraz usuwanie. \n"
                                   "Wybierz co chcesz zrobić:", font=("Times New Roman", 14), justify=CENTER)
    button_zarejestruj = Button(ramka_okno_glowne_menu, text="Zarejestruj nowego użytkownika",
                                font=("Times New Roman", 12), command=okno_zarejestruj)
    button_szukaj = Button(ramka_okno_glowne_menu, text="Szukaj rekordu w bazie", font=("Times New Roman", 12),
                           command=okno_szukania_rekordu)
    button_wprowadz = Button(ramka_okno_glowne_menu, text="Wprowadź nowy rekord", font=("Times New Roman", 12),
                             command=okno_wprowadzania_rekordu)
    button_zaktualizuj = Button(ramka_okno_glowne_menu, text="Zaktualizuj rekord", font=("Times New Roman", 12),
                                command=okno_aktualizacji_rekordu_wskaz)
    button_usun = Button(ramka_okno_glowne_menu, text="Usuń rekord z bazy", font=("Times New Roman", 12),
                         command=okno_usuwania_rekordu)
    button_zamknij = Button(ramka_okno_glowne_menu, text="ZAMKNIJ", font=("Times New Roman", 12), command=root.quit)
    ramka_okno_glowne_menu.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    label_info_ogolne.grid(row=0, column=0, columnspan=3, pady=20)
    button_zarejestruj.grid(row=1, column=1,pady=10, ipadx=150, ipady=5)
    button_szukaj.grid(row=2, column=1,pady=10, ipadx=176, ipady=5)
    button_wprowadz.grid(row=3, column=1,pady=10, ipadx=173, ipady=5)
    button_zaktualizuj.grid(row=4, column=1,pady=10, ipadx=193, ipady=5)
    button_usun.grid(row=5, column=1,pady=10, ipadx=190, ipady=5)
    button_zamknij.grid(row=6, column=1,pady=10, sticky=E)

def weryfikacja_danych(login, password, ramka):
    sprawdx_login=login.get()
    sprawdz_password=password.get()
    baza_logowania = sqlite3.connect("baza_logowania.db")
    kursor_logowania = baza_logowania.cursor()
    kursor_logowania.execute('SELECT * FROM baza_logowania WHERE login = ? AND password = ?',(sprawdx_login, sprawdz_password))
    baza_logowania.commit()
    if kursor_logowania.fetchall():
        okno_glowne_udane_log(ramka)
    else:
        messagebox.showerror("Błąd logowania!", "Wprowadzony login lub hasło są nieprawidłowe!")
        login.delete(0, END)
        password.delete(0, END)

def okno_glowne_logowanie():
    """Okno z ramką żądającą od użytkowanika danych do weryfikacji, po ich uzyskaniu i sprawdzeniu poprawności, wywołuje ramkę
    z oknem głównym programu"""
    global root
    root = Tk()
    root.title("Baza klientów")

    ramka_log = LabelFrame(root, padx=5, pady=5)
    label_wprowadz = Label(ramka_log, text="Wprowadź dane logowania:", font=("Times New Roman", 12, "bold italic"),
                           justify=CENTER)
    label_login = Label(ramka_log, text="Login:", font=("Times New Roman", 12))
    entry_login = Entry(ramka_log, relief=GROOVE, font=("Times New Roman", 12))
    label_password = Label(ramka_log, text="Hasło:", font=("Times New Roman", 12))
    entry_password = Entry(ramka_log, relief=GROOVE, font=("Times New Roman", 12), show='*')
    button_zamknij = Button(ramka_log, text="ZAMKNIJ", font=("Times New Roman", 10), command=root.quit)

    button_zaloguj = Button(ramka_log, text="ZALOGUJ", font=("Times New Roman", 10),
                            command=lambda: weryfikacja_danych(entry_login, entry_password, ramka_log))
    ramka_log.grid(row=0, column=0)
    label_wprowadz.grid(row=0, column=0,columnspan=2, padx=60, pady=10)
    label_login.grid(row=1, column=0)
    label_password.grid(row=2, column=0)
    entry_login.grid(row=1, column=1)
    entry_password.grid(row=2, column=1)
    button_zamknij.grid(row=3, column=0, pady=10)
    button_zaloguj.grid(row=3, column=1, pady=10)

if __name__ == "__main__":
    okno_glowne_logowanie()
    root.mainloop()