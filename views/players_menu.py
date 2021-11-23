from views.menu import Menu


class PlayersMenu(Menu):
    """ Classe PlayersMenu qui hérite de la classe Menu
    Un string et une liste de tuple qui en fais un sous-Menu"""
    
    def __init__(self):
        super().__init__("Gérer les joueurs", [
            ("Déclarer un nouveau joueur", 1),
            ("Modifier un joueur", 2),
            ("Lister les joueurs (par nom)", 3),
            ("Lister les joueurs (par classement)", 4),
            ("Retour", 5),
        ])
