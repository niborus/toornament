from .toornament_connection import SyncToornamentConnection, AsyncToornamentConnection
from typing import Optional, List
from .range import Range


class SyncViewerAPI(SyncToornamentConnection):

    @staticmethod
    def _base_url():
        return 'https://api.toornament.com/viewer/v2'

    def get_match(self, tournament_id, id, **request_arguments):
        """Retrieve a single match of a tournament.
        Returns a match with all its games and opponents. In ffa matches only the first four opponents are included in each match game.

        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param id: The id of the match to retrieve."""

        return self._access(
            'viewer_get_match', request_arguments,
            tournament_id = tournament_id,
            id = id,
        )

    def get_matches_from_tournament(self, tournament_id, *, range: Range, stage_ids: Optional[list] = None,
                                    stage_numbers: Optional[list] = None, group_ids: Optional[list] = None,
                                    group_numbers: Optional[list] = None, round_ids: Optional[list] = None,
                                    round_numbers: Optional[list] = None, statuses: Optional[list] = None,
                                    is_scheduled: Optional[bool] = None, scheduled_before: Optional[str] = None,
                                    scheduled_after: Optional[str] = None, participant_ids: Optional[list] = None,
                                    sort: Optional[str] = None, **request_arguments):
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

        return self._access(
            'viewer_get_matches_from_tournament', request_arguments,
            tournament_id = tournament_id,
            range = range,
            stage_ids = stage_ids,
            stage_numbers = stage_numbers,
            group_ids = group_ids,
            group_numbers = group_numbers,
            round_ids = round_ids,
            round_numbers = round_numbers,
            statuses = statuses,
            is_scheduled = is_scheduled,
            scheduled_before = scheduled_before,
            scheduled_after = scheduled_after,
            participant_ids = participant_ids,
            sort = sort,
        )

    def get_matches_from_discipline(self, discipline_id, *, range: Range, is_featured: Optional[bool] = None,
                                    statuses: Optional[list] = None, scheduled_before: Optional[str] = None,
                                    scheduled_after: Optional[str] = None, participant_ids: Optional[list] = None,
                                    tournament_ids: Optional[list] = None, sort: Optional[str] = None,
                                    **request_arguments):
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

        return self._access(
            'viewer_get_matches_from_discipline', request_arguments,
            discipline_id = discipline_id,
            range = range,
            is_featured = is_featured,
            statuses = statuses,
            scheduled_before = scheduled_before,
            scheduled_after = scheduled_after,
            participant_ids = participant_ids,
            tournament_ids = tournament_ids,
            sort = sort,
        )

    def get_bracket_nodes(self, tournament_id, stage_id, *, range: Range, group_ids: Optional[list] = None,
                          group_numbers: Optional[list] = None, round_ids: Optional[list] = None,
                          round_numbers: Optional[list] = None, min_depth: Optional[int] = None,
                          max_depth: Optional[int] = None, **request_arguments):
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

        return self._access(
            'viewer_get_bracket_nodes', request_arguments,
            tournament_id = tournament_id,
            stage_id = stage_id,
            range = range,
            group_ids = group_ids,
            group_numbers = group_numbers,
            round_ids = round_ids,
            round_numbers = round_numbers,
            min_depth = min_depth,
            max_depth = max_depth,
        )

    def get_custom_fields(self, tournament_id, *, target_type: Optional[str] = None, **request_arguments):
        """Retrieves custom fields of a tournament.
        Returns the complete definition of all custom fields for a given tournament. This includes both public and private custom fields.
        A custom field may be associated to a player, a team or a team's player. For more information, please read the [Custom Fields](https://developer.toornament.com/v2/core-concepts/custom-fields) documentation.

        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param target_type: The entity affected by the custom fields."""

        return self._access(
            'viewer_get_custom_fields', request_arguments,
            tournament_id = tournament_id,
            target_type = target_type,
        )

    def get_disciplines(self, *, range: Range, **request_arguments):
        """Retrieve the list of available disciplines and their basic information.
        Returns a collection of disciplines.

        :param range
        A range of requested items using the 'disciplines' unit.
        The size of the range can not exceed 50. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))"""

        return self._access(
            'viewer_get_disciplines', request_arguments,
            range = range,
        )

    def get_discipline(self, id, **request_arguments):
        """Retrieve a specific discipline, with advanced information.
        Returns a discipline with its information and configuration options.

        :param id: The string id of the discipline."""

        return self._access(
            'viewer_get_discipline', request_arguments,
            id = id,
        )

    def get_groups(self, tournament_id, *, range: Range, stage_ids: Optional[list] = None,
                   stage_numbers: Optional[list] = None, **request_arguments):
        """Retrieve all groups of a tournament.
        Returns all groups of a tournament with basic information and settings.

        :param range: A range of requested items using the 'groups' unit. The size of the range can not exceed 50. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))
        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param stage_ids: A list of stage ids to filter.
        :param stage_numbers: A list of stage numbers to filter."""

        return self._access(
            'viewer_get_groups', request_arguments,
            tournament_id = tournament_id,
            range = range,
            stage_ids = stage_ids,
            stage_numbers = stage_numbers,
        )

    def get_group(self, tournament_id, id, **request_arguments):
        """Retrieve a single group of a tournament.
        Returns a group with the given id with basic information and settings.

        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param id: The id of the group to retrieve."""

        return self._access(
            'viewer_get_group', request_arguments,
            tournament_id = tournament_id,
            id = id,
        )

    def get_game(self, tournament_id, match_id, number, **request_arguments):
        """Retrieve a single game of a match.
        Returns detailed information about one match game.

        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param match_id: The id of the match to retrieve.
        :param number: The relative identifier of the match game to retrieve."""

        return self._access(
            'viewer_get_game', request_arguments,
            tournament_id = tournament_id,
            match_id = match_id,
            number = number,
        )

    def get_participants(self, tournament_id, *, range: Range, name: Optional[str] = None, sort: Optional[str] = None,
                         **request_arguments):
        """Retrieve the participants of a tournament.
        Returns the participants of the given tournament. The data provided in the participant depends on whether the participant type is team or player. This setting can be found in the tournament.

        :param range: A range of requested items using the 'participants' unit. The size of the range can not exceed 50. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))
        :param tournament_id: The id of the tournament the participants are from.
        :param name: The string to be looked for in the name of the participant.
        :param sort: A method to sort the filtered data. “created_asc” and “created_desc” sort the participants from their creation date (earliest to latest, and inversely). “Alphabetic” sorts the participants using their case-insensitive names."""

        return self._access(
            'viewer_get_participants', request_arguments,
            tournament_id = tournament_id,
            range = range,
            name = name,
            sort = sort,
        )

    def get_participant(self, tournament_id, id, **request_arguments):
        """Retrieve a single participant of a tournament.
        Returns a participant identified with the given id. The data provided in the participant depends on whether the participant type is team or player. This setting can be found in the tournament.

        :param tournament_id: The id of the tournament the participants are from.
        :param id: The id of the participant to retrieve."""

        return self._access(
            'viewer_get_participant', request_arguments,
            tournament_id = tournament_id,
            id = id,
        )

    def get_playlist(self, id, **request_arguments):
        """Retrieve a single playlist.
        Returns a playlist identified with the given id.

        :param id: The id of the playlist to retrieve."""

        return self._access(
            'viewer_get_playlist', request_arguments,
            id = id,
        )

    def get_ranking_items(self, tournament_id, stage_id, *, range: Range, group_ids: Optional[list] = None,
                          group_numbers: Optional[list] = None, **request_arguments):
        """Retrieve ranking items of a stage and tournament.
        Returns ranking items of a stage with a small summary of the associated participant in the ranking. The items are always ordered by ascending position.

        :param range: A range of requested items using the 'items' unit. The size of the range can not exceed 50. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))
        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param stage_id: The id of the stage you want to retrieve data about.
        :param group_ids: A list of group ids to filter.
        :param group_numbers: A list of group numbers to filter."""

        return self._access(
            'viewer_get_ranking_items', request_arguments,
            tournament_id = tournament_id,
            stage_id = stage_id,
            range = range,
            group_ids = group_ids,
            group_numbers = group_numbers,
        )

    def get_rounds(self, tournament_id, *, range: Range, stage_ids: Optional[list] = None,
                   stage_numbers: Optional[list] = None, group_ids: Optional[list] = None,
                   group_numbers: Optional[list] = None, **request_arguments):
        """Retrieve all rounds of a tournament.
        Returns all rounds of a tournament with basic information and settings.

        :param range: A range of requested items using the 'rounds' unit. The size of the range can not exceed 50. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))
        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param stage_ids: A list of stage ids to filter.
        :param stage_numbers: A list of stage numbers to filter.
        :param group_ids: A list of group ids to filter.
        :param group_numbers: A list of group numbers to filter."""

        return self._access(
            'viewer_get_rounds', request_arguments,
            tournament_id = tournament_id,
            range = range,
            stage_ids = stage_ids,
            stage_numbers = stage_numbers,
            group_ids = group_ids,
            group_numbers = group_numbers,
        )

    def get_round(self, tournament_id, id, **request_arguments):
        """Retrieve a single round of a tournament.
        Returns a round with the given id with basic information and settings.

        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param id: The id of the round to retrieve."""

        return self._access(
            'viewer_get_round', request_arguments,
            tournament_id = tournament_id,
            id = id,
        )

    def get_stages(self, tournament_id, **request_arguments):
        """Retrieve all stages of a tournament.
        Returns all stages of a tournament with basic information and settings.

        :param tournament_id: The id of the tournament you want to retrieve data about."""

        return self._access(
            'viewer_get_stages', request_arguments,
            tournament_id = tournament_id,
        )

    def get_stage(self, tournament_id, id, **request_arguments):
        """Retrieve a single stage of a tournament.
        Returns a stage with the given id with basic information and settings.

        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param id: The id of the stage to retrieve."""

        return self._access(
            'viewer_get_stage', request_arguments,
            tournament_id = tournament_id,
            id = id,
        )

    def get_standings(self, *, range: Range, tournament_ids: list, participant_ids: Optional[list] = None,
                      **request_arguments):
        """Retrieve a list of final standing items.
        Returns a list of final standing items.

        :param range: A range of requested items using the 'items' unit. The size of the range can not exceed 50. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))
        :param tournament_ids: Only return tournaments for the given list of ids.
        :param participant_ids: One or several participant ids involved in the standings to filter."""

        return self._access(
            'viewer_get_standings', request_arguments,
            range = range,
            tournament_ids = tournament_ids,
            participant_ids = participant_ids,
        )

    def get_streams(self, tournament_id, *, range: Range, match_ids: Optional[list] = None, **request_arguments):
        """Retrieves available streams.
        Returns the streams of the given tournament.

        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param range: A range of requested items using the 'streams' unit. The size of the range can not exceed 50. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))
        :param match_ids: A list of match ids to filter."""

        return self._access(
            'viewer_get_streams', request_arguments,
            tournament_id = tournament_id,
            range = range,
            match_ids = match_ids,
        )

    def get_videos(self, tournament_id, *, range: Range, participant_ids: Optional[list] = None,
                   category: Optional[str] = None, sort: Optional[str] = None, **request_arguments):
        """Retrieve videos of a tournament.
        Returns the videos of the given tournament.

        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param range: A range of requested items using the 'videos' unit. The size of the range can not exceed 50. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))
        :param participant_ids: One or several participant ids to filter.
        :param category: The category of the videos.
        :param sort: Sorts the collection in a particular order. "created_asc" sorts the videos from the oldest to the most recent one; "created_desc" sorts the videos from the most recent to the oldest one."""

        return self._access(
            'viewer_get_videos', request_arguments,
            tournament_id = tournament_id,
            range = range,
            participant_ids = participant_ids,
            category = category,
            sort = sort,
        )

    def get_videos_by_match(self, tournament_id, match_id, *, category: Optional[str] = None,
                            sort: Optional[str] = None, **request_arguments):
        """Retrieve videos of a match.
        Returns the videos of the given match.

        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param match_id: The id of the match to retrieve.
        :param category: The category of the videos.
        :param sort: Sorts the collection in a particular order. "created_asc" sorts the videos from the oldest to the most recent one; "created_desc" sorts the videos from the most recent to the oldest one."""

        return self._access(
            'viewer_get_videos_by_match', request_arguments,
            tournament_id = tournament_id,
            match_id = match_id,
            category = category,
            sort = sort,
        )

    def get_tournaments_featured(self, *, range: Range, name: Optional[str] = None, disciplines: Optional[str] = None,
                                 statuses: Optional[str] = None, scheduled_before: Optional[str] = None,
                                 scheduled_after: Optional[str] = None, countries: Optional[str] = None,
                                 platforms: Optional[str] = None, is_online: Optional[int] = None,
                                 sort: Optional[str] = None, **request_arguments):
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

        return self._access(
            'viewer_get_tournaments_featured', request_arguments,
            range = range,
            name = name,
            disciplines = disciplines,
            statuses = statuses,
            scheduled_before = scheduled_before,
            scheduled_after = scheduled_after,
            countries = countries,
            platforms = platforms,
            is_online = is_online,
            sort = sort,
        )

    def get_tournament(self, id, **request_arguments):
        """Retrieve a single tournament.
        Returns a tournament identified with the given id.

        :param id: The id of the tournament to retrieve."""

        return self._access(
            'viewer_get_tournament', request_arguments,
            id = id,
        )

    def get_tournaments_by_playlist(self, id, *, range: Range, name: Optional[str] = None,
                                    disciplines: Optional[str] = None, statuses: Optional[str] = None,
                                    scheduled_before: Optional[str] = None, scheduled_after: Optional[str] = None,
                                    countries: Optional[str] = None, platforms: Optional[str] = None,
                                    is_online: Optional[int] = None, sort: Optional[str] = None, **request_arguments):
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

        return self._access(
            'viewer_get_tournaments_by_playlist', request_arguments,
            id = id,
            range = range,
            name = name,
            disciplines = disciplines,
            statuses = statuses,
            scheduled_before = scheduled_before,
            scheduled_after = scheduled_after,
            countries = countries,
            platforms = platforms,
            is_online = is_online,
            sort = sort,
        )


