import random, os
print("Witaj w Generatorze Postaci v1!\nWybierz imię dla swojej postaci nim przejdziemy dalej:")
lista_ras = ["elf", "człowiek", "krasnolud"]
lista_klas = ["wojownik", "strzelec", "mag"]
cechy_postaci = {"Zręczność":5,"Siła":5, "Intelekt":5}
dostepny_orez = {"wojownik":("miecz", "topór"), "strzelec":("łuk", "kusza"), "mag":("kostur")}
nazwa_postaci = input()
class ZlyWyborException(Exception):
    def __init__(self, wprowadzana):
        super().__init__("Wprowadzona treść: {}, nie jest jedną z opcji do wyboru".format(wprowadzana))
class ZlyTypDamychException(Exception):
    def __init__(self, wprowadzana):
        super().__init__("Wprowadzone dane \"{}\" nie są danymi tekstowymi!".format(wprowadzana))
def wybor_rasy():
    print("Pierwszym krokiem do stworzenia Twojej postaci będzie wybór jednej z 3 ras\n(krasnoluda, elfa lub człowieka). By tego"
          "dokonać wpisz nazwę rasy:")
    wprowadzana = input().lower()
    if type(wprowadzana) != str:
        raise ZlyTypDamychException(wprowadzana)
    elif wprowadzana in lista_ras:
        return wprowadzana
    else:
        raise ZlyWyborException(wprowadzana)
wybrana_rasa = wybor_rasy()
print(wybrana_rasa)
def wybor_klasy():
    print("Czas byś wybrał klasę dla swojej postaci. Tak jak poprzednio do wyboru masz 3 opcje {}".format(lista_klas))
    wprowadzana = input().lower()
    if type(wprowadzana) != str:
        raise ZlyTypDamychException(wprowadzana)
    elif wprowadzana in lista_klas:
        return wprowadzana
    else:
        raise ZlyWyborException(wprowadzana)
wybrana_klasa = wybor_klasy()
print("Początkowe wartości cech postaci wynoszą: {}. Jednakże teraz nastąpi ich dostosowanie do podjętych przez ciebie wyborów.".format(cechy_postaci))
def wybor_oreza():
    if wybrana_klasa == "wojownik":
        print("Jako wojownik możesz dzierżyć miecz lub topór. Co wybierasz?")
        wprowadzana = input()
        if type(wprowadzana) != str:
            raise ZlyTypDamychException(wprowadzana)
        elif wprowadzana in dostepny_orez[wybrana_klasa]:
            return wprowadzana
        else:
            raise ZlyWyborException(wprowadzana)
    elif wybrana_klasa == "strzelec":
        print("Jako wojownik możesz dzierżyć łuk lub kuszę. Co wybierasz?")
        wprowadzana = input()
        if type(wprowadzana) != str:
            raise ZlyTypDamychException(wprowadzana)
        elif wprowadzana in dostepny_orez[wybrana_klasa]:
            return wprowadzana
        else:
            raise ZlyWyborException(wprowadzana)
    else:
        print("Jako mag możesz dzierżyć wyłącznie kostur")
        return "kostur"
