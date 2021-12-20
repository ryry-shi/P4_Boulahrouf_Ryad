from typing import Any, List, Tuple
from models.tournament import TimeControl
from views.view import View


class Text(str):

    def __new__(cls, value, max_len=255, min_len=2):
        for p in value:
            if not isinstance(value, str) or len(value) > max_len or len(value) < min_len:
                raise ValueError()
            if isinstance(p, int):
                raise ValueError()
        return str.__new__(cls, value)


class PositiveInt(int):

    def __new__(cls, value):
        value = int(value)
        if value < 1:
            raise ValueError()
        return int.__new__(cls, value)


class Gender(str):

    def __new__(cls, value):
        value = str(value)
        if value not in ["H", "F"]:
            raise ValueError()
        return str.__new__(cls, value)


class Form(View):

    def __init__(self, title: str, fields: List[Tuple[str, str, Any]]):
        self.fields = fields
        super().__init__(title=title)

    def show(self):
        data = {}
        for field_name, field_desc, field_type in self.fields:
            while True:
                super().show()
                try:
                    data[field_name] = field_type(input(field_desc.capitalize() + " ? "))
                    break
                except ValueError:
                    pass
        return data


class CreateTournamentForm(Form):

    def __init__(self):
        # Formulaire de tournois
        super().__init__(title="Créer un tournois", fields=[
            ("name", " Prénom", Text),
            ("location", " Lieu", Text),
            ("start_date_year", " Année de début du tournoi", PositiveInt),
            ("start_date_month", "Mois de début du tournoi", PositiveInt),
            ("start_date_day", " Jour de début du tournoi", PositiveInt),
            ("time_control", " Controle du temps", TimeControl),
            ("description", " Description", Text),
            ("nb_turns", "Nombre de tours", PositiveInt),
            ("numbers_players", " Nombre de joueurs", PositiveInt),
            ("id", "Identifiant", PositiveInt)
        ])


class CreatePlayerForm(Form):

    def __init__(self):
        # Formulaire de player
        super().__init__(title="Créer un player", fields=[
            ("first_name", " Prénom", Text),
            ("last_name", " Nom du joueur", Text),
            ("birthdate_year", " Année de naissance", PositiveInt),
            ("birthdate_month", "Mois de naissance", PositiveInt),
            ("birthdate_day", " Jour de naissance", PositiveInt),
            ("gender", " Sexe", Gender),
            ("rank", " Rang du joueur", int)
        ])
