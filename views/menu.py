from typing import List, Tuple, Any
from .view import View


class Menu(View):
    """Création de la classe Menu avec la fonction show pour
    afficher les menu elle servira
    de classe parent pour les autres classe_menu """

    def __init__(self, title: str, choices: List[Tuple[str, Any]]):
        super().__init__(title, "\n".join(
            [f"{nb}. {desc}" for nb, (desc, _) in enumerate(choices, start=1)]))
        self.choices = [value for _, value in choices]

    def show(self):
        """ Méthod qui permet a l'utilisateur
        d'entrer une valeur pour un menu """
        while True:
            super().show()
            try:
                choice = int(input("Entrez une valeur : ")) - 1
                if choice < 0:
                    raise IndexError
                return self.choices[choice]
            except (IndexError, ValueError):
                pass
