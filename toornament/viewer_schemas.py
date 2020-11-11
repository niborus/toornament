from .converter import Converter


class Participant:

    def __init__(self, *, id, name, custom_fields):
        """
        :param id string The id of the participant.
        :param name string The name of the participant.
        :param custom_fields object The values of the public custom fields configured in the tournament using the machine names as keys. For more information, please read the [Custom Fields](https://developer.toornament.com/v2/core-concepts/custom-fields) documentation.
        """

        self.id = int(id)
        self.name = name
        self.custom_fields = custom_fields


class Opponent:

    def __init__(self, *, number, position=None, result=None, rank=None, forfeit, score=None):
        """
        :param number integer A relative identifier between 1 and the total number of participants, it is unique and determined by the seeding.
        :param position integer The position of the participant in the ranking. It is unique and tied participants have their position determined by their number.
        :param result string The match result of the opponent.
        :param rank integer The rank of the participant in the ranking. Multiple participants can share the same rank if they are tied after applying all configured tiebreakers.
        :param forfeit boolean Whether the opponent is forfeit.
        :param score integer The score of the opponent.
        """

        self.number = number
        self.position = position
        self.result = result
        self.rank = rank
        self.forfeit = forfeit
        self.score = score


class MatchOpponent(Opponent):

    def __init__(self, *, participant=None, **kwargs):
        """
        :param participant The participant identified with this opponent.
        """

        super().__init__(**kwargs)

        self.participant = Participant(**participant) if participant else None


class MatchGameOpponent(Opponent):

    def __init__(self, *, properties, **kwargs):
        """
        :param properties object Opponent properties depending on the discipline features (champion, spells...).
        """

        super().__init__(**kwargs)

        self.properties = properties


class Game:

    def __init__(self, *, number, status, opponents, properties):
        """
        :param number integer A relative identifier between 1 and the total number of games, to identify the game within the match.
        :param status string The status of the match game.
        :param opponents array List of match game opponents.
        :param properties object Discipline features that define the specificities of the match game (map, gamemode...).
        """

        self.number = number
        self.status = status
        self.opponents = [MatchGameOpponent(**opponent) for opponent in opponents]
        self.properties = properties


class Match:

    def __init__(self, *, id, stage_id, group_id, round_id, number, type, status, scheduled_datetime=None, played_at=None, opponents):
        """
        :param id string The id of the match.
        :param stage_id string The id of the stage that contains this match.
        :param group_id string The id of the group that contains this match.
        :param round_id string The id of the round that contains this match.
        :param number integer The match number (a relative identifier within a round).
        :param type string The match type.
        :param status string The status of the match.
        :param scheduled_datetime string The scheduled date of the match in RFC 3339 (combined date, time and utc offset).
        :param played_at string The timestamp on which the match was played (a result was provided) in RFC 3339 (combined date, time and utc offset).
        :param opponents array List of match opponents.
        """

        self.id = int(id)
        self.stage_id = int(stage_id)
        self.group_id = int(group_id)
        self.round_id = int(round_id)
        self.number = number
        self.type = type
        self.status = status
        self.scheduled_datetime = Converter.datetime(scheduled_datetime)
        self.played_at = Converter.datetime(played_at)
        self.opponents = [MatchOpponent(**opponent) for opponent in opponents]


class MatchDetailed(Match):

    def __init__(self, *, public_notes=None, games, **kwargs):
        """
        :param public_notes string Public note of a match, written by the organizer.
        :param games array List of the match games.
        """

        super().__init__(**kwargs)

        self.public_notes = public_notes
        self.games = [Game(**game) for game in games]


class Tournament:

    def __init__(self, *, id, name, full_name=None):
        """
        :param id string The unique identifier of the tournament.
        :param name string The name of the tournament.
        :param full_name string The complete name of the tournament.
        """

        self.id = int(id)
        self.name = name
        self.full_name = full_name


class MatchDiscipline(Match):

    def __init__(self, *, tournament, **kwargs):
        """
        :param tournament
        """

        super().__init__(**kwargs)
        self.tournament = Tournament(**tournament)
