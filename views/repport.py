from models.tournament import Tournament
from views.view import View


class Repport(View):

    def __init__(self, tournament: Tournament):
        content = ""
        for turn in tournament.turns:
            content += str(turn) + "\n"
            for match in turn.matchs:
                content += str(match) + "\n"
        super().__init__(title="rapport", content=content)
