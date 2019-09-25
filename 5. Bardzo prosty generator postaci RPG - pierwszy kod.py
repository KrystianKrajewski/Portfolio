import random, os
print("Witaj w Generatorze Postaci v1!\nWybierz imię dla swojej postaci nim przejdziemy dalej:")
race_list = ["elf", "człowiek", "krasnolud"]
clas_list = ["wojownik", "strzelec", "mag"]
char_traits = {"Zręczność":5,"Siła":5, "Intelekt":5}
weapons = {"wojownik":("miecz", "topór"), "strzelec":("łuk", "kusza"), "mag":("kostur")}
ch_name = input()
class WrongChoiceException(Exception):
    def __init__(self, entry):
        super().__init__("Wprowadzona treść: {}, nie jest jedną z opcji do wyboru".format(entry))
class WrongDataTypeException(Exception):
    def __init__(self, entry):
        super().__init__("Wprowadzone dane \"{}\" nie są danymi tekstowymi!".format(entry))
def race_choice():
    print("Pierwszym krokiem do stworzenia Twojej postaci będzie wybór jednej z 3 ras\n(krasnoluda, elfa lub człowieka). By tego"
          "dokonać wpisz nazwę rasy:")
    entry = input().lower()
    if type(entry) != str:
        raise WrongDataTypeException(entry)
    elif entry in race_list:
        return entry
    else:
        raise WrongChoiceException(entry)
chosen_race = race_choice()
print(chosen_race)
def clas_choice():
    print("Czas byś wybrał klasę dla swojej postaci. Tak jak poprzednio do wyboru masz 3 opcje {}".format(clas_list))
    entry = input().lower()
    if type(entry) != str:
        raise WrongDataTypeException(entry)
    elif entry in clas_list:
        return entry
    else:
        raise WrongChoiceException(entry)
chosen_clas = clas_choice()
print("Początkowe wartości cech postaci wynoszą: {}. Jednakże teraz nastąpi ich dostosowanie do podjętych przez ciebie wyborów.".format(char_traits))
def weapon_choice():
    if chosen_clas == "wojownik":
        print("Jako wojownik możesz dzierżyć miecz lub topór. Co wybierasz?")
        entry = input()
        if type(entry) != str:
            raise WrongDataTypeException(entry)
        elif entry in weapons[chosen_clas]:
            return entry
        else:
            raise WrongChoiceException(entry)
    elif chosen_clas == "strzelec":
        print("Jako wojownik możesz dzierżyć łuk lub kuszę. Co wybierasz?")
        entry = input()
        if type(entry) != str:
            raise WrongDataTypeException(entry)
        elif entry in weapons[chosen_clas]:
            return entry
        else:
            raise WrongChoiceException(entry)
    else:
        print("Jako mag możesz dzierżyć wyłącznie kostur")
        return "kostur"
chosen_weapon = weapon_choice()
class Assignement_traits():

    def assignement_traits_race(self):
        if chosen_race == "krasnolud":
            char_traits["Siła"] += 3
            char_traits["Zręczność"] -= 3
            char_traits["Intelekt"] -= 1
        elif chosen_race == "elf":
            char_traits["Zręczność"] += 1
            char_traits["Intelekt"] += 2
        else:
            char_traits["Siła"] -= 1
            char_traits["Intelekt"] -= 1
    def assignement_traits_clas(self):
        if chosen_clas == "wojownik":
            char_traits["Siła"] += 2
            char_traits["Intelekt"] -= 3
        elif chosen_clas == "strzelec":
            char_traits["Siła"] -= 1
            char_traits["Zręczność"] += 2
            char_traits["Intelekt"] -= 1
        else:
            char_traits["Siła"] -= 2
            char_traits["Zręczność"] -= 1
            char_traits["Intelekt"] += 3
    def assignement_traits_dominant(self):
        if chosen_clas == "wojownik":
            dominant = char_traits["Siła"]
            return dominant
        elif chosen_clas == "strzelec":
            dominant = char_traits["Zręczność"]
            return dominant
        else:
            dominant = char_traits["Intelekt"]
            return dominant
    def assignement_weapon_value(self):
        stregth = random.randint(1, 10) + round((dominant / 2), 1)
        return  stregth
    def health_points(self):
        b = char_traits["Siła"] * 10 + 100
        health = random.randint(100, b)
        return  health
    def mana_points(self):
        b = char_traits["Intelekt"] * 10 + 100
        mana = random.randint(100, b)
        return  mana
    def condition_points(self):
        b = char_traits["Zręczność"] * 10 + 100
        condition = random.randint(100, b)
        return  condition
modification_traits = Assignement_traits()
modification_traits.assignement_traits_clas()
modification_traits.assignement_traits_race()
dominant = modification_traits.assignement_traits_dominant()
attack = modification_traits.assignement_weapon_value()
health = modification_traits.health_points()
mana = modification_traits.mana_points()
condition = modification_traits.condition_points()
print("Obecne cechy Twojej postaci to: {}".format(char_traits))
print(modification_traits.assignement_weapon_value())
"""postac = {"imię":ch_name,
          "rasa":chosen_race,
          "klasa":chosen_clas,
          "statystyki": {"ilość punktów życia": health,
                        "ilość punktów many": mana,
                        "ilość punktów attaku": attack,},
          "broń":chosen_weapon,
          "cechy": char_traits}"""
stats = {"ilość punktów życia": health, "ilość punktów many": mana,"ilość punktów attaku": attack,}
def story():
    print("Czy chcesz wprowadzić własną historię dla swojej postaci? T/N")
    entry = input().upper()
    if type(entry) != str:
        raise WrongDataTypeException(entry)
    elif entry == "T":
        print("Wpisz swoją historię:")
        historia = input()
        return  historia
    elif entry == "N":
        historia = "Historia tej postaci nie została nigdy zapisana"
        return historia
    else:
        raise WrongChoiceException(entry)
history = story()
def save_character():
    print("Czy chcesz zapisać swoją postać? T/N")
    entry = input().upper()
    if type(entry) != str:
        raise WrongDataTypeException(entry)
    elif entry == "T":
        save_to_directory()
    elif entry == "N":
        pass
    else:
        raise WrongChoiceException(entry)
def save_to_directory():
    path = "Utworzone postacie/{}/{}.txt ".format(ch_name,ch_name)
    dir_path = os.path.dirname(path)
    os.makedirs(dir_path)
    plik = open(path, "a+")
    plik.write( "DANE POSTACI:\nImię: {}\nRasa: {}\nKlasa: {}\nCechy postaci:\n\tZręczność: {}\n\tSiła: {}\n\tIntelekt: {}\nStatystyki:\n\tŻycie: {}\n\tMana: {}\n\tattack: {}\nHistoria:\n{}".format(ch_name, chosen_race, chosen_race, char_traits["Zręczność"],char_traits["Siła"], char_traits["Intelekt"], stats["ilość punktów życia"], stats["ilość punktów many"], stats["ilość punktów attacku"], history))
    plik.close()
save_character()
