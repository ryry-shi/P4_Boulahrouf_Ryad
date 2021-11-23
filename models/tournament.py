from datetime import datetime
from utils.manager import Manager
from models.player import Player, player_manager
from typing import Union, List
from models.turn import Turn
from models.match import Match
from enum import Enum


class TimeControl(Enum):
    Blitz = "Blitz"
    Bullet = "Bullet"
    FastMove = "FastMove"


class Tournament:

    def __init__(
        self,
        id: int,
        name: str,
        location: str,
        start_date : datetime,
        time_control: TimeControl,
        description: str,
        nb_turns: int = 4,
        turns: List[Turn] = None,
        players: List[int] = None
    ):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.scores = {}
        self.turns = turns
        self.nb_turns = nb_turns
        self.players = players
        self.time_control = time_control
        self.description = description
        self.id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if 2 < len(value) < 25:
            self.__name = value
        else:
            raise ValueError("Erreur le prénom est trop grand ou trop petit")

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, value: str):
        if 3 < len(value) < 20:
            self.__location = value
        else:
            raise ValueError("Erreur le prénom est trop grand ou trop petit")

    @property
    def start_date(self) -> str:
        return self.__start_date

    @start_date.setter
    def start_date(self, value: str):
        self.__start_date = datetime.fromisoformat(str(value))

    @property
    def turns(self) -> List:
        return self.__turns

    @turns.setter
    def turns(self, value: List):
        if value == None:
            self.__turns = []
        self.__turns = [Turn(**turn) for turn in value]

    @property
    def nb_turns(self):
        return self.__nb_turns

    @nb_turns.setter
    def nb_turns(self, value=4):
        self.__nb_turns = value

    @property
    def players(self) -> List[Player]:
        return self.__players

    @players.setter
    def players(self, value: List[Union[Player, int]]):
        self.__players = []
        if len(value) % 2 != 0:
            raise ValueError("Le nombre de joueurs doit être pair")
        if self.nb_turns >= len(value):
            raise ValueError("Le nombre de tours doit être inférieur au nombre de joueurs")
        for p in value:
            if isinstance(p, int):
                p = player_manager.find_by_id(p)
            if isinstance(p, Player):
                self.__players.append(p)
            self.scores[p.id] = 0.0

    @property
    def time_control(self) -> TimeControl:
        return self.__time_control


    @time_control.setter
    def time_control(self, value: TimeControl):
        try:
            if isinstance(value, str):
                value = TimeControl[value]
            else:
                try:
                    value = TimeControl(value)
                except AttributeError:
                    raise ValueError
            self.__time_control = value
        except (ValueError, KeyError):
            raise ValueError("time control must have value bullet, blitz or fast")

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, value: str):
        self.__description = value

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, value: int):
        self.__id = value

    def serialize(self):
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date.isoformat(),
            "turns": [turn.serialize() for turn in self.turns],
            "nb_turns": self.nb_turns,
            "players": [player.id for player in self.players],
            "time_control": self.time_control.value,
            "description": self.description,
            "id": self.id
        }

    @property
    def tournois_id(self) -> str:
        return f"{self.name}:{self.location}:{self.start_date.isoformat()}:{self.players}"

    @property
    def matchs(self) -> List[Match]:
        result = []
        for t in self.turns:
            for m in t.matchs:
                result.append(m)
        return result

tournament_manager = Manager(item_type=Tournament)
