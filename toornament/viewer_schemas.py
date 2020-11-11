from .converter import Converter


class Match:

    def __init__(self, *, id, stage_id, group_id, round_id, number, type, status, scheduled_datetime, played_at,
                 opponents):
        self.id = int(id)  # The id of the match.
        self.stage_id = int(stage_id)  # The id of the stage that contains this match.
        self.group_id = int(group_id)  # The id of the group that contains this match.
        self.round_id = int(round_id)  # The id of the round that contains this match.
        self.number = number  # The match number (a relative identifier within a round).
        self.type = type  # The match type.
        self.status = status  # The status of the match.
        self.scheduled_datetime = Converter.datetime(
            scheduled_datetime)  # The scheduled date of the match in RFC 3339 (combined date, time and utc offset).
        self.played_at = Converter.datetime(
            played_at)  # The timestamp on which the match was played (a result was provided) in RFC 3339 (combined date, time and utc offset).
        self.opponents = opponents  # Array  # List of match opponents.


class MatchDetailed(Match):

    def __init__(self, *, public_notes=None, opponents, games, **kwargs):
        super().__init__(**kwargs)
        self.public_notes = public_notes  # Public note of a match, written by the organizer.
        self.opponents = opponents  # Array  # List of match opponents.
        self.games = games  # Array  # List of the match games.


class Tournament:

    def __init__(self, id, name, full_name=None):
        self.id = int(id)  # The unique identifier of the tournament.
        self.name = name  # The name of the tournament.
        self.full_name = full_name  # The complete name of the tournament.


class MatchDiscipline(Match):

    def __init__(self, tournament, **kwargs):
        super().__init__(**kwargs)
        self.tournament = Tournament(**tournament)
