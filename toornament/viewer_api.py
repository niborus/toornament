from .toornament_connection import SyncToornamentConnection, AsyncToornamentConnection
from .viewer_schemas import *
from typing import Optional
from .range import Range


class SyncViewerAPI(SyncToornamentConnection):

    @staticmethod
    def _base_url():
        return 'https://api.toornament.com/viewer/v2'

    def get_match(self, tournament_id, id):
        """Retrieve a single match of a tournament.
        Returns a match with all its games and opponents. In ffa matches only the first four opponents are included in each match game.

        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param id: The id of the match to retrieve."""

        tournament_id = str(tournament_id)
        id = str(id)

        method = 'GET'

        path = '/tournaments/{tournament_id}/matches/{id}'

        path_mapping = {
            'tournament_id': tournament_id,
            'id': id,
        }

        query_parameters = {
        }

        headers = {
        }

        content = self._simple_access(method, path, path_parameters = path_mapping, query_parameters = query_parameters,
                                      headers = headers)

        return MatchDetailed(**content)

    def get_matches_from_tournament(self, tournament_id, *, range: Range, stage_ids: Optional[list] = None,
                                    stage_numbers: Optional[list] = None, group_ids: Optional[list] = None,
                                    group_numbers: Optional[list] = None, round_ids: Optional[list] = None,
                                    round_numbers: Optional[list] = None, statuses: Optional[list] = None,
                                    is_scheduled: Optional[bool] = None, scheduled_before: Optional[str] = None,
                                    scheduled_after: Optional[str] = None, participant_ids: Optional[list] = None,
                                    sort: Optional[str] = None):
        """Retrieve matches of a tournament.
        Returns the matches of a tournament. In ffa matches only the first four opponents are included in each match.

        :param range: A range of requested items using the 'matches' unit. The size of the range can not exceed 128. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))
        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param stage_ids: One or several stage ids to filter.
        :param stage_numbers: One or several stage numbers to filter.
        :param group_ids: One or several group ids to filter.
        :param group_numbers: One or several group numbers to filter.
        :param round_ids: One or several round ids to filter.
        :param round_numbers: One or several round numbers to filter.
        :param statuses: One or several match statuses to filter.
        :param is_scheduled: Whether to include scheduled matches.
        :param scheduled_before: A datetime in RFC 3339 format (combined date, time and utc offset), to include all matches scheduled before or at the datetime.
        :param scheduled_after: A datetime in RFC 3339 format (combined date, time and utc offset), to include all matches scheduled after or at the datetime
        :param participant_ids: One or several participant ids involved in the matches to filter.
        :param sort: A method to sort the filtered data. "structure" sorts using the stage, group, round and match numbers. "schedule" sorts using the scheduled date. "latest results" sorts using the date at which the matches were played (not scheduled)."""

        tournament_id = str(tournament_id)
        stage_ids = [str(e) for e in stage_ids] if stage_ids else stage_ids
        group_ids = [str(e) for e in group_ids] if group_ids else group_ids
        round_ids = [str(e) for e in round_ids] if round_ids else round_ids
        participant_ids = [str(e) for e in participant_ids] if participant_ids else participant_ids

        method = 'GET'

        path = '/tournaments/{tournament_id}/matches'

        path_mapping = {
            'tournament_id': tournament_id,
        }

        query_parameters = {
        }
        if stage_ids:
            query_parameters['stage_ids'] = stage_ids
        if stage_numbers:
            query_parameters['stage_numbers'] = stage_numbers
        if group_ids:
            query_parameters['group_ids'] = group_ids
        if group_numbers:
            query_parameters['group_numbers'] = group_numbers
        if round_ids:
            query_parameters['round_ids'] = round_ids
        if round_numbers:
            query_parameters['round_numbers'] = round_numbers
        if statuses:
            query_parameters['statuses'] = statuses
        if is_scheduled:
            query_parameters['is_scheduled'] = is_scheduled
        if scheduled_before:
            query_parameters['scheduled_before'] = scheduled_before
        if scheduled_after:
            query_parameters['scheduled_after'] = scheduled_after
        if participant_ids:
            query_parameters['participant_ids'] = participant_ids
        if sort:
            query_parameters['sort'] = sort

        if not range.unit:
            range.unit = 'matches'

        headers = {
            'Range': range.get_header_value(),
        }

        content = self._simple_access(method, path, path_parameters = path_mapping, query_parameters = query_parameters,
                                      headers = headers)

        return [Match(**match) for match in content]

    def get_matches_from_discipline(self, discipline_id, *, range: Range, is_featured: Optional[bool] = None,
                                    statuses: Optional[list] = None, scheduled_before: Optional[str] = None,
                                    scheduled_after: Optional[str] = None, participant_ids: Optional[list] = None,
                                    tournament_ids: Optional[list] = None, sort: Optional[str] = None):
        """Retrieve matches of a discipline, regardless of their tournament.
        Returns matches of a discipline. In ffa matches only the first four opponents are included in each match game.

        :param range: A range of requested items using the 'matches' unit. The size of the range can not exceed 128. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))
        :param discipline_id: The string id of the discipline.
        :param is_featured: Whether to include featured tournaments.
        :param statuses: One or several match statuses to filter.
        :param scheduled_before: A datetime in RFC 3339 format (combined date, time and utc offset), to include all matches scheduled before or at the datetime.
        :param scheduled_after: A datetime in RFC 3339 format (combined date, time and utc offset), to include all matches scheduled after or at the datetime
        :param participant_ids: One or several participant ids involved in the matches to filter.
        :param tournament_ids: List of tournament IDs to filter the data with.
        :param sort: A method to sort the filtered data. "structure" sorts using the stage, group, round and match numbers. "schedule" sorts using the scheduled date. "latest results" sorts using the date at which the matches were played (not scheduled)."""

        discipline_id = str(discipline_id)
        participant_ids = [str(e) for e in participant_ids] if participant_ids else participant_ids
        tournament_ids = [str(e) for e in tournament_ids] if tournament_ids else tournament_ids

        method = 'GET'

        path = '/disciplines/{discipline_id}/matches'

        path_mapping = {
            'discipline_id': discipline_id,
        }

        query_parameters = {
        }
        if is_featured:
            query_parameters['is_featured'] = is_featured
        if statuses:
            query_parameters['statuses'] = statuses
        if scheduled_before:
            query_parameters['scheduled_before'] = scheduled_before
        if scheduled_after:
            query_parameters['scheduled_after'] = scheduled_after
        if participant_ids:
            query_parameters['participant_ids'] = participant_ids
        if tournament_ids:
            query_parameters['tournament_ids'] = tournament_ids
        if sort:
            query_parameters['sort'] = sort

        if not range.unit:
            range.unit = 'matches'

        headers = {
            'Range': range.get_header_value(),
        }

        content = self._simple_access(method, path, path_parameters = path_mapping, query_parameters = query_parameters,
                                      headers = headers)

        return [MatchDiscipline(**match) for match in content]

    def get_bracket_nodes(self, tournament_id, stage_id, *, range: Range, group_ids: Optional[list] = None,
                          group_numbers: Optional[list] = None, round_ids: Optional[list] = None,
                          round_numbers: Optional[list] = None, min_depth: Optional[int] = None,
                          max_depth: Optional[int] = None):
        """Retrieve bracket nodes of a stage and tournament.
        Returns the bracket nodes of a stage. A bracket node represents a match and some extra data.

        :param range: A range of requested items using the 'nodes' unit. The size of the range can not exceed 128. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))
        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param stage_id: The id of the stage you want to retrieve data about.
        :param group_ids: A list of group ids to filter.
        :param group_numbers: A list of group numbers to filter.
        :param round_ids: A list of round ids to filter.
        :param round_numbers: A list of round numbers to filter.
        :param min_depth: A minimum depth to filter.
        :param max_depth: A maximal depth to filter."""

        tournament_id = str(tournament_id)
        stage_id = str(stage_id)
        group_ids = [str(e) for e in group_ids] if group_ids else group_ids
        round_ids = [str(e) for e in round_ids] if round_ids else round_ids

        method = 'GET'

        path = '/tournaments/{tournament_id}/stages/{stage_id}/bracket-nodes'

        path_mapping = {
            'tournament_id': tournament_id,
            'stage_id': stage_id,
        }

        query_parameters = {
        }
        if group_ids:
            query_parameters['group_ids'] = group_ids
        if group_numbers:
            query_parameters['group_numbers'] = group_numbers
        if round_ids:
            query_parameters['round_ids'] = round_ids
        if round_numbers:
            query_parameters['round_numbers'] = round_numbers
        if min_depth:
            query_parameters['min_depth'] = min_depth
        if max_depth:
            query_parameters['max_depth'] = max_depth

        if not range.unit:
            range.unit = 'nodes'

        headers = {
            'Range': range.get_header_value(),
        }

        content = self._simple_access(method, path, path_parameters = path_mapping, query_parameters = query_parameters,
                                      headers = headers)

        return [BracketNode(**node) for node in content]

    def get_custom_fields(self, tournament_id, *, target_type: Optional[str] = None):
        """Retrieves custom fields of a tournament.
        Returns the complete definition of all custom fields for a given tournament. This includes both public and private custom fields.
        A custom field may be associated to a player, a team or a team's player. For more information, please read the [Custom Fields](https://developer.toornament.com/v2/core-concepts/custom-fields) documentation.

        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param target_type: The entity affected by the custom fields."""

        tournament_id = str(tournament_id)

        method = 'GET'

        path = '/tournaments/{tournament_id}/custom-fields'

        path_mapping = {
            'tournament_id': tournament_id,
        }

        query_parameters = {
        }
        if target_type:
            query_parameters['target_type'] = target_type

        headers = {
        }

        content = self._simple_access(method, path, path_parameters = path_mapping, query_parameters = query_parameters,
                                      headers = headers)

        return [CustomField(**field) for field in content]

    def get_disciplines(self, *, range: Range):
        """Retrieve the list of available disciplines and their basic information.
        Returns a collection of disciplines.

        :param range
        A range of requested items using the 'disciplines' unit.
        The size of the range can not exceed 50. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))"""

        method = 'GET'

        path = '/disciplines'

        path_mapping = {
        }

        query_parameters = {
        }

        if not range.unit:
            range.unit = 'disciplines'

        headers = {
            'Range': range.get_header_value(),
        }

        content = self._simple_access(method, path, path_parameters = path_mapping, query_parameters = query_parameters,
                                      headers = headers)

        return [Discipline(**discipline) for discipline in content]

    def get_discipline(self, id):
        """Retrieve a specific discipline, with advanced information.
        Returns a discipline with its information and configuration options.

        :param id: The string id of the discipline."""

        id = str(id)

        method = 'GET'

        path = '/disciplines/{id}'

        path_mapping = {
            'id': id,
        }

        query_parameters = {
        }

        headers = {
        }

        content = self._simple_access(method, path, path_parameters = path_mapping, query_parameters = query_parameters,
                                      headers = headers)

        return DisciplineDetailed(**content)

    def get_groups(self, tournament_id, *, range: Range, stage_ids: Optional[list] = None,
                   stage_numbers: Optional[list] = None):
        """Retrieve all groups of a tournament.
        Returns all groups of a tournament with basic information and settings.

        :param range: A range of requested items using the 'groups' unit. The size of the range can not exceed 50. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))
        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param stage_ids: A list of stage ids to filter.
        :param stage_numbers: A list of stage numbers to filter."""

        tournament_id = str(tournament_id)
        stage_ids = [str(e) for e in stage_ids] if stage_ids else stage_ids

        method = 'GET'

        path = '/tournaments/{tournament_id}/groups'

        path_mapping = {
            'tournament_id': tournament_id,
        }

        query_parameters = {
        }
        if stage_ids:
            query_parameters['stage_ids'] = stage_ids
        if stage_numbers:
            query_parameters['stage_numbers'] = stage_numbers

        if not range.unit:
            range.unit = 'groups'

        headers = {
            'Range': range.get_header_value(),
        }

        content = self._simple_access(method, path, path_parameters = path_mapping, query_parameters = query_parameters,
                                      headers = headers)

        return [Group(**group) for group in content]

    def get_group(self, tournament_id, id):
        """Retrieve a single group of a tournament.
        Returns a group with the given id with basic information and settings.

        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param id: The id of the group to retrieve."""

        tournament_id = str(tournament_id)
        id = str(id)

        method = 'GET'

        path = '/tournaments/{tournament_id}/groups/{id}'

        path_mapping = {
            'tournament_id': tournament_id,
            'id': id,
        }

        query_parameters = {
        }

        headers = {
        }

        content = self._simple_access(method, path, path_parameters = path_mapping, query_parameters = query_parameters,
                                      headers = headers)

        return Group(**content)

    def get_game(self, tournament_id, match_id, number):
        """Retrieve a single game of a match.
        Returns detailed information about one match game.

        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param match_id: The id of the match to retrieve.
        :param number: The relative identifier of the match game to retrieve."""

        tournament_id = str(tournament_id)
        match_id = str(match_id)

        method = 'GET'

        path = '/tournaments/{tournament_id}/matches/{match_id}/games/{number}'

        path_mapping = {
            'tournament_id': tournament_id,
            'match_id': match_id,
            'number': number,
        }

        query_parameters = {
        }

        headers = {
        }

        content = self._simple_access(method, path, path_parameters = path_mapping, query_parameters = query_parameters,
                                      headers = headers)

        return Game(**content)

    def get_participants(self, tournament_id, *, range: Range, name: Optional[str] = None, sort: Optional[str] = None):
        """Retrieve the participants of a tournament.
        Returns the participants of the given tournament. The data provided in the participant depends on whether the participant type is team or player. This setting can be found in the tournament.

        :param range: A range of requested items using the 'participants' unit. The size of the range can not exceed 50. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))
        :param tournament_id: The id of the tournament the participants are from.
        :param name: The string to be looked for in the name of the participant.
        :param sort: A method to sort the filtered data. “created_asc” and “created_desc” sort the participants from their creation date (earliest to latest, and inversely). “Alphabetic” sorts the participants using their case-insensitive names."""

        tournament_id = str(tournament_id)

        method = 'GET'

        path = '/tournaments/{tournament_id}/participants'

        path_mapping = {
            'tournament_id': tournament_id,
        }

        query_parameters = {
        }
        if name:
            query_parameters['name'] = name
        if sort:
            query_parameters['sort'] = sort

        if not range.unit:
            range.unit = 'participants'

        headers = {
            'Range': range.get_header_value(),
        }

        content = self._simple_access(method, path, path_parameters = path_mapping, query_parameters = query_parameters,
                                      headers = headers)

        return [
            ParticipantPlayer(**participant) if participant.get('lineup') is None else ParticipantTeam(**participant)
            for participant in content]

    def get_participant(self, tournament_id, id):
        """Retrieve a single participant of a tournament.
        Returns a participant identified with the given id. The data provided in the participant depends on whether the participant type is team or player. This setting can be found in the tournament.

        :param tournament_id: The id of the tournament the participants are from.
        :param id: The id of the participant to retrieve."""

        tournament_id = str(tournament_id)
        id = str(id)

        method = 'GET'

        path = '/tournaments/{tournament_id}/participants/{id}'

        path_mapping = {
            'tournament_id': tournament_id,
            'id': id,
        }

        query_parameters = {
        }

        headers = {
        }

        content = self._simple_access(method, path, path_parameters = path_mapping, query_parameters = query_parameters,
                                      headers = headers)

        return ParticipantPlayer(**content) if content.get('lineup') is None else ParticipantTeam(**content)

    def get_playlist(self, id):
        """Retrieve a single playlist.
        Returns a playlist identified with the given id.

        :param id: The id of the playlist to retrieve."""

        id = str(id)

        method = 'GET'

        path = '/playlists/{id}'

        path_mapping = {
            'id': id,
        }

        query_parameters = {
        }

        headers = {
        }

        content = self._simple_access(method, path, path_parameters = path_mapping, query_parameters = query_parameters,
                                      headers = headers)

        return Playlist(**content)

    def get_ranking_items(self, tournament_id, stage_id, *, range: Range, group_ids: Optional[list] = None,
                          group_numbers: Optional[list] = None):
        """Retrieve ranking items of a stage and tournament.
        Returns ranking items of a stage with a small summary of the associated participant in the ranking. The items are always ordered by ascending position.

        :param range: A range of requested items using the 'items' unit. The size of the range can not exceed 50. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))
        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param stage_id: The id of the stage you want to retrieve data about.
        :param group_ids: A list of group ids to filter.
        :param group_numbers: A list of group numbers to filter."""

        tournament_id = str(tournament_id)
        stage_id = str(stage_id)
        group_ids = [str(e) for e in group_ids] if group_ids else group_ids

        method = 'GET'

        path = '/tournaments/{tournament_id}/stages/{stage_id}/ranking-items'

        path_mapping = {
            'tournament_id': tournament_id,
            'stage_id': stage_id,
        }

        query_parameters = {
        }
        if group_ids:
            query_parameters['group_ids'] = group_ids
        if group_numbers:
            query_parameters['group_numbers'] = group_numbers

        if not range.unit:
            range.unit = 'items'

        headers = {
            'Range': range.get_header_value(),
        }

        content = self._simple_access(method, path, path_parameters = path_mapping, query_parameters = query_parameters,
                                      headers = headers)

        return [RankingItem(**item) for item in content]

    def get_rounds(self, tournament_id, *, range: Range, stage_ids: Optional[list] = None,
                   stage_numbers: Optional[list] = None, group_ids: Optional[list] = None,
                   group_numbers: Optional[list] = None):
        """Retrieve all rounds of a tournament.
        Returns all rounds of a tournament with basic information and settings.

        :param range: A range of requested items using the 'rounds' unit. The size of the range can not exceed 50. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))
        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param stage_ids: A list of stage ids to filter.
        :param stage_numbers: A list of stage numbers to filter.
        :param group_ids: A list of group ids to filter.
        :param group_numbers: A list of group numbers to filter."""

        tournament_id = str(tournament_id)
        stage_ids = [str(e) for e in stage_ids] if stage_ids else stage_ids
        group_ids = [str(e) for e in group_ids] if group_ids else group_ids

        method = 'GET'

        path = '/tournaments/{tournament_id}/rounds'

        path_mapping = {
            'tournament_id': tournament_id,
        }

        query_parameters = {
        }
        if stage_ids:
            query_parameters['stage_ids'] = stage_ids
        if stage_numbers:
            query_parameters['stage_numbers'] = stage_numbers
        if group_ids:
            query_parameters['group_ids'] = group_ids
        if group_numbers:
            query_parameters['group_numbers'] = group_numbers

        if not range.unit:
            range.unit = 'rounds'

        headers = {
            'Range': range.get_header_value(),
        }

        content = self._simple_access(method, path, path_parameters = path_mapping, query_parameters = query_parameters,
                                      headers = headers)

        return [Round(**round) for round in content]

    def get_round(self, tournament_id, id):
        """Retrieve a single round of a tournament.
        Returns a round with the given id with basic information and settings.

        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param id: The id of the round to retrieve."""

        tournament_id = str(tournament_id)
        id = str(id)

        method = 'GET'

        path = '/tournaments/{tournament_id}/rounds/{id}'

        path_mapping = {
            'tournament_id': tournament_id,
            'id': id,
        }

        query_parameters = {
        }

        headers = {
        }

        content = self._simple_access(method, path, path_parameters = path_mapping, query_parameters = query_parameters,
                                      headers = headers)

        return Round(**content)

    def get_stages(self, tournament_id):
        """Retrieve all stages of a tournament.
        Returns all stages of a tournament with basic information and settings.

        :param tournament_id: The id of the tournament you want to retrieve data about."""

        tournament_id = str(tournament_id)

        method = 'GET'

        path = '/tournaments/{tournament_id}/stages'

        path_mapping = {
            'tournament_id': tournament_id,
        }

        query_parameters = {
        }

        headers = {
        }

        content = self._simple_access(method, path, path_parameters = path_mapping, query_parameters = query_parameters,
                                      headers = headers)

        return [Stage(**stage) for stage in content]

    def get_stage(self, tournament_id, id):
        """Retrieve a single stage of a tournament.
        Returns a stage with the given id with basic information and settings.

        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param id: The id of the stage to retrieve."""

        tournament_id = str(tournament_id)
        id = str(id)

        method = 'GET'

        path = '/tournaments/{tournament_id}/stages/{id}'

        path_mapping = {
            'tournament_id': tournament_id,
            'id': id,
        }

        query_parameters = {
        }

        headers = {
        }

        content = self._simple_access(method, path, path_parameters = path_mapping, query_parameters = query_parameters,
                                      headers = headers)

        return Stage(**content)

    def get_standings(self, *, range: Range, tournament_ids: list, participant_ids: Optional[list] = None):
        """Retrieve a list of final standing items.
        Returns a list of final standing items.

        :param range: A range of requested items using the 'items' unit. The size of the range can not exceed 50. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))
        :param tournament_ids: Only return tournaments for the given list of ids.
        :param participant_ids: One or several participant ids involved in the standings to filter."""

        tournament_ids = [str(e) for e in tournament_ids]
        participant_ids = [str(e) for e in participant_ids] if participant_ids else participant_ids

        method = 'GET'

        path = '/standings'

        path_mapping = {
        }

        query_parameters = {
            'tournament_ids': tournament_ids,
        }
        if participant_ids:
            query_parameters['participant_ids'] = participant_ids

        if not range.unit:
            range.unit = 'items'

        headers = {
            'Range': range.get_header_value(),
        }

        content = self._simple_access(method, path, path_parameters = path_mapping, query_parameters = query_parameters,
                                      headers = headers)

        return [StandingItem(**item) for item in content]

    def get_streams(self, tournament_id, *, range: Range, match_ids: Optional[list] = None):
        """Retrieves available streams.
        Returns the streams of the given tournament.

        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param range: A range of requested items using the 'streams' unit. The size of the range can not exceed 50. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))
        :param match_ids: A list of match ids to filter."""

        tournament_id = str(tournament_id)
        match_ids = [str(e) for e in match_ids] if match_ids else match_ids

        method = 'GET'

        path = '/tournaments/{tournament_id}/streams'

        path_mapping = {
            'tournament_id': tournament_id,
        }

        query_parameters = {
        }
        if match_ids:
            query_parameters['match_ids'] = match_ids

        if not range.unit:
            range.unit = 'streams'

        headers = {
            'Range': range.get_header_value(),
        }

        content = self._simple_access(method, path, path_parameters = path_mapping, query_parameters = query_parameters,
                                      headers = headers)

        return [Stream(**stream) for stream in content]

    def get_videos(self, tournament_id, *, range: Range, participant_ids: Optional[list] = None,
                   category: Optional[str] = None, sort: Optional[str] = None):
        """Retrieve videos of a tournament.
        Returns the videos of the given tournament.

        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param range: A range of requested items using the 'videos' unit. The size of the range can not exceed 50. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))
        :param participant_ids: One or several participant ids to filter.
        :param category: The category of the videos.
        :param sort: Sorts the collection in a particular order. "created_asc" sorts the videos from the oldest to the most recent one; "created_desc" sorts the videos from the most recent to the oldest one."""

        tournament_id = str(tournament_id)
        participant_ids = [str(e) for e in participant_ids] if participant_ids else participant_ids

        method = 'GET'

        path = '/tournaments/{tournament_id}/videos'

        path_mapping = {
            'tournament_id': tournament_id,
        }

        query_parameters = {
        }
        if participant_ids:
            query_parameters['participant_ids'] = participant_ids
        if category:
            query_parameters['category'] = category
        if sort:
            query_parameters['sort'] = sort

        if not range.unit:
            range.unit = 'videos'

        headers = {
            'Range': range.get_header_value(),
        }

        content = self._simple_access(method, path, path_parameters = path_mapping, query_parameters = query_parameters,
                                      headers = headers)

        return [VideoTournament(**video) for video in content]

    def get_videos_by_match(self, tournament_id, match_id, *, category: Optional[str] = None,
                            sort: Optional[str] = None):
        """Retrieve videos of a match.
        Returns the videos of the given match.

        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param match_id: The id of the match to retrieve.
        :param category: The category of the videos.
        :param sort: Sorts the collection in a particular order. "created_asc" sorts the videos from the oldest to the most recent one; "created_desc" sorts the videos from the most recent to the oldest one."""

        tournament_id = str(tournament_id)
        match_id = str(match_id)

        method = 'GET'

        path = '/tournaments/{tournament_id}/matches/{match_id}/videos'

        path_mapping = {
            'tournament_id': tournament_id,
            'match_id': match_id,
        }

        query_parameters = {
        }
        if category:
            query_parameters['category'] = category
        if sort:
            query_parameters['sort'] = sort

        headers = {
        }

        content = self._simple_access(method, path, path_parameters = path_mapping, query_parameters = query_parameters,
                                      headers = headers)

        return [Video(**video) for video in content]

    def get_tournaments_featured(self, *, range: Range, name: Optional[str] = None, disciplines: Optional[str] = None,
                                 statuses: Optional[str] = None, scheduled_before: Optional[str] = None,
                                 scheduled_after: Optional[str] = None, countries: Optional[str] = None,
                                 platforms: Optional[str] = None, is_online: Optional[int] = None,
                                 sort: Optional[str] = None):
        """Retrieve published featured tournaments.
        Returns a collection of published featured tournaments.

        :param range: A range of requested items using the 'tournaments' unit. The size of the range can not exceed 50. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))
        :param name: The string to be looked for in the name or full name.
        :param disciplines: One or several disciplines to filter.
        :param statuses: One or several tournament statuses to filter.
        :param scheduled_before: A date to include all tournaments scheduled to take place before or at the date, in ISO 8601 format (only the date part, with YYYY-MM-DD pattern).
        :param scheduled_after: A date to include all tournaments scheduled to take place after or at the date, in ISO 8601 format (only the date part, with YYYY-MM-DD pattern).
        :param countries: One or several countries to filter in ISO 3166-1 alpha-2 country codes format (some codes may not be supported)
        :param platforms: One or several platforms to filter.
        :param is_online: Whether the tournament is played online.
        :param sort: Sorts the collection in a particular order. "scheduled_asc" sorts the tournaments by scheduled date from the oldest to the most recent one; "scheduled_desc" sorts the tournaments by scheduled date from the most recent to the oldest one."""

        method = 'GET'

        path = '/tournaments/featured'

        path_mapping = {
        }

        query_parameters = {
        }
        if name:
            query_parameters['name'] = name
        if disciplines:
            query_parameters['disciplines'] = disciplines
        if statuses:
            query_parameters['statuses'] = statuses
        if scheduled_before:
            query_parameters['scheduled_before'] = scheduled_before
        if scheduled_after:
            query_parameters['scheduled_after'] = scheduled_after
        if countries:
            query_parameters['countries'] = countries
        if platforms:
            query_parameters['platforms'] = platforms
        if is_online:
            query_parameters['is_online'] = is_online
        if sort:
            query_parameters['sort'] = sort

        if not range.unit:
            range.unit = 'tournaments'

        headers = {
            'Range': range.get_header_value(),
        }

        content = self._simple_access(method, path, path_parameters = path_mapping, query_parameters = query_parameters,
                                      headers = headers)

        return [Tournament(**tour) for tour in content]

    def get_tournament(self, id):
        """Retrieve a single tournament.
        Returns a tournament identified with the given id.

        :param id: The id of the tournament to retrieve."""

        id = str(id)

        method = 'GET'

        path = '/tournaments/{id}'

        path_mapping = {
            'id': id,
        }

        query_parameters = {
        }

        headers = {
        }

        content = self._simple_access(method, path, path_parameters = path_mapping, query_parameters = query_parameters,
                                      headers = headers)

        return TournamentDetailed(**content)

    def get_tournaments_by_playlist(self, id, *, range: Range, name: Optional[str] = None,
                                    disciplines: Optional[str] = None, statuses: Optional[str] = None,
                                    scheduled_before: Optional[str] = None, scheduled_after: Optional[str] = None,
                                    countries: Optional[str] = None, platforms: Optional[str] = None,
                                    is_online: Optional[int] = None, sort: Optional[str] = None):
        """Retrieve the tournaments of a playlist.
        Returns the tournaments of a playlist.

        :param range: A range of requested items using the 'tournaments' unit. The size of the range can not exceed 50. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))
        :param id: The string id of the tournament.
        :param name: The string to be looked for in the name or full name.
        :param disciplines: One or several disciplines to filter.
        :param statuses: One or several tournament statuses to filter.
        :param scheduled_before: A date to include all tournaments scheduled to take place before or at the date, in ISO 8601 format (only the date part, with YYYY-MM-DD pattern).
        :param scheduled_after: A date to include all tournaments scheduled to take place after or at the date, in ISO 8601 format (only the date part, with YYYY-MM-DD pattern).
        :param countries: One or several countries to filter in ISO 3166-1 alpha-2 country codes format (some codes may not be supported)
        :param platforms: One or several platforms to filter.
        :param is_online: Whether the tournament is played online.
        :param sort: Sorts the collection in a particular order. "scheduled_asc" sorts the tournaments by scheduled date from the oldest to the most recent one; "scheduled_desc" sorts the tournaments by scheduled date from the most recent to the oldest one."""

        id = str(id)

        method = 'GET'

        path = '/playlists/{id}/tournaments'

        path_mapping = {
            'id': id,
        }

        query_parameters = {
        }
        if name:
            query_parameters['name'] = name
        if disciplines:
            query_parameters['disciplines'] = disciplines
        if statuses:
            query_parameters['statuses'] = statuses
        if scheduled_before:
            query_parameters['scheduled_before'] = scheduled_before
        if scheduled_after:
            query_parameters['scheduled_after'] = scheduled_after
        if countries:
            query_parameters['countries'] = countries
        if platforms:
            query_parameters['platforms'] = platforms
        if is_online:
            query_parameters['is_online'] = is_online
        if sort:
            query_parameters['sort'] = sort

        if not range.unit:
            range.unit = 'tournaments'

        headers = {
            'Range': range.get_header_value(),
        }

        content = self._simple_access(method, path, path_parameters = path_mapping, query_parameters = query_parameters,
                                      headers = headers)

        return [Tournament(**tour) for tour in content]


