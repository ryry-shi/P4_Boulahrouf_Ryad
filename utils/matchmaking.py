from models.match import Match
from models.tournament import Tournament
from models.turn import Turn


def gen_turn(turn_nb: int, tournament: Tournament):
    """Méthode qui créer les turn et les groupe de joueur et les ajoute
    dans une liste"""

    # création du tour
    turn = Turn(matchs=[], name=f"Turn {turn_nb}")

    # récupération des joueurs du tournoi
    players = tournament.players.copy()

    # si premier tour
    if turn_nb == 1:
        # triage des joueur par rang
        players.sort(key=lambda x: x.rank)
        group1, group2 = players[:len(players)//2], players[len(players)//2:]
        turn.matchs = [Match(p1.id, p2.id) for p1, p2 in zip(group1, group2)]

    # si prochains tours
    else:
        # triage des joueurs par score
        players.sort(key=lambda x: tournament.scores[x.id])

        # tant qu'il reste des joueurs qui n'ont pas joué
        while players:

            # on retire et garde un premier joueur
            p1 = players.pop(0)

            # on parcours les autres joueurs
            for p2 in players:

                # on crée le match hypothétique
                match = Match(p1.id, p2.id)

                # si le match n'a pas déjà été joué
                for m in tournament.matchs:
                    print(m)
                    print(match)
                    if m == match:
                        break
                else:
                    # ajout du match au tournoi
                    turn.matchs.append(match)

                    # suppression du joueur qui vient de jouer
                    players.pop(players.index(p2))
                    break
    return turn