class AsyncViewerAPI(AsyncToornamentConnection):

    @staticmethod
    def _base_url():
        return 'https://api.toornament.com/viewer/v2'

    async def get_match(self, tournament_id, id, **request_arguments):
        """Retrieve a single match of a tournament.
        Returns a match with all its games and opponents. In ffa matches only the first four opponents are included in each match game.

        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param id: The id of the match to retrieve."""

        return await self._access(
            'viewer_get_match', request_arguments,
            tournament_id = tournament_id,
            id = id,
        )

    async def get_matches_from_tournament(self, tournament_id, *, range: Range, stage_ids: Optional[list] = None,
                                    stage_numbers: Optional[list] = None, group_ids: Optional[list] = None,
                                    group_numbers: Optional[list] = None, round_ids: Optional[list] = None,
                                    round_numbers: Optional[list] = None, statuses: Optional[list] = None,
                                    is_scheduled: Optional[bool] = None, scheduled_before: Optional[str] = None,
                                    scheduled_after: Optional[str] = None, participant_ids: Optional[list] = None,
                                    sort: Optional[str] = None, **request_arguments):
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

        return await self._access(
            'viewer_get_matches_from_tournament', request_arguments,
            tournament_id = tournament_id,
            range = range,
            stage_ids = stage_ids,
            stage_numbers = stage_numbers,
            group_ids = group_ids,
            group_numbers = group_numbers,
            round_ids = round_ids,
            round_numbers = round_numbers,
            statuses = statuses,
            is_scheduled = is_scheduled,
            scheduled_before = scheduled_before,
            scheduled_after = scheduled_after,
            participant_ids = participant_ids,
            sort = sort,
        )

    async def get_matches_from_discipline(self, discipline_id, *, range: Range, is_featured: Optional[bool] = None,
                                    statuses: Optional[list] = None, scheduled_before: Optional[str] = None,
                                    scheduled_after: Optional[str] = None, participant_ids: Optional[list] = None,
                                    tournament_ids: Optional[list] = None, sort: Optional[str] = None,
                                    **request_arguments):
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

        return await self._access(
            'viewer_get_matches_from_discipline', request_arguments,
            discipline_id = discipline_id,
            range = range,
            is_featured = is_featured,
            statuses = statuses,
            scheduled_before = scheduled_before,
            scheduled_after = scheduled_after,
            participant_ids = participant_ids,
            tournament_ids = tournament_ids,
            sort = sort,
        )

    async def get_bracket_nodes(self, tournament_id, stage_id, *, range: Range, group_ids: Optional[list] = None,
                          group_numbers: Optional[list] = None, round_ids: Optional[list] = None,
                          round_numbers: Optional[list] = None, min_depth: Optional[int] = None,
                          max_depth: Optional[int] = None, **request_arguments):
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

        return await self._access(
            'viewer_get_bracket_nodes', request_arguments,
            tournament_id = tournament_id,
            stage_id = stage_id,
            range = range,
            group_ids = group_ids,
            group_numbers = group_numbers,
            round_ids = round_ids,
            round_numbers = round_numbers,
            min_depth = min_depth,
            max_depth = max_depth,
        )

    async def get_custom_fields(self, tournament_id, *, target_type: Optional[str] = None, **request_arguments):
        """Retrieves custom fields of a tournament.
        Returns the complete definition of all custom fields for a given tournament. This includes both public and private custom fields.
        A custom field may be associated to a player, a team or a team's player. For more information, please read the [Custom Fields](https://developer.toornament.com/v2/core-concepts/custom-fields) documentation.

        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param target_type: The entity affected by the custom fields."""

        return await self._access(
            'viewer_get_custom_fields', request_arguments,
            tournament_id = tournament_id,
            target_type = target_type,
        )

    async def get_disciplines(self, *, range: Range, **request_arguments):
        """Retrieve the list of available disciplines and their basic information.
        Returns a collection of disciplines.

        :param range
        A range of requested items using the 'disciplines' unit.
        The size of the range can not exceed 50. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))"""

        return await self._access(
            'viewer_get_disciplines', request_arguments,
            range = range,
        )

    async def get_discipline(self, id, **request_arguments):
        """Retrieve a specific discipline, with advanced information.
        Returns a discipline with its information and configuration options.

        :param id: The string id of the discipline."""

        return await self._access(
            'viewer_get_discipline', request_arguments,
            id = id,
        )

    async def get_groups(self, tournament_id, *, range: Range, stage_ids: Optional[list] = None,
                   stage_numbers: Optional[list] = None, **request_arguments):
        """Retrieve all groups of a tournament.
        Returns all groups of a tournament with basic information and settings.

        :param range: A range of requested items using the 'groups' unit. The size of the range can not exceed 50. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))
        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param stage_ids: A list of stage ids to filter.
        :param stage_numbers: A list of stage numbers to filter."""

        return await self._access(
            'viewer_get_groups', request_arguments,
            tournament_id = tournament_id,
            range = range,
            stage_ids = stage_ids,
            stage_numbers = stage_numbers,
        )

    async def get_group(self, tournament_id, id, **request_arguments):
        """Retrieve a single group of a tournament.
        Returns a group with the given id with basic information and settings.

        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param id: The id of the group to retrieve."""

        return await self._access(
            'viewer_get_group', request_arguments,
            tournament_id = tournament_id,
            id = id,
        )

    async def get_game(self, tournament_id, match_id, number, **request_arguments):
        """Retrieve a single game of a match.
        Returns detailed information about one match game.

        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param match_id: The id of the match to retrieve.
        :param number: The relative identifier of the match game to retrieve."""

        return await self._access(
            'viewer_get_game', request_arguments,
            tournament_id = tournament_id,
            match_id = match_id,
            number = number,
        )

    async def get_participants(self, tournament_id, *, range: Range, name: Optional[str] = None, sort: Optional[str] = None,
                         **request_arguments):
        """Retrieve the participants of a tournament.
        Returns the participants of the given tournament. The data provided in the participant depends on whether the participant type is team or player. This setting can be found in the tournament.

        :param range: A range of requested items using the 'participants' unit. The size of the range can not exceed 50. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))
        :param tournament_id: The id of the tournament the participants are from.
        :param name: The string to be looked for in the name of the participant.
        :param sort: A method to sort the filtered data. “created_asc” and “created_desc” sort the participants from their creation date (earliest to latest, and inversely). “Alphabetic” sorts the participants using their case-insensitive names."""

        return await self._access(
            'viewer_get_participants', request_arguments,
            tournament_id = tournament_id,
            range = range,
            name = name,
            sort = sort,
        )

    async def get_participant(self, tournament_id, id, **request_arguments):
        """Retrieve a single participant of a tournament.
        Returns a participant identified with the given id. The data provided in the participant depends on whether the participant type is team or player. This setting can be found in the tournament.

        :param tournament_id: The id of the tournament the participants are from.
        :param id: The id of the participant to retrieve."""

        return await self._access(
            'viewer_get_participant', request_arguments,
            tournament_id = tournament_id,
            id = id,
        )

    async def get_playlist(self, id, **request_arguments):
        """Retrieve a single playlist.
        Returns a playlist identified with the given id.

        :param id: The id of the playlist to retrieve."""

        return await self._access(
            'viewer_get_playlist', request_arguments,
            id = id,
        )

    async def get_ranking_items(self, tournament_id, stage_id, *, range: Range, group_ids: Optional[list] = None,
                          group_numbers: Optional[list] = None, **request_arguments):
        """Retrieve ranking items of a stage and tournament.
        Returns ranking items of a stage with a small summary of the associated participant in the ranking. The items are always ordered by ascending position.

        :param range: A range of requested items using the 'items' unit. The size of the range can not exceed 50. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))
        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param stage_id: The id of the stage you want to retrieve data about.
        :param group_ids: A list of group ids to filter.
        :param group_numbers: A list of group numbers to filter."""

        return await self._access(
            'viewer_get_ranking_items', request_arguments,
            tournament_id = tournament_id,
            stage_id = stage_id,
            range = range,
            group_ids = group_ids,
            group_numbers = group_numbers,
        )

    async def get_rounds(self, tournament_id, *, range: Range, stage_ids: Optional[list] = None,
                   stage_numbers: Optional[list] = None, group_ids: Optional[list] = None,
                   group_numbers: Optional[list] = None, **request_arguments):
        """Retrieve all rounds of a tournament.
        Returns all rounds of a tournament with basic information and settings.

        :param range: A range of requested items using the 'rounds' unit. The size of the range can not exceed 50. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))
        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param stage_ids: A list of stage ids to filter.
        :param stage_numbers: A list of stage numbers to filter.
        :param group_ids: A list of group ids to filter.
        :param group_numbers: A list of group numbers to filter."""

        return await self._access(
            'viewer_get_rounds', request_arguments,
            tournament_id = tournament_id,
            range = range,
            stage_ids = stage_ids,
            stage_numbers = stage_numbers,
            group_ids = group_ids,
            group_numbers = group_numbers,
        )

    async def get_round(self, tournament_id, id, **request_arguments):
        """Retrieve a single round of a tournament.
        Returns a round with the given id with basic information and settings.

        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param id: The id of the round to retrieve."""

        return await self._access(
            'viewer_get_round', request_arguments,
            tournament_id = tournament_id,
            id = id,
        )

    async def get_stages(self, tournament_id, **request_arguments):
        """Retrieve all stages of a tournament.
        Returns all stages of a tournament with basic information and settings.

        :param tournament_id: The id of the tournament you want to retrieve data about."""

        return await self._access(
            'viewer_get_stages', request_arguments,
            tournament_id = tournament_id,
        )

    async def get_stage(self, tournament_id, id, **request_arguments):
        """Retrieve a single stage of a tournament.
        Returns a stage with the given id with basic information and settings.

        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param id: The id of the stage to retrieve."""

        return await self._access(
            'viewer_get_stage', request_arguments,
            tournament_id = tournament_id,
            id = id,
        )

    async def get_standings(self, *, range: Range, tournament_ids: list, participant_ids: Optional[list] = None,
                      **request_arguments):
        """Retrieve a list of final standing items.
        Returns a list of final standing items.

        :param range: A range of requested items using the 'items' unit. The size of the range can not exceed 50. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))
        :param tournament_ids: Only return tournaments for the given list of ids.
        :param participant_ids: One or several participant ids involved in the standings to filter."""

        return await self._access(
            'viewer_get_standings', request_arguments,
            range = range,
            tournament_ids = tournament_ids,
            participant_ids = participant_ids,
        )

    async def get_streams(self, tournament_id, *, range: Range, match_ids: Optional[list] = None, **request_arguments):
        """Retrieves available streams.
        Returns the streams of the given tournament.

        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param range: A range of requested items using the 'streams' unit. The size of the range can not exceed 50. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))
        :param match_ids: A list of match ids to filter."""

        return await self._access(
            'viewer_get_streams', request_arguments,
            tournament_id = tournament_id,
            range = range,
            match_ids = match_ids,
        )

    async def get_videos(self, tournament_id, *, range: Range, participant_ids: Optional[list] = None,
                   category: Optional[str] = None, sort: Optional[str] = None, **request_arguments):
        """Retrieve videos of a tournament.
        Returns the videos of the given tournament.

        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param range: A range of requested items using the 'videos' unit. The size of the range can not exceed 50. (see [Pagination](https://developer.toornament.com/v2/overview/pagination))
        :param participant_ids: One or several participant ids to filter.
        :param category: The category of the videos.
        :param sort: Sorts the collection in a particular order. "created_asc" sorts the videos from the oldest to the most recent one; "created_desc" sorts the videos from the most recent to the oldest one."""

        return await self._access(
            'viewer_get_videos', request_arguments,
            tournament_id = tournament_id,
            range = range,
            participant_ids = participant_ids,
            category = category,
            sort = sort,
        )

    async def get_videos_by_match(self, tournament_id, match_id, *, category: Optional[str] = None,
                            sort: Optional[str] = None, **request_arguments):
        """Retrieve videos of a match.
        Returns the videos of the given match.

        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param match_id: The id of the match to retrieve.
        :param category: The category of the videos.
        :param sort: Sorts the collection in a particular order. "created_asc" sorts the videos from the oldest to the most recent one; "created_desc" sorts the videos from the most recent to the oldest one."""

        return await self._access(
            'viewer_get_videos_by_match', request_arguments,
            tournament_id = tournament_id,
            match_id = match_id,
            category = category,
            sort = sort,
        )

    async def get_tournaments_featured(self, *, range: Range, name: Optional[str] = None, disciplines: Optional[str] = None,
                                 statuses: Optional[str] = None, scheduled_before: Optional[str] = None,
                                 scheduled_after: Optional[str] = None, countries: Optional[str] = None,
                                 platforms: Optional[str] = None, is_online: Optional[int] = None,
                                 sort: Optional[str] = None, **request_arguments):
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

        return await self._access(
            'viewer_get_tournaments_featured', request_arguments,
            range = range,
            name = name,
            disciplines = disciplines,
            statuses = statuses,
            scheduled_before = scheduled_before,
            scheduled_after = scheduled_after,
            countries = countries,
            platforms = platforms,
            is_online = is_online,
            sort = sort,
        )

    async def get_tournament(self, id, **request_arguments):
        """Retrieve a single tournament.
        Returns a tournament identified with the given id.

        :param id: The id of the tournament to retrieve."""

        return await self._access(
            'viewer_get_tournament', request_arguments,
            id = id,
        )

    async def get_tournaments_by_playlist(self, id, *, range: Range, name: Optional[str] = None,
                                    disciplines: Optional[str] = None, statuses: Optional[str] = None,
                                    scheduled_before: Optional[str] = None, scheduled_after: Optional[str] = None,
                                    countries: Optional[str] = None, platforms: Optional[str] = None,
                                    is_online: Optional[int] = None, sort: Optional[str] = None, **request_arguments):
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

        return await self._access(
            'viewer_get_tournaments_by_playlist', request_arguments,
            id = id,
            range = range,
            name = name,
            disciplines = disciplines,
            statuses = statuses,
            scheduled_before = scheduled_before,
            scheduled_after = scheduled_after,
            countries = countries,
            platforms = platforms,
            is_online = is_online,
            sort = sort,
        )