class AsyncViewerAPI(AsyncToornamentConnection):

    @staticmethod
    def _base_url():
        return 'https://api.toornament.com/viewer/v2'

    async def get_match(self, tournament_id, id):
        """Retrieve a single match of a tournament.
        Returns a match with all its games and opponents. In ffa matches only the first four opponents are included in each match game.

        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param id: The id of the match to retrieve."""

        tournament_id = str(tournament_id)
        id = str(id)

        method = 'GET'

        path = '/tournaments/{tournament_id}/matches/{id}'

        path_mapping = {
            'tournament_id': tournament_id,
            'id': id,
        }

        query_parameters = {
        }

        headers = {
        }

        content = await self._simple_access(method, path, path_parameters = path_mapping,
                                            query_parameters = query_parameters,
                                            headers = headers)

        return MatchDetailed(**content)

    async def get_matches_from_tournament(self, tournament_id, *, range: Range, stage_ids: Optional[list] = None,
                                          stage_numbers: Optional[list] = None, group_ids: Optional[list] = None,
                                          group_numbers: Optional[list] = None, round_ids: Optional[list] = None,
                                          round_numbers: Optional[list] = None, statuses: Optional[list] = None,
                                          is_scheduled: Optional[bool] = None, scheduled_before: Optional[str] = None,
                                          scheduled_after: Optional[str] = None, participant_ids: Optional[list] = None,
                                          sort: Optional[str] = None):
        """Retrieve matches of a tournament.
        Returns the matches of a tournament. In ffa matches only the first four opponents are included in each match.

        :param range: A range of requested items using the 'matches' unit. The size of the range can not exceed 128. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))
        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param stage_ids: One or several stage ids to filter.
        :param stage_numbers: One or several stage numbers to filter.
        :param group_ids: One or several group ids to filter.
        :param group_numbers: One or several group numbers to filter.
        :param round_ids: One or several round ids to filter.
        :param round_numbers: One or several round numbers to filter.
        :param statuses: One or several match statuses to filter.
        :param is_scheduled: Whether to include scheduled matches.
        :param scheduled_before: A datetime in RFC 3339 format (combined date, time and utc offset), to include all matches scheduled before or at the datetime.
        :param scheduled_after: A datetime in RFC 3339 format (combined date, time and utc offset), to include all matches scheduled after or at the datetime
        :param participant_ids: One or several participant ids involved in the matches to filter.
        :param sort: A method to sort the filtered data. "structure" sorts using the stage, group, round and match numbers. "schedule" sorts using the scheduled date. "latest results" sorts using the date at which the matches were played (not scheduled)."""

        tournament_id = str(tournament_id)
        stage_ids = [str(e) for e in stage_ids] if stage_ids else stage_ids
        group_ids = [str(e) for e in group_ids] if group_ids else group_ids
        round_ids = [str(e) for e in round_ids] if round_ids else round_ids
        participant_ids = [str(e) for e in participant_ids] if participant_ids else participant_ids

        method = 'GET'

        path = '/tournaments/{tournament_id}/matches'

        path_mapping = {
            'tournament_id': tournament_id,
        }

        query_parameters = {
        }
        if stage_ids:
            query_parameters['stage_ids'] = stage_ids
        if stage_numbers:
            query_parameters['stage_numbers'] = stage_numbers
        if group_ids:
            query_parameters['group_ids'] = group_ids
        if group_numbers:
            query_parameters['group_numbers'] = group_numbers
        if round_ids:
            query_parameters['round_ids'] = round_ids
        if round_numbers:
            query_parameters['round_numbers'] = round_numbers
        if statuses:
            query_parameters['statuses'] = statuses
        if is_scheduled:
            query_parameters['is_scheduled'] = is_scheduled
        if scheduled_before:
            query_parameters['scheduled_before'] = scheduled_before
        if scheduled_after:
            query_parameters['scheduled_after'] = scheduled_after
        if participant_ids:
            query_parameters['participant_ids'] = participant_ids
        if sort:
            query_parameters['sort'] = sort

        if not range.unit:
            range.unit = 'matches'

        headers = {
            'Range': range.get_header_value(),
        }

        content = await self._simple_access(method, path, path_parameters = path_mapping,
                                            query_parameters = query_parameters,
                                            headers = headers)

        return [Match(**match) for match in content]

    async def get_matches_from_discipline(self, discipline_id, *, range: Range, is_featured: Optional[bool] = None,
                                          statuses: Optional[list] = None, scheduled_before: Optional[str] = None,
                                          scheduled_after: Optional[str] = None, participant_ids: Optional[list] = None,
                                          tournament_ids: Optional[list] = None, sort: Optional[str] = None):
        """Retrieve matches of a discipline, regardless of their tournament.
        Returns matches of a discipline. In ffa matches only the first four opponents are included in each match game.

        :param range: A range of requested items using the 'matches' unit. The size of the range can not exceed 128. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))
        :param discipline_id: The string id of the discipline.
        :param is_featured: Whether to include featured tournaments.
        :param statuses: One or several match statuses to filter.
        :param scheduled_before: A datetime in RFC 3339 format (combined date, time and utc offset), to include all matches scheduled before or at the datetime.
        :param scheduled_after: A datetime in RFC 3339 format (combined date, time and utc offset), to include all matches scheduled after or at the datetime
        :param participant_ids: One or several participant ids involved in the matches to filter.
        :param tournament_ids: List of tournament IDs to filter the data with.
        :param sort: A method to sort the filtered data. "structure" sorts using the stage, group, round and match numbers. "schedule" sorts using the scheduled date. "latest results" sorts using the date at which the matches were played (not scheduled)."""

        discipline_id = str(discipline_id)
        participant_ids = [str(e) for e in participant_ids] if participant_ids else participant_ids
        tournament_ids = [str(e) for e in tournament_ids] if tournament_ids else tournament_ids

        method = 'GET'

        path = '/disciplines/{discipline_id}/matches'

        path_mapping = {
            'discipline_id': discipline_id,
        }

        query_parameters = {
        }
        if is_featured:
            query_parameters['is_featured'] = is_featured
        if statuses:
            query_parameters['statuses'] = statuses
        if scheduled_before:
            query_parameters['scheduled_before'] = scheduled_before
        if scheduled_after:
            query_parameters['scheduled_after'] = scheduled_after
        if participant_ids:
            query_parameters['participant_ids'] = participant_ids
        if tournament_ids:
            query_parameters['tournament_ids'] = tournament_ids
        if sort:
            query_parameters['sort'] = sort

        if not range.unit:
            range.unit = 'matches'

        headers = {
            'Range': range.get_header_value(),
        }

        content = await self._simple_access(method, path, path_parameters = path_mapping,
                                            query_parameters = query_parameters,
                                            headers = headers)

        return [MatchDiscipline(**match) for match in content]

    async def get_bracket_nodes(self, tournament_id, stage_id, *, range: Range, group_ids: Optional[list] = None,
                                group_numbers: Optional[list] = None, round_ids: Optional[list] = None,
                                round_numbers: Optional[list] = None, min_depth: Optional[int] = None,
                                max_depth: Optional[int] = None):
        """Retrieve bracket nodes of a stage and tournament.
        Returns the bracket nodes of a stage. A bracket node represents a match and some extra data.

        :param range: A range of requested items using the 'nodes' unit. The size of the range can not exceed 128. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))
        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param stage_id: The id of the stage you want to retrieve data about.
        :param group_ids: A list of group ids to filter.
        :param group_numbers: A list of group numbers to filter.
        :param round_ids: A list of round ids to filter.
        :param round_numbers: A list of round numbers to filter.
        :param min_depth: A minimum depth to filter.
        :param max_depth: A maximal depth to filter."""

        tournament_id = str(tournament_id)
        stage_id = str(stage_id)
        group_ids = [str(e) for e in group_ids] if group_ids else group_ids
        round_ids = [str(e) for e in round_ids] if round_ids else round_ids

        method = 'GET'

        path = '/tournaments/{tournament_id}/stages/{stage_id}/bracket-nodes'

        path_mapping = {
            'tournament_id': tournament_id,
            'stage_id': stage_id,
        }

        query_parameters = {
        }
        if group_ids:
            query_parameters['group_ids'] = group_ids
        if group_numbers:
            query_parameters['group_numbers'] = group_numbers
        if round_ids:
            query_parameters['round_ids'] = round_ids
        if round_numbers:
            query_parameters['round_numbers'] = round_numbers
        if min_depth:
            query_parameters['min_depth'] = min_depth
        if max_depth:
            query_parameters['max_depth'] = max_depth

        if not range.unit:
            range.unit = 'nodes'

        headers = {
            'Range': range.get_header_value(),
        }

        content = await self._simple_access(method, path, path_parameters = path_mapping,
                                            query_parameters = query_parameters,
                                            headers = headers)

        return [BracketNode(**node) for node in content]

    async def get_custom_fields(self, tournament_id, *, target_type: Optional[str] = None):
        """Retrieves custom fields of a tournament.
        Returns the complete definition of all custom fields for a given tournament. This includes both public and private custom fields.
        A custom field may be associated to a player, a team or a team's player. For more information, please read the [Custom Fields](https://developer.toornament.com/v2/core-concepts/custom-fields) documentation.

        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param target_type: The entity affected by the custom fields."""

        tournament_id = str(tournament_id)

        method = 'GET'

        path = '/tournaments/{tournament_id}/custom-fields'

        path_mapping = {
            'tournament_id': tournament_id,
        }

        query_parameters = {
        }
        if target_type:
            query_parameters['target_type'] = target_type

        headers = {
        }

        content = await self._simple_access(method, path, path_parameters = path_mapping,
                                            query_parameters = query_parameters,
                                            headers = headers)

        return [CustomField(**field) for field in content]

    async def get_disciplines(self, *, range: Range):
        """Retrieve the list of available disciplines and their basic information.
        Returns a collection of disciplines.

        :param range
        A range of requested items using the 'disciplines' unit.
        The size of the range can not exceed 50. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))"""

        method = 'GET'

        path = '/disciplines'

        path_mapping = {
        }

        query_parameters = {
        }

        if not range.unit:
            range.unit = 'disciplines'

        headers = {
            'Range': range.get_header_value(),
        }

        content = await self._simple_access(method, path, path_parameters = path_mapping,
                                            query_parameters = query_parameters,
                                            headers = headers)

        return [Discipline(**discipline) for discipline in content]

    async def get_discipline(self, id):
        """Retrieve a specific discipline, with advanced information.
        Returns a discipline with its information and configuration options.

        :param id: The string id of the discipline."""

        id = str(id)

        method = 'GET'

        path = '/disciplines/{id}'

        path_mapping = {
            'id': id,
        }

        query_parameters = {
        }

        headers = {
        }

        content = await self._simple_access(method, path, path_parameters = path_mapping,
                                            query_parameters = query_parameters,
                                            headers = headers)

        return DisciplineDetailed(**content)

    async def get_groups(self, tournament_id, *, range: Range, stage_ids: Optional[list] = None,
                         stage_numbers: Optional[list] = None):
        """Retrieve all groups of a tournament.
        Returns all groups of a tournament with basic information and settings.

        :param range: A range of requested items using the 'groups' unit. The size of the range can not exceed 50. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))
        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param stage_ids: A list of stage ids to filter.
        :param stage_numbers: A list of stage numbers to filter."""

        tournament_id = str(tournament_id)
        stage_ids = [str(e) for e in stage_ids] if stage_ids else stage_ids

        method = 'GET'

        path = '/tournaments/{tournament_id}/groups'

        path_mapping = {
            'tournament_id': tournament_id,
        }

        query_parameters = {
        }
        if stage_ids:
            query_parameters['stage_ids'] = stage_ids
        if stage_numbers:
            query_parameters['stage_numbers'] = stage_numbers

        if not range.unit:
            range.unit = 'groups'

        headers = {
            'Range': range.get_header_value(),
        }

        content = await self._simple_access(method, path, path_parameters = path_mapping,
                                            query_parameters = query_parameters,
                                            headers = headers)

        return [Group(**group) for group in content]

    async def get_group(self, tournament_id, id):
        """Retrieve a single group of a tournament.
        Returns a group with the given id with basic information and settings.

        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param id: The id of the group to retrieve."""

        tournament_id = str(tournament_id)
        id = str(id)

        method = 'GET'

        path = '/tournaments/{tournament_id}/groups/{id}'

        path_mapping = {
            'tournament_id': tournament_id,
            'id': id,
        }

        query_parameters = {
        }

        headers = {
        }

        content = await self._simple_access(method, path, path_parameters = path_mapping,
                                            query_parameters = query_parameters,
                                            headers = headers)

        return Group(**content)

    async def get_game(self, tournament_id, match_id, number):
        """Retrieve a single game of a match.
        Returns detailed information about one match game.

        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param match_id: The id of the match to retrieve.
        :param number: The relative identifier of the match game to retrieve."""

        tournament_id = str(tournament_id)
        match_id = str(match_id)

        method = 'GET'

        path = '/tournaments/{tournament_id}/matches/{match_id}/games/{number}'

        path_mapping = {
            'tournament_id': tournament_id,
            'match_id': match_id,
            'number': number,
        }

        query_parameters = {
        }

        headers = {
        }

        content = await self._simple_access(method, path, path_parameters = path_mapping,
                                            query_parameters = query_parameters,
                                            headers = headers)

        return Game(**content)

    async def get_participants(self, tournament_id, *, range: Range, name: Optional[str] = None,
                               sort: Optional[str] = None):
        """Retrieve the participants of a tournament.
        Returns the participants of the given tournament. The data provided in the participant depends on whether the participant type is team or player. This setting can be found in the tournament.

        :param range: A range of requested items using the 'participants' unit. The size of the range can not exceed 50. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))
        :param tournament_id: The id of the tournament the participants are from.
        :param name: The string to be looked for in the name of the participant.
        :param sort: A method to sort the filtered data. “created_asc” and “created_desc” sort the participants from their creation date (earliest to latest, and inversely). “Alphabetic” sorts the participants using their case-insensitive names."""

        tournament_id = str(tournament_id)

        method = 'GET'

        path = '/tournaments/{tournament_id}/participants'

        path_mapping = {
            'tournament_id': tournament_id,
        }

        query_parameters = {
        }
        if name:
            query_parameters['name'] = name
        if sort:
            query_parameters['sort'] = sort

        if not range.unit:
            range.unit = 'participants'

        headers = {
            'Range': range.get_header_value(),
        }

        content = await self._simple_access(method, path, path_parameters = path_mapping,
                                            query_parameters = query_parameters,
                                            headers = headers)

        return [
            ParticipantPlayer(**participant) if participant.get('lineup') is None else ParticipantTeam(**participant)
            for participant in content]

    async def get_participant(self, tournament_id, id):
        """Retrieve a single participant of a tournament.
        Returns a participant identified with the given id. The data provided in the participant depends on whether the participant type is team or player. This setting can be found in the tournament.

        :param tournament_id: The id of the tournament the participants are from.
        :param id: The id of the participant to retrieve."""

        tournament_id = str(tournament_id)
        id = str(id)

        method = 'GET'

        path = '/tournaments/{tournament_id}/participants/{id}'

        path_mapping = {
            'tournament_id': tournament_id,
            'id': id,
        }

        query_parameters = {
        }

        headers = {
        }

        content = await self._simple_access(method, path, path_parameters = path_mapping,
                                            query_parameters = query_parameters,
                                            headers = headers)

        return ParticipantPlayer(**content) if content.get('lineup') is None else ParticipantTeam(**content)

    async def get_playlist(self, id):
        """Retrieve a single playlist.
        Returns a playlist identified with the given id.

        :param id: The id of the playlist to retrieve."""

        id = str(id)

        method = 'GET'

        path = '/playlists/{id}'

        path_mapping = {
            'id': id,
        }

        query_parameters = {
        }

        headers = {
        }

        content = await self._simple_access(method, path, path_parameters = path_mapping,
                                            query_parameters = query_parameters,
                                            headers = headers)

        return Playlist(**content)

    async def get_ranking_items(self, tournament_id, stage_id, *, range: Range, group_ids: Optional[list] = None,
                                group_numbers: Optional[list] = None):
        """Retrieve ranking items of a stage and tournament.
        Returns ranking items of a stage with a small summary of the associated participant in the ranking. The items are always ordered by ascending position.

        :param range: A range of requested items using the 'items' unit. The size of the range can not exceed 50. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))
        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param stage_id: The id of the stage you want to retrieve data about.
        :param group_ids: A list of group ids to filter.
        :param group_numbers: A list of group numbers to filter."""

        tournament_id = str(tournament_id)
        stage_id = str(stage_id)
        group_ids = [str(e) for e in group_ids] if group_ids else group_ids

        method = 'GET'

        path = '/tournaments/{tournament_id}/stages/{stage_id}/ranking-items'

        path_mapping = {
            'tournament_id': tournament_id,
            'stage_id': stage_id,
        }

        query_parameters = {
        }
        if group_ids:
            query_parameters['group_ids'] = group_ids
        if group_numbers:
            query_parameters['group_numbers'] = group_numbers

        if not range.unit:
            range.unit = 'items'

        headers = {
            'Range': range.get_header_value(),
        }

        content = await self._simple_access(method, path, path_parameters = path_mapping,
                                            query_parameters = query_parameters,
                                            headers = headers)

        return [RankingItem(**item) for item in content]

    async def get_rounds(self, tournament_id, *, range: Range, stage_ids: Optional[list] = None,
                         stage_numbers: Optional[list] = None, group_ids: Optional[list] = None,
                         group_numbers: Optional[list] = None):
        """Retrieve all rounds of a tournament.
        Returns all rounds of a tournament with basic information and settings.

        :param range: A range of requested items using the 'rounds' unit. The size of the range can not exceed 50. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))
        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param stage_ids: A list of stage ids to filter.
        :param stage_numbers: A list of stage numbers to filter.
        :param group_ids: A list of group ids to filter.
        :param group_numbers: A list of group numbers to filter."""

        tournament_id = str(tournament_id)
        stage_ids = [str(e) for e in stage_ids] if stage_ids else stage_ids
        group_ids = [str(e) for e in group_ids] if group_ids else group_ids

        method = 'GET'

        path = '/tournaments/{tournament_id}/rounds'

        path_mapping = {
            'tournament_id': tournament_id,
        }

        query_parameters = {
        }
        if stage_ids:
            query_parameters['stage_ids'] = stage_ids
        if stage_numbers:
            query_parameters['stage_numbers'] = stage_numbers
        if group_ids:
            query_parameters['group_ids'] = group_ids
        if group_numbers:
            query_parameters['group_numbers'] = group_numbers

        if not range.unit:
            range.unit = 'rounds'

        headers = {
            'Range': range.get_header_value(),
        }

        content = await self._simple_access(method, path, path_parameters = path_mapping,
                                            query_parameters = query_parameters,
                                            headers = headers)

        return [Round(**round) for round in content]

    async def get_round(self, tournament_id, id):
        """Retrieve a single round of a tournament.
        Returns a round with the given id with basic information and settings.

        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param id: The id of the round to retrieve."""

        tournament_id = str(tournament_id)
        id = str(id)

        method = 'GET'

        path = '/tournaments/{tournament_id}/rounds/{id}'

        path_mapping = {
            'tournament_id': tournament_id,
            'id': id,
        }

        query_parameters = {
        }

        headers = {
        }

        content = await self._simple_access(method, path, path_parameters = path_mapping,
                                            query_parameters = query_parameters,
                                            headers = headers)

        return Round(**content)

    async def get_stages(self, tournament_id):
        """Retrieve all stages of a tournament.
        Returns all stages of a tournament with basic information and settings.

        :param tournament_id: The id of the tournament you want to retrieve data about."""

        tournament_id = str(tournament_id)

        method = 'GET'

        path = '/tournaments/{tournament_id}/stages'

        path_mapping = {
            'tournament_id': tournament_id,
        }

        query_parameters = {
        }

        headers = {
        }

        content = await self._simple_access(method, path, path_parameters = path_mapping,
                                            query_parameters = query_parameters,
                                            headers = headers)

        return [Stage(**stage) for stage in content]

    async def get_stage(self, tournament_id, id):
        """Retrieve a single stage of a tournament.
        Returns a stage with the given id with basic information and settings.

        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param id: The id of the stage to retrieve."""

        tournament_id = str(tournament_id)
        id = str(id)

        method = 'GET'

        path = '/tournaments/{tournament_id}/stages/{id}'

        path_mapping = {
            'tournament_id': tournament_id,
            'id': id,
        }

        query_parameters = {
        }

        headers = {
        }

        content = await self._simple_access(method, path, path_parameters = path_mapping,
                                            query_parameters = query_parameters,
                                            headers = headers)

        return Stage(**content)

    async def get_standings(self, *, range: Range, tournament_ids: list, participant_ids: Optional[list] = None):
        """Retrieve a list of final standing items.
        Returns a list of final standing items.

        :param range: A range of requested items using the 'items' unit. The size of the range can not exceed 50. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))
        :param tournament_ids: Only return tournaments for the given list of ids.
        :param participant_ids: One or several participant ids involved in the standings to filter."""

        tournament_ids = [str(e) for e in tournament_ids]
        participant_ids = [str(e) for e in participant_ids] if participant_ids else participant_ids

        method = 'GET'

        path = '/standings'

        path_mapping = {
        }

        query_parameters = {
            'tournament_ids': tournament_ids,
        }
        if participant_ids:
            query_parameters['participant_ids'] = participant_ids

        if not range.unit:
            range.unit = 'items'

        headers = {
            'Range': range.get_header_value(),
        }

        content = await self._simple_access(method, path, path_parameters = path_mapping,
                                            query_parameters = query_parameters,
                                            headers = headers)

        return [StandingItem(**item) for item in content]

    async def get_streams(self, tournament_id, *, range: Range, match_ids: Optional[list] = None):
        """Retrieves available streams.
        Returns the streams of the given tournament.

        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param range: A range of requested items using the 'streams' unit. The size of the range can not exceed 50. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))
        :param match_ids: A list of match ids to filter."""

        tournament_id = str(tournament_id)
        match_ids = [str(e) for e in match_ids] if match_ids else match_ids

        method = 'GET'

        path = '/tournaments/{tournament_id}/streams'

        path_mapping = {
            'tournament_id': tournament_id,
        }

        query_parameters = {
        }
        if match_ids:
            query_parameters['match_ids'] = match_ids

        if not range.unit:
            range.unit = 'streams'

        headers = {
            'Range': range.get_header_value(),
        }

        content = await self._simple_access(method, path, path_parameters = path_mapping,
                                            query_parameters = query_parameters,
                                            headers = headers)

        return [Stream(**stream) for stream in content]

    async def get_videos(self, tournament_id, *, range: Range, participant_ids: Optional[list] = None,
                         category: Optional[str] = None, sort: Optional[str] = None):
        """Retrieve videos of a tournament.
        Returns the videos of the given tournament.

        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param range: A range of requested items using the 'videos' unit. The size of the range can not exceed 50. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))
        :param participant_ids: One or several participant ids to filter.
        :param category: The category of the videos.
        :param sort: Sorts the collection in a particular order. "created_asc" sorts the videos from the oldest to the most recent one; "created_desc" sorts the videos from the most recent to the oldest one."""

        tournament_id = str(tournament_id)
        participant_ids = [str(e) for e in participant_ids] if participant_ids else participant_ids

        method = 'GET'

        path = '/tournaments/{tournament_id}/videos'

        path_mapping = {
            'tournament_id': tournament_id,
        }

        query_parameters = {
        }
        if participant_ids:
            query_parameters['participant_ids'] = participant_ids
        if category:
            query_parameters['category'] = category
        if sort:
            query_parameters['sort'] = sort

        if not range.unit:
            range.unit = 'videos'

        headers = {
            'Range': range.get_header_value(),
        }

        content = await self._simple_access(method, path, path_parameters = path_mapping,
                                            query_parameters = query_parameters,
                                            headers = headers)

        return [VideoTournament(**video) for video in content]

    async def get_videos_by_match(self, tournament_id, match_id, *, category: Optional[str] = None,
                                  sort: Optional[str] = None):
        """Retrieve videos of a match.
        Returns the videos of the given match.

        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param match_id: The id of the match to retrieve.
        :param category: The category of the videos.
        :param sort: Sorts the collection in a particular order. "created_asc" sorts the videos from the oldest to the most recent one; "created_desc" sorts the videos from the most recent to the oldest one."""

        tournament_id = str(tournament_id)
        match_id = str(match_id)

        method = 'GET'

        path = '/tournaments/{tournament_id}/matches/{match_id}/videos'

        path_mapping = {
            'tournament_id': tournament_id,
            'match_id': match_id,
        }

        query_parameters = {
        }
        if category:
            query_parameters['category'] = category
        if sort:
            query_parameters['sort'] = sort

        headers = {
        }

        content = await self._simple_access(method, path, path_parameters = path_mapping,
                                            query_parameters = query_parameters,
                                            headers = headers)

        return [Video(**video) for video in content]

    async def get_tournaments_featured(self, *, range: Range, name: Optional[str] = None,
                                       disciplines: Optional[str] = None,
                                       statuses: Optional[str] = None, scheduled_before: Optional[str] = None,
                                       scheduled_after: Optional[str] = None, countries: Optional[str] = None,
                                       platforms: Optional[str] = None, is_online: Optional[int] = None,
                                       sort: Optional[str] = None):
        """Retrieve published featured tournaments.
        Returns a collection of published featured tournaments.

        :param range: A range of requested items using the 'tournaments' unit. The size of the range can not exceed 50. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))
        :param name: The string to be looked for in the name or full name.
        :param disciplines: One or several disciplines to filter.
        :param statuses: One or several tournament statuses to filter.
        :param scheduled_before: A date to include all tournaments scheduled to take place before or at the date, in ISO 8601 format (only the date part, with YYYY-MM-DD pattern).
        :param scheduled_after: A date to include all tournaments scheduled to take place after or at the date, in ISO 8601 format (only the date part, with YYYY-MM-DD pattern).
        :param countries: One or several countries to filter in ISO 3166-1 alpha-2 country codes format (some codes may not be supported)
        :param platforms: One or several platforms to filter.
        :param is_online: Whether the tournament is played online.
        :param sort: Sorts the collection in a particular order. "scheduled_asc" sorts the tournaments by scheduled date from the oldest to the most recent one; "scheduled_desc" sorts the tournaments by scheduled date from the most recent to the oldest one."""

        method = 'GET'

        path = '/tournaments/featured'

        path_mapping = {
        }

        query_parameters = {
        }
        if name:
            query_parameters['name'] = name
        if disciplines:
            query_parameters['disciplines'] = disciplines
        if statuses:
            query_parameters['statuses'] = statuses
        if scheduled_before:
            query_parameters['scheduled_before'] = scheduled_before
        if scheduled_after:
            query_parameters['scheduled_after'] = scheduled_after
        if countries:
            query_parameters['countries'] = countries
        if platforms:
            query_parameters['platforms'] = platforms
        if is_online:
            query_parameters['is_online'] = is_online
        if sort:
            query_parameters['sort'] = sort

        if not range.unit:
            range.unit = 'tournaments'

        headers = {
            'Range': range.get_header_value(),
        }

        content = await self._simple_access(method, path, path_parameters = path_mapping,
                                            query_parameters = query_parameters,
                                            headers = headers)

        return [Tournament(**tour) for tour in content]

    async def get_tournament(self, id):
        """Retrieve a single tournament.
        Returns a tournament identified with the given id.

        :param id: The id of the tournament to retrieve."""

        id = str(id)

        method = 'GET'

        path = '/tournaments/{id}'

        path_mapping = {
            'id': id,
        }

        query_parameters = {
        }

        headers = {
        }

        content = await self._simple_access(method, path, path_parameters = path_mapping,
                                            query_parameters = query_parameters,
                                            headers = headers)

        return TournamentDetailed(**content)

    async def get_tournaments_by_playlist(self, id, *, range: Range, name: Optional[str] = None,
                                          disciplines: Optional[str] = None, statuses: Optional[str] = None,
                                          scheduled_before: Optional[str] = None, scheduled_after: Optional[str] = None,
                                          countries: Optional[str] = None, platforms: Optional[str] = None,
                                          is_online: Optional[int] = None, sort: Optional[str] = None):
        """Retrieve the tournaments of a playlist.
        Returns the tournaments of a playlist.

        :param range: A range of requested items using the 'tournaments' unit. The size of the range can not exceed 50. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))
        :param id: The string id of the tournament.
        :param name: The string to be looked for in the name or full name.
        :param disciplines: One or several disciplines to filter.
        :param statuses: One or several tournament statuses to filter.
        :param scheduled_before: A date to include all tournaments scheduled to take place before or at the date, in ISO 8601 format (only the date part, with YYYY-MM-DD pattern).
        :param scheduled_after: A date to include all tournaments scheduled to take place after or at the date, in ISO 8601 format (only the date part, with YYYY-MM-DD pattern).
        :param countries: One or several countries to filter in ISO 3166-1 alpha-2 country codes format (some codes may not be supported)
        :param platforms: One or several platforms to filter.
        :param is_online: Whether the tournament is played online.
        :param sort: Sorts the collection in a particular order. "scheduled_asc" sorts the tournaments by scheduled date from the oldest to the most recent one; "scheduled_desc" sorts the tournaments by scheduled date from the most recent to the oldest one."""

        id = str(id)

        method = 'GET'

        path = '/playlists/{id}/tournaments'

        path_mapping = {
            'id': id,
        }

        query_parameters = {
        }
        if name:
            query_parameters['name'] = name
        if disciplines:
            query_parameters['disciplines'] = disciplines
        if statuses:
            query_parameters['statuses'] = statuses
        if scheduled_before:
            query_parameters['scheduled_before'] = scheduled_before
        if scheduled_after:
            query_parameters['scheduled_after'] = scheduled_after
        if countries:
            query_parameters['countries'] = countries
        if platforms:
            query_parameters['platforms'] = platforms
        if is_online:
            query_parameters['is_online'] = is_online
        if sort:
            query_parameters['sort'] = sort

        if not range.unit:
            range.unit = 'tournaments'

        headers = {
            'Range': range.get_header_value(),
        }

        content = await self._simple_access(method, path, path_parameters = path_mapping,
                                            query_parameters = query_parameters,
                                            headers = headers)

        return [Tournament(**tour) for tour in content]
