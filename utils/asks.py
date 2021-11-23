from datetime import date, datetime
from typing import List


def ask_integer(name: str, min_value: int, max_value: int):
    """ Fonction qui a en paramètre deux valeur une min_value et une max_value
    et une autre taper par l'utilisateur et cette valeur doit rester entre
    min_value et max_value  """
    while True:
        try:
            value = int(input(f"{name} ? "))
            if min_value <= value <= max_value:
                return value
            print(f"Entrez un entier entre {min_value} et {max_value} ")
        except ValueError:
            pass


def ask_string(name: str, min_len: int, max_len: int):
    """ Fonction qui a en paramètre deux valeur min_value et une max_value
    et un autre taper par l'utilisateur qui est une valeur string.
    La Fonction calcule la taille du nom et doit être entre min_value
    et une max_value """
    while True:
        string = input(f"{name} ? ")
        if min_len <= len(string) <= max_len:
            return string
        print(f"Entrez une chaine de caractère dont la"
              f"taille est comprise entre {min_len} et {max_len}")


def ask_choice(name: str, choices: List[str]):
    """ Fonction qui a en paramètre une liste de string
    l'utilisateur entre une valeur qui doit correspondre
    a l'une des string de la liste (Gender)"""

    while True:
        choice = input(f"{name} ({', '.join(choices)}) ? ")
        if choice in choices:
            return choice


def ask_date(name: str):
    """ Fonction vérifie si la date est bien dans les norme c'est à dire
    tant que la date rentré n'est pas dans ce format l'utilisateur doit
    répeter la manoeuvre YYYY-MM-DD """

    while True:
        try:
            year = int(input(f"{name} ?, Année ? "))
            month = int(input("Mois ? "))
            day = int(input("Jour ? "))
            return date(year=year, month=month, day=day)
        except ValueError:
            pass


def ask_datetime(name: str):
    """ Fonction identique avec les Heures et minute en +
    YYYY-MM-DD HH:mm """
    while True:
        try:
            year = int(input(f"{name} ?, Année ? "))
            month = int(input("Mois ? "))
            day = int(input("Jour ? "))
            hour = int(input("Heure ? "))
            minute = int(input("Minute ?"))
            return datetime(
                year=year, month=month, day=day, hour=hour, minute=minute)
        except ValueError:
            pass


def ask_number(name: str):
    """ Fonction qui vérifie si la variable est un int"""

    while True:
        try:
            number = int(input(f'{name} ?'))
            return number
        except ValueError:
            pass


def resultat(p1_resultat):    
    """ Fonction qui affiche la liste des matchs et leurs
    résultats"""
    i = 0
    Turn = 0
    table = [1, 5, 9, 13]
    for (pid1, p1_result), (p1, p2) in p1_resultat:
        i += 1
        if i in table:
            Turn += 1
            print("Résultat du tour",  Turn)
        if p1_result == 1:
            print(f"Le joueur {p1} a gagner ")
        if p1_result == 0.5:
            print(f"Match nul entre {p1} et {p2} ")
        if p1_result == 0:
            print(f"le joueur {p2} a gagner ")
    
