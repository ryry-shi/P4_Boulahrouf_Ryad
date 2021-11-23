from datetime import date
from typing import List
from models.match import Match
from models.turn import Turn
from utils.asks import resultat
from models.player import player_manager as pm
from models.tournament import tournament_manager as tm
from views.main_menu import MainMenu
from views.tournaments_menu import TournamentsMenu
from views.players_menu import PlayersMenu
from utils.matchmaking import (
    gen_turn
)
from views.forms import (
    select_identifiant
)
from views.lists import (
    rang_by_name, rang_by_rank
)
from views.form import(
    CreatePlayerForm,
    CreateTournamentForm
)


class Controller:
    def players(self):
        """Menu du joueur"""
        while True:
            choice = PlayersMenu().show()
            liste_players = pm.find_all()
            if choice == 1:
                self.create_player()
            if choice == 2:
                data = select_identifiant()
                player = pm.find_by_id(data["id"])
                edit = int(input(""))
                player.rank = edit
                pm.insert_item(player.id)
            if choice == 3:
                rang_by_name(liste_players)
            if choice == 4:
                rang_by_rank(liste_players)
            if choice == 5:
                break

    def create_player(self):
        data = CreatePlayerForm().show()
        data["birthdate"] = date(
            year=data["birthdate_year"],
            month=data["birthdate_month"],
            day=data["birthdate_day"])
        del data["birthdate_year"]
        del data["birthdate_month"]
        del data["birthdate_day"]
        player = pm.create(**data)
        pm.insert_item(player.id)


    def create_tournament(self):
        data = CreateTournamentForm().show()
        data["players"] = []
        data["turns"] = []
        data["start_date"] = date(
            year=data["start_date_year"],
            month=data["start_date_month"],
            day=data["start_date_day"])
        del data["start_date_year"]
        del data["start_date_month"]
        del data["start_date_day"]
        for _ in range(data["numbers_players"]):
            while True:
                try:
                    pid = int(input("Id du joueur ? "))
                    if pid in data["players"]:
                        raise ValueError
                    data["players"].append(pm.find_by_id(pid))
                    break
                except (ValueError, KeyError):
                    pass
        del data["numbers_players"]
        tournament = tm.create(**data)
        tm.insert_item(tournament.id)

    def tournament(self):
        while True:
            choice = TournamentsMenu().show()
            if choice == 1:
                tournament = self.create_tournament()
                print(tournament)
            if choice == 2:
                self.play_tournament()
            if choice == 3:
                data = select_identifiant()
                tm.insert_item(data["id"])
            if choice == 4:
                break

    def play_tournament(self):
        # obtenir un tournoi
        while True:
            data = select_identifiant()
            try:
                tournament = tm.find_by_id(data["id"])
                break
            except ValueError:
                pass
        # afficher une erreur si tournoi terminé
        if len(tournament.turns) == tournament.nb_turns:
            print("le tournois est déja terminé")

        # sinon jouer le tournoi
        else:
            # reprendre le tournoi là où il en était
            for turn_nb in range(len(tournament.turns) + 1, tournament.nb_turns + 1):
                
                # on génère un tour qui contient des matchs à jouer
                turn = gen_turn(turn_nb, tournament)
                print(turn.name)

                # parcours les matchs à jouer
                for match in turn.matchs:

                    #on récupère les participants
                    p1 = pm.find_by_id(match.player_1_id)
                    p2 = pm.find_by_id(match.player_2_id)

                    # on demande à l'organisation d'entrer le score du joueur1
                    while True:
                        try:
                            match.score_1 = float(input(f"(1) {p1} vs (2) {p2} : score (1)) ? "))
                            if match.score_1 not in (0.0, 0.5, 1.0):
                                raise ValueError
                            break
                        except ValueError:
                            pass

                    # mise à jour du tableau des scores
                    tournament.scores[p1.id] += match.score_1
                    tournament.scores[p2.id] += match.score_2

                # insertion du tour dans le tournoi
                tournament.turns.append(turn)

                # sauvegarde du tournoi à chaque tour
                tm.insert_item(tournament.id)


    def main(self):
        while True:
            choice = MainMenu().show()
            if choice == 1:
                self.players()
            elif choice == 2:
                self.tournament()
            elif choice == 3:
                break
