from .toornament_connection import SyncToornamentConnection
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

        :param tournament_id The id of the tournament you want to retrieve data about.
        :param id The id of the match to retrieve."""

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

        :param range A range of requested items using the 'matches' unit. The size of the range can not exceed 128. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))
        :param tournament_id The id of the tournament you want to retrieve data about.
        :param stage_ids One or several stage ids to filter.
        :param stage_numbers One or several stage numbers to filter.
        :param group_ids One or several group ids to filter.
        :param group_numbers One or several group numbers to filter.
        :param round_ids One or several round ids to filter.
        :param round_numbers One or several round numbers to filter.
        :param statuses One or several match statuses to filter.
        :param is_scheduled Whether to include scheduled matches.
        :param scheduled_before A datetime in RFC 3339 format (combined date, time and utc offset), to include all matches scheduled before or at the datetime.
        :param scheduled_after A datetime in RFC 3339 format (combined date, time and utc offset), to include all matches scheduled after or at the datetime
        :param participant_ids One or several participant ids involved in the matches to filter.
        :param sort A method to sort the filtered data. "structure" sorts using the stage, group, round and match numbers. "schedule" sorts using the scheduled date. "latest results" sorts using the date at which the matches were played (not scheduled)."""

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

    def get_matches_from_discipline(self, discipline_id, *, range: Range, is_featured: Optional[bool]=None, statuses: Optional[list]=None, scheduled_before: Optional[str]=None, scheduled_after: Optional[str]=None, participant_ids: Optional[list]=None, tournament_ids: Optional[list]=None, sort: Optional[str]=None):
        """Retrieve matches of a discipline, regardless of their tournament.
        Returns matches of a discipline. In ffa matches only the first four opponents are included in each match game.

        :param range A range of requested items using the 'matches' unit. The size of the range can not exceed 128. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))
        :param discipline_id The string id of the discipline.
        :param is_featured Whether to include featured tournaments.
        :param statuses One or several match statuses to filter.
        :param scheduled_before A datetime in RFC 3339 format (combined date, time and utc offset), to include all matches scheduled before or at the datetime.
        :param scheduled_after A datetime in RFC 3339 format (combined date, time and utc offset), to include all matches scheduled after or at the datetime
        :param participant_ids One or several participant ids involved in the matches to filter.
        :param tournament_ids List of tournament IDs to filter the data with.
        :param sort A method to sort the filtered data. "structure" sorts using the stage, group, round and match numbers. "schedule" sorts using the scheduled date. "latest results" sorts using the date at which the matches were played (not scheduled)."""

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

        content = self._simple_access(method, path, path_parameters = path_mapping, query_parameters = query_parameters, headers = headers)

        return [MatchDiscipline(**match) for match in content]

    def get_bracket_nodes(self, tournament_id, stage_id, *, range: Range, group_ids: Optional[list]=None, group_numbers: Optional[list]=None, round_ids: Optional[list]=None, round_numbers: Optional[list]=None, min_depth: Optional[int]=None, max_depth: Optional[int]=None):
        """Retrieve bracket nodes of a stage and tournament.
        Returns the bracket nodes of a stage. A bracket node represents a match and some extra data.

        :param range A range of requested items using the 'nodes' unit. The size of the range can not exceed 128. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))
        :param tournament_id The id of the tournament you want to retrieve data about.
        :param stage_id The id of the stage you want to retrieve data about.
        :param group_ids A list of group ids to filter.
        :param group_numbers A list of group numbers to filter.
        :param round_ids A list of round ids to filter.
        :param round_numbers A list of round numbers to filter.
        :param min_depth A minimum depth to filter.
        :param max_depth A maximal depth to filter."""

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

        content = self._simple_access(method, path, path_parameters = path_mapping, query_parameters = query_parameters, headers = headers)

        return [BracketNode(**node) for node in content]

    def get_custom_fields(self, tournament_id, *, target_type: Optional[str]=None):
        """Retrieves custom fields of a tournament.
        Returns the complete definition of all custom fields for a given tournament. This includes both public and private custom fields.
        A custom field may be associated to a player, a team or a team's player. For more information, please read the [Custom Fields](https://developer.toornament.com/v2/core-concepts/custom-fields) documentation.

        :param tournament_id The id of the tournament you want to retrieve data about.
        :param target_type The entity affected by the custom fields."""

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

        content = self._simple_access(method, path, path_parameters = path_mapping, query_parameters = query_parameters, headers = headers)

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

        content = self._simple_access(method, path, path_parameters = path_mapping, query_parameters = query_parameters, headers = headers)

        return [Discipline(**discipline) for discipline in content]

    def get_discipline(self, id):
        """Retrieve a specific discipline, with advanced information.
        Returns a discipline with its information and configuration options.

        :param id The string id of the discipline."""

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

        content = self._simple_access(method, path, path_parameters = path_mapping, query_parameters = query_parameters, headers = headers)

        return DisciplineDetailed(**content)