wybrany_orez = wybor_oreza()
class PrzypisanieCech():
    """Klasa zmieniająca cechy tworzonej postaci ze względu na podjęte w kreatorze decyzje"""
    def przypisanie_cech_rasowych(self):
        if wybrana_rasa == "krasnolud":
            cechy_postaci["Siła"] += 3
            cechy_postaci["Zręczność"] -= 3
            cechy_postaci["Intelekt"] -= 1
        elif wybrana_rasa == "elf":
            cechy_postaci["Zręczność"] += 1
            cechy_postaci["Intelekt"] += 2
        else:
            cechy_postaci["Siła"] -= 1
            cechy_postaci["Intelekt"] -= 1
    def przypisanie_cech_klasowych(self):
        if wybrana_klasa == "wojownik":
            cechy_postaci["Siła"] += 2
            cechy_postaci["Intelekt"] -= 3
        elif wybrana_klasa == "strzelec":
            cechy_postaci["Siła"] -= 1
            cechy_postaci["Zręczność"] += 2
            cechy_postaci["Intelekt"] -= 1
        else:
            cechy_postaci["Siła"] -= 2
            cechy_postaci["Zręczność"] -= 1
            cechy_postaci["Intelekt"] += 3
    def przypisanie_cechy_dominujacej(self):
        if wybrana_klasa == "wojownik":
            cecha_dominujaca = cechy_postaci["Siła"]
            return cecha_dominujaca
        elif wybrana_klasa == "strzelec":
            cecha_dominujaca = cechy_postaci["Zręczność"]
            return cecha_dominujaca
        else:
            cecha_dominujaca = cechy_postaci["Intelekt"]
            return cecha_dominujaca
    def przypisanie_wartosci_oreza(self):
        sila_ataku = random.randint(1, 10) + round((cecha_dominujaca / 2), 1)
        return  sila_ataku
    def ilosc_pkt_zycia(self):
        b = cechy_postaci["Siła"] * 10 + 100
        pkt_zycia = random.randint(100, b)
        return  pkt_zycia
    def ilosc_pkt_many(self):
        b = cechy_postaci["Intelekt"] * 10 + 100
        pkt_many = random.randint(100, b)
        return  pkt_many
    def ilosc_pkt_kondycji(self):
        b = cechy_postaci["Zręczność"] * 10 + 100
        pkt_kondycji = random.randint(100, b)
        return  pkt_kondycji
modyfikacja_cech = PrzypisanieCech()
modyfikacja_cech.przypisanie_cech_klasowych()
modyfikacja_cech.przypisanie_cech_rasowych()
cecha_dominujaca = modyfikacja_cech.przypisanie_cechy_dominujacej()
atak = modyfikacja_cech.przypisanie_wartosci_oreza()
zycie = modyfikacja_cech.ilosc_pkt_zycia()
mana = modyfikacja_cech.ilosc_pkt_many()
kondycja = modyfikacja_cech.ilosc_pkt_kondycji()
print("Obecne cechy Twojej postaci to: {}".format(cechy_postaci))
print(modyfikacja_cech.przypisanie_wartosci_oreza())
"""postac = {"imię":nazwa_postaci,
          "rasa":wybrana_rasa,
          "klasa":wybrana_klasa,
          "statystki": {"ilość punktów życia": zycie,
                        "ilość punktów many": mana,
                        "ilość punktów ataku": atak,},
          "broń":wybrany_orez,
          "cechy": cechy_postaci}"""
statystki = {"ilość punktów życia": zycie, "ilość punktów many": mana,"ilość punktów ataku": atak,}
def historia():
    print("Czy chcesz wprowadzić własną historię dla swojej postaci? T/N")
    wprowadzana = input().upper()
    if type(wprowadzana) != str:
        raise ZlyTypDamychException(wprowadzana)
    elif wprowadzana == "T":
        print("Wpisz swoją historię:")
        historia = input()
        return  historia
    elif wprowadzana == "N":
        historia = "Historia tej postaci nie została nigdy zapisana"
        return historia
    else:
        raise ZlyWyborException(wprowadzana)
zyciorys = historia()
def zapis_postaci():
    print("Czy chcesz zapisać swoją postać? T/N")
    wprowadzana = input().upper()
    if type(wprowadzana) != str:
        raise ZlyTypDamychException(wprowadzana)
    elif wprowadzana == "T":
        zapis_do_folderu()
    elif wprowadzana == "N":
        pass
    else:
        raise ZlyWyborException(wprowadzana)
def zapis_do_folderu():
    path = "Utworzone postacie/{}/{}.txt ".format(nazwa_postaci,nazwa_postaci)
    dir_path = os.path.dirname(path)
    os.makedirs(dir_path)
    plik = open(path, "a+")
    plik.write( "DANE POSTACI:\nImię: {}\nRasa: {}\nKlasa: {}\nCechy postaci:\n\tZręczność: {}\n\tSiła: {}\n\tIntelekt: {}\nStatystyki:\n\tŻycie: {}\n\tMana: {}\n\tAtak: {}\nHistoria:\n{}".format(nazwa_postaci, wybrana_rasa, wybrana_rasa, cechy_postaci["Zręczność"],cechy_postaci["Siła"], cechy_postaci["Intelekt"], statystki["ilość punktów życia"], statystki["ilość punktów many"], statystki["ilość punktów ataku"], zyciorys))
    plik.close()
zapis_postaci()
