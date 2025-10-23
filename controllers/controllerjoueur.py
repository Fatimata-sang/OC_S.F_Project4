from models import joueur
from views import viewjoueur


class ControllerJoueur:
    def __init__(self):
        """Initialise un contrôleur gérant les joueurs.

        Attrs:
        - model (obj): contient un modèle Player.
        - report_view (obj): contient la vue PlayerView associée au contrôleur.
        - waiting_room (list): salle d'attente tampon
        des joueurs créés ou chargés
         (initialisé en une liste vide).
        """
        self.model = joueur.Joueur
        self.player_view = viewjoueur.ViewJoueur(self)
        self.waiting_room = []

    def create_new_player(self, name, first_name,
                          birthdate, national_chess_id):
        """Crée un joueur, le sauvegarde dans la base de données et
         l'ajoute à la salle d'attente."""
        new_player = self.model(name, first_name, birthdate, national_chess_id)
        new_player.update_json_file()
        self.waiting_room.append(new_player)

    def get_existing_players(self):
        """Renvoie la liste des joueurs existants."""
        return self.model.list_existing_players()
