from utils.asks import (
    ask_choice, ask_date, ask_integer, ask_number, ask_string
)


def create_tournament_form():
    """ Création d'un formulaire de pour la classe Tournament  """
    print("Création de tournois")
    return {
        "name": ask_string("nom du tournois", 2, 14),
        "location": ask_string("location", 2, 14),
        "start_date": ask_date("date du tournois"),
        "turns": [],
        "time_control": ask_string("controle du temps", 2, 14),
        "description": ask_string("description", 2, 14),
        "nb_turns": ask_number("nombre de tours"),
        "numbers_players": ask_integer("nombre de joueurs", 2, 8),
        "id": ask_number("id")
    }

# def create_match():
#     return{
#         "self.player_1_id = player_1_id
#             self.player_2_id = player_2_id
#         score_1
#          score_2"
#     }

def create_player_form():
    """ Création d'un formulaire pour la classe Player """
    print("Déclaration d'un nouveau joueur")
    return {
       "first_name": ask_string("Prénom", 2, 14),
       "last_name": ask_string("Nom", 2, 14),
       "gender": ask_choice("Sexe", ["H", "F"]),
       "rank": ask_integer("Rang", 1, 3000),
       "birthdate": ask_date("Date d'anniversaire"),
       "id": ask_integer("identifiant", 1, 8)
     }


def select_identifiant():
    """ Fonction pour sélectioner un tournois arréter """

    print("Sélection d'indentifiant")
    return {
       "id": ask_integer("identifiant ?", 1, 8)
    }


def edit_rank():
    """Fonction pour modifier le rang aprés la fin d'un tournois"""
    print("Modification de rang")
    return {
        "rank": ask_integer("Rang", 1, 3000)
    }
