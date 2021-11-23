from typing import List
from views.menu import Menu
from models.player import Player


class PlayerChoice(Menu):

    def __init__(self, players: List[Player]):
        super().__init__(
            title="choix du joueur", choices=[
                (str(player), player.id) for player in players])
