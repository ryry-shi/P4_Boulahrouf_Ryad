from views.menu import Menu


class MainMenu(Menu):
    """ Classe MainMenu qui hérite de la classe Menu
    Une string et une liste de tuple qui en fais un sous-Menu"""

    def __init__(self):
        super().__init__(
            "Menu principal",
            [
                ("Gérer les joueur", 1),
                ("Gérer les tournois", 2),
                ("Fin du programme", 3),
            ])
