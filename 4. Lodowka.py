
zawartosc_lodowki =  {'jajka': 1, 'mleko': 1, 'ser gouda': 1, 'ser pleśniowy': 1,
'serek topiony': 1, 'polędwica sopocka': 1, ' kiełbasa podwawelska': 1, 'boczek wędzony': 1, 'musztarda': 1, "majonez": 1}
lista_produktow = list(zawartosc_lodowki.keys())
liczba_kategorii = 10

class TNDecyzjaException(Exception):

    def __init__(self):
        super().__init__('Decyzję należy podjąć wprowadzająć T lub N!')

class NiezgodnaWartoscException(Exception):

    def __init__(self):
        super().__init__('Dostępnym opcją odpowiadają liczby od 1 do 5. Podana wartość nie mieści się w tym zakresie!')

class TypNotStrException(Exception):

    def __init__(self):
        super().__init__('Nazwę produktu należy wprowadzić za pomocą liter!')

class Zarzadzanie():

    def szukanie_produktow(self, produkt):
        if produkt in zawartosc_lodowki:
            print('W lodówce jest następująca ilość {}: {}'.format(produkt, zawartosc_lodowki[produkt]))
        else:
            print('Brak {} w lodówce'.format(produkt))
    def dodawanie_poj_produktow(self, produkt, ilosc):
            zawartosc_lodowki[produkt] =+ ilosc
    def odejmowanie_poj_produktow(self, produkt, ilosc):
        if produkt in zawartosc_lodowki:
            if zawartosc_lodowki[produkt] >= ilosc:
                zawartosc_lodowki[produkt] = zawartosc_lodowki[produkt] - ilosc
                return zawartosc_lodowki
            else:
                print('za mało produktow')
        else:
            print('brak produktu w lodówce lub jego ilość jest niewystarczająca!')
    def konczace_sie_produkty(self, minimalna):
        licznik = 0
        while licznik != liczba_kategorii:
            produkt = lista_produktow[licznik]
            if zawartosc_lodowki[produkt] < minimalna:
                print("{} kończy się. Trzeba dokupić!".format(produkt))
            licznik += 1

zarzadzanie = Zarzadzanie



print('Witaj w zarządzaniu lodówką. Do wyboru masz jedną z 4 opcji. \n'
          'Jeśli chcesz sprawdzić obecność produktu w lodówce wciśnij 1. \n'
          'Jeśli chcesz dołożyć produkt do lodówki wyciśnij 2 \n'
          'Jeśli chcesz wyjąć produkt z lodówki wciśnij 3 \n'
          'Jeśli chcesz sprawdzić kończące się produkty wciśnij 4 \n'
          'Jeśli chcesz sprawdzić zawartość lodówki wciśnij 5 \n'
          'Jeśli chcesz wyjść wciśnij 6 \n'
          'Swój wybór zatwierdź wciskając ENTER')

wybor = int(input())

if wybor >= 1 <= 5:
    if wybor == 1:
        print('Wprowadź nazwę produktu, który chcesz znaleźć:')
        poszukiwany = input().lower()
        if type(poszukiwany) != str:
            raise TypNotStrException()
        else:
            zarzadzanie.szukanie_produktow(Zarzadzanie, poszukiwany)
    elif wybor == 2:
        print('Wprowadź nazwę produktu, który chcesz wprowadzić:')
        wprowadzany = input().lower()
        if type(wprowadzany) != str:
            raise TypNotStrException()
        elif wprowadzany in zawartosc_lodowki:
            print('Wprowadź ilość {} umieszczanych w lodówce'.format(wprowadzany))
            wprowadzana_ilosc = int(input())
            zarzadzanie.dodawanie_poj_produktow(Zarzadzanie, wprowadzany, wprowadzana_ilosc)
        else:
            print('Nie znaleziono {} w bazie produktow. Czy chcesz go dodać? T/N'.format(wprowadzany))
            decyzja = input().upper()
            if type(decyzja) != str:
                raise TypNotStrException
            elif decyzja == 'N':
                pass
            elif decyzja == 'T':
                print('Wprowadź ilość {} umieszczanych w lodówce'.format(wprowadzany))
                wprowadzana_ilosc = int(input())
                zarzadzanie.dodawanie_poj_produktow(Zarzadzanie, wprowadzany, wprowadzana_ilosc)
                liczba_kategorii = liczba_kategorii + 1
                print(liczba_kategorii)
            else:
                raise TNDecyzjaException
    elif wybor == 3:
        print('Wprowadź nazwę produktu, który chcesz wyjąć:')
        wyjmowany = input().lower()
        if type(wyjmowany) != str:
            raise TypNotStrException()
        else:
            print('Wprowadź ilość {}, którą chcesz wyjąć:'.format(wyjmowany))
            wyjmowana_ilosc = int(input())
            zarzadzanie.odejmowanie_poj_produktow(Zarzadzanie, wyjmowany, wyjmowana_ilosc)
    elif wybor == 4:
        print('Czy chcesz wprowadzić minimalną ilość produktów? T/N')
        decyzja = input().upper()
        if type(decyzja) != str:
            raise TypNotStrException
        elif decyzja != 'T' or 'N':
            raise TNDecyzjaException
        elif decyzja == 'T':
            wartosc_min = int(input())
        else:
            wartosc_min = 3
        zarzadzanie.konczace_sie_produkty(Zarzadzanie, wartosc_min)
    elif wybor == 5:
        print(zawartosc_lodowki)
    else:
        raise NiezgodnaWartoscException()

