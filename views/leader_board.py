from models.tournament import Tournament
from views.view import View


class LeaderBoard(View):

    def __init__(self, tournament: Tournament):
        content = ""
        for turn in tournament.turns:
            content += str(turn) + "\n"
            for match in turn.matchs:
                if match.score_1 == 1:
                    content += "le joueur 1 a gagner \n"
                elif match.score_1 == 0.5:
                    content += "Match nul \n"
                else:
                    content += "le joueur 2 a gagner \n"
        super().__init__(title="rapport", content=content)
