from models.match import Match


class Turn:
    """classe turn
    la classe turn est une classe nécéssaire pour
    le tournois qui possède les tours c'est une liste
    a l'intérieur ou se trouve un str et
    une autre liste match qui possèdera sa classe"""
    def __init__(self, matchs, name):
        self.matchs = matchs
        self.name = name

    @property
    def matchs(self):
        return self.__matchs

    @matchs.setter
    def matchs(self, value):
        self.__matchs = [Match(**match) if not isinstance(match, Match) else match for match in value]

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def __repr__(self) -> str:
        return self.name

    def serialize(self):
        return {
            "name": self.name,
            "matchs": [match.serialize() for match in self.matchs]
        }
