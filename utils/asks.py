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

def select_identifiant():
    """ Fonction pour sélectioner un tournois arréter """

    print("Sélection d'indentifiant")
    return {
       "id": ask_integer("identifiant ?", 1, 200)
    }


def edit_rank():
    """Fonction pour modifier le rang aprés la fin d'un tournois"""
    print("Modification de rang")
    return {
        "rank": ask_integer("Rang", 1, 3000)
    }
