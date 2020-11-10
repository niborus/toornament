from .toornament_connection import SyncToornamentConnection


class SyncViewerAPI(SyncToornamentConnection):

    @staticmethod
    def _base_url():
        return 'https://api.toornament.com/viewer/v2'

    def fetch_match(self, tournament_id, id):
        """Retrieve a single match of a tournament.
        Returns a match with all its games and opponents. In ffa matches only the first four opponents are included in each match game.

        :param tournament_id The id of the tournament you want to retrieve data about.
        :param id The id of the match to retrieve."""

        tournament_id = str(tournament_id)
        id = str(id)

        method = 'GET'

        path = '/tournaments/{tournament_id}/matches/{id}'

        path_mapping = {
            'tournament_id': tournament_id,
            'id': id
        }

        return self._simple_access(method, path, path_parameters = path_mapping)
