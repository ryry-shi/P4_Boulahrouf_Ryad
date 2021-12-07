from datetime import date
from utils.manager import Manager


class Player:

    """Classe Player
    il y a 8 joueur dans un tournois identifié par un nom prénom sexe
    rang et id"""
    next_id = 0

    def __init__(
        self,
        first_name: str,
        last_name: str,
        gender: str,
        rank: int,
        birthdate: str,
        id: int = None
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.gender = gender
        self.rank = rank
        self.id = id

    @property
    def first_name(self) -> str:
        return self.__first_name

    @first_name.setter
    def first_name(self, value: str):
        if 2 < len(value) < 16:
            self.__first_name = value.title()
        else:
            raise ValueError("Erreur le prénom est trop grand ou trop petit")

    @property
    def last_name(self) -> str:
        return self.__last_name

    @last_name.setter
    def last_name(self, value: str):
        if 2 < len(value) < 16:
            self.__last_name = value.title()
        else:
            raise ValueError("Erreur le prénom est trop grand ou trop petit")

    @property
    def birthdate(self) -> str:
        return self.__birthdate

    @birthdate.setter
    def birthdate(self, value: str):
        self.__birthdate = date.fromisoformat(str(value))

    @property
    def gender(self) -> str:
        return self.__gender

    @gender.setter
    def gender(self, value: str):
        if value.lower():
            self.__gender = value

    @property
    def rank(self) -> int:
        return self.__rank

    @rank.setter
    def rank(self, value: int):
        if (value <= 0):
            raise AttributeError("Le rang doit être positif")
        self.__rank = value

    def serialize(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'birthdate': self.birthdate.isoformat(),
            'gender': self.gender,
            'rank': self.rank,
            'id': self.id
        }

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if not value:
            value = Player.next_id
            Player.next_id += 1
        self.__id = value

    def __repr__(self) -> str:
        return f"{self.last_name} {self.first_name}"

    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name} {self.rank}"


player_manager = Manager(item_type=Player)
