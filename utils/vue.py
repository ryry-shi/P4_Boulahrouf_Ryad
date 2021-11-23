def rang_by_rank(players):
        """méthode qui permet de trier les joueur par leur prénom"""
        players.sort(key=lambda x: x.rank)
        print(players)

def rang_by_name(players):
        """méthode qui permet de trier les joueur par leur rang"""
        players.sort(key=lambda x: x.first_name)
        print(players)
