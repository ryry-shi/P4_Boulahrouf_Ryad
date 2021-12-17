from views.menu import Menu


class TournamentsMenu(Menu):
    """ Classe TournamentMenu qui hérite de la classe Menu
    Un string et une liste de tuple qui en fais un sous-Menu"""

    def __init__(self):
        super().__init__("Menu tournois", [
            ("Créer un tournois", 1),
            ("Reprendre un tournois", 2),
            ("Liste des tournois", 3),
            ("Rapport duel", 4),
            ("Rapport de victoire", 5),
            ("Retour", 6)
        ])
