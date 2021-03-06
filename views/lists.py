from views.view import View


def rang_by_rank(players):
    """Fonction qui permet de trier les joueur par leur prénom"""
    View(
        title="Liste des joueurs",
        content="\n".join([str(p) for p in sorted(
            players, key=lambda x: (-x.rank, x.last_name, x.first_name))]),
        blocking=True
    ).show()


def rang_by_name(players):
    """Fonction qui permet de trier les joueur par leur rang"""
    View(
        title="Liste des joueurs",
        content="\n".join([str(p) for p in sorted(
            players, key=lambda x: (x.last_name, x.first_name, -x.rank))]),
        blocking=True
    ).show()


def liste_tournaments(tournaments):
    """Fonction qui permet de lister les tournois"""
    View(
        title="Liste des tournois",
        content="\n".join([str(p.serialize()) for p in tournaments]),
        blocking=True
    ).show()
