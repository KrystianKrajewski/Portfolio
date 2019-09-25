
fridge_contenr =  {'jajka': 1, 'mleko': 1, 'ser gouda': 1, 'ser pleśniowy': 1,
'serek topiony': 1, 'polędwica sopocka': 1, ' kiełbasa podwawelska': 1, 'boczek wędzony': 1, 'musztarda': 1, "majonez": 1}
products_list = list(fridge_contenr.keys())
number_category = 10

class YNDecisionException(Exception):

    def __init__(self):
        super().__init__('Decyzję należy podjąć wprowadzająć T lub N!')

class ValueException(Exception):

    def __init__(self):
        super().__init__('Dostępnym opcją odpowiadają liczby od 1 do 5. Podana wartość nie mieści się w tym zakresie!')

class typeNotStrException(Exception):

    def __init__(self):
        super().__init__('Nazwę productu należy wprowadzić za postrengthą liter!')

class Management():

    def search_product(self, product):
        if product in fridge_contenr:
            print('W lodówce jest następująca ilość {}: {}'.format(product, fridge_contenr[product]))
        else:
            print('Brak {} w lodówce'.format(product))
    def add_singe_product(self, product, quantity):
            fridge_contenr[product] =+ quantity
    def subtract_singe_product(self, product, quantity):
        if product in fridge_contenr:
            if fridge_contenr[product] >= quantity:
                fridge_contenr[product] = fridge_contenr[product] - quantity
                return fridge_contenr
            else:
                print('za mało productow')
        else:
            print('brak productu w lodówce lub jego ilość jest niewystarczająca!')
    def endig_products(self, minimal):
        counter = 0
        while counter != number_category:
            product = products_list[counter]
            if fridge_contenr[product] < minimal:
                print("{} kończy się. Trzeba dokupić!".format(product))
            counter += 1

managment = Management



print('Witaj w zarządzaniu lodówką. Do chooseu masz jedną z 4 opcji. \n'
          'Jeśli chcesz checkić obecność productu w lodówce wciśnij 1. \n'
          'Jeśli chcesz dołożyć product do lodówki wyciśnij 2 \n'
          'Jeśli chcesz wyjąć product z lodówki wciśnij 3 \n'
          'Jeśli chcesz checkić kończące się producty wciśnij 4 \n'
          'Jeśli chcesz checkić zawartość lodówki wciśnij 5 \n'
          'Jeśli chcesz wyjść wciśnij 6 \n'
          'Swój wybór zatwierdź wciskając ENTER')

choose = int(input())

if choose >= 1 <= 5:
    if choose == 1:
        print('Wprowadź nazwę productu, który chcesz znaleźć:')
        wanted = input().lower()
        if type(wanted) != str:
            raise typeNotStrException()
        else:
            managment.search_product(managment, wanted)
    elif choose == 2:
        print('Wprowadź nazwę productu, który chcesz wprowadzić:')
        entry = input().lower()
        if type(entry) != str:
            raise typeNotStrException()
        elif entry in fridge_contenr:
            print('Wprowadź ilość {} umieszczanych w lodówce'.format(entry))
            entry_quantity = int(input())
            managment.add_singe_product(managment, entry, entry_quantity)
        else:
            print('Nie znaleziono {} w bazie productow. Czy chcesz go dodać? T/N'.format(entry))
            decision = input().upper()
            if type(decision) != str:
                raise typeNotStrException
            elif decision == 'N':
                pass
            elif decision == 'T':
                print('Wprowadź ilość {} umieszczanych w lodówce'.format(entry))
                entry_quantity = int(input())
                managment.add_singe_product(managment, entry, entry_quantity)
                number_category = number_category + 1
                print(number_category)
            else:
                raise YNDecisionException
    elif choose == 3:
        print('Wprowadź nazwę productu, który chcesz wyjąć:')
        removable = input().lower()
        if type(removable) != str:
            raise typeNotStrException()
        else:
            print('Wprowadź ilość {}, którą chcesz wyjąć:'.format(removable))
            removable_quantity = int(input())
            managment.subtract_singe_product(managment, removable, removable_quantity)
    elif choose == 4:
        print('Czy chcesz wprowadzić minimalną ilość productów? T/N')
        decision = input().upper()
        if type(decision) != str:
            raise typeNotStrException
        elif decision != 'T' or 'N':
            raise YNDecisionException
        elif decision == 'T':
            value_min = int(input())
        else:
            value_min = 3
        managment.endig_products(managment, value_min)
    elif choose == 5:
        print(fridge_contenr)
    else:
        raise ValueException()

