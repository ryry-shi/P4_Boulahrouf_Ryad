from models.player import player_manager as pm


class Match:
    def __init__(self, player_1_id, player_2_id, score_1=None):
        self.player_1_id = player_1_id
        self.player_2_id = player_2_id
        self.score_1 = score_1

    @property
    def player_1_id(self) -> int:
        return self.__player_1_id

    @player_1_id.setter
    def player_1_id(self, value: int):
        self.__player_1_id = value

    @property
    def player_2_id(self) -> int:
        return self.__player_2_id

    @player_2_id.setter
    def player_2_id(self, value: int):
        self.__player_2_id = value

    @property
    def score_1(self) -> float:
        return self.__score_1

    @score_1.setter
    def score_1(self, value: float):
        self.__score_1 = value

    @property
    def score_2(self) -> float:
        return 1.0 - self.score_1

    def __repr__(self) -> int:
        return f"(1) {pm.find_by_id(self.player_1_id)} vs (2) {pm.find_by_id(self.player_2_id)}"

    def __str__(self) -> int:
        return f"(1) {pm.find_by_id(self.player_1_id)} vs (2) {pm.find_by_id(self.player_2_id)}"

    def __eq__(self, obj) -> bool:
        return min(obj.player_1_id, obj.player_2_id) == min(self.player_1_id, self.player_2_id) and\
                max(obj.player_1_id, obj.player_2_id) == max(self.player_1_id, self.player_2_id)

    def serialize(self):
        return {
            "player_1_id": self.player_1_id,
            "player_2_id": self.player_2_id,
            "score_1": self.score_1
        }
