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

    def __init__(self, *, number, position=None, result=None, rank=None, forfeit, score=None, properties=None):
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
        self.properties = properties


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

    def __init__(self, *, number, type=None, status, opponents, properties):
        """
        :param number integer A relative identifier between 1 and the total number of games, to identify the game within the match.
        :param status string The status of the match game.
        :param opponents array List of match game opponents.
        :param properties object Discipline features that define the specificities of the match game (map, gamemode...).
        """

        self.number = number
        self.type = type
        self.status = status
        self.opponents = [MatchGameOpponent(**opponent) for opponent in opponents]
        self.properties = properties


class Match:

    def __init__(self, *, id, stage_id, group_id, round_id, number, type, status, scheduled_datetime=None,
                 played_at=None, opponents):
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


class TournamentLight:

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
        self.tournament = TournamentLight(**tournament)


class BracketNodeOpponent:

    def __init__(self, *, number, result=None, rank=None, forfeit, score=None, source_type, source_node_id=None,
                 participant):
        """
        :param number integer A relative identifier between 1 and the total number of participants, it is unique and determined by the seeding.
        :param result string The game result of the opponent.
        :param rank integer The rank of the participant in the ranking. Multiple participants can share the same rank if they are tied after applying all configured tiebreakers.
        :param forfeit boolean Whether the opponent is forfeit.
        :param score integer The score of the opponent.
        :param source_type string The type of source of this node item.
        :param source_node_id string The id of the bracket node connected to this opponent.
        :param participant The participant identified with this opponent.
        """

        self.number = number
        self.result = result
        self.rank = rank
        self.forfeit = forfeit
        self.score = score
        self.source_type = source_type
        self.source_node_id = int(source_node_id) if source_node_id else None
        self.participant = Participant(**participant) if participant else None


class BracketNode:

    def __init__(self, *, id, stage_id, group_id, round_id, number, type, status, scheduled_datetime=None,
                 played_at=None, depth, branch=None, opponents):
        """
        :param id string The id of the bracket node and the match (they both share the same id).
        :param stage_id string The id of the stage that contains this bracket node.
        :param group_id string The id of the group that contains this bracket node.
        :param round_id string The id of the round that contains this bracket node.
        :param number integer The match number (a relative identifier within a round).
        :param type string The match type.
        :param status string The status of the match.
        :param scheduled_datetime string The scheduled date of the match in RFC 3339 (combined date, time and utc offset).
        :param played_at string The timestamp on which the match was played (a result was provided) in RFC 3339 (combined date, time and utc offset).
        :param depth integer The depth of the node in the bracket.
        :param branch string The core branch of the node in the bracket.
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
        self.depth = depth
        self.branch = branch
        self.opponents = [BracketNodeOpponent(**opponent) for opponent in opponents]


class CustomField:

    def __init__(self, *, machine_name, label, target_type, type, default_value=None, required, public, position):
        """
        :param machine_name string A name used to identify a custom field for computing purposes.
        :param label string The display name of a custom field in forms.
        :param target_type string The entity concerned by the custom field.
        :param type string A data type used for both input and computing.
        :param default_value any A default value (can be array, scalar or null).
        :param required boolean Whether the custom field is required.
        :param public boolean Whether the value of the custom field is public.
        :param position integer The position of the field in forms.
        """

        self.machine_name = machine_name
        self.label = label
        self.target_type = target_type
        self.type = type
        self.default_value = default_value
        self.required = required
        self.public = public
        self.position = position


class Discipline:

    def __init__(self, *, id, name, shortname, fullname, copyrights):
        """
        :param id string An identifier for a discipline, can be used in others APIs.
        :param name string The official name of the discipline.
        :param shortname string The short name of the discipline.
        :param fullname string The complete name of the discipline.
        :param copyrights string Name of the entity or entities that are the creators and/or right holders of the discipline.
        """

        self.id = str(id)
        self.name = name
        self.shortname = shortname
        self.fullname = fullname
        self.copyrights = copyrights


class DisciplineFeature:

    def __init__(self, *, name, type, options):
        """
        :param name string Name of the feature.
        :param type string Type of the feature.
        :param options object Options of the feature.
        """

        self.name = name
        self.type = type
        self.options = options


class TeamSize:

    def __init__(self, *, min, max):
        """Sets the minimum and maximum of players in a team
        :param min integer Minimal size of a team in the tournament.
        :param max integer Maximal size of a team in the tournament.
        """

        self.min = min
        self.max = max


class DisciplineDetailed(Discipline):

    def __init__(self, *, platforms_available, team_size, features, **kwargs):
        """
        :param platforms_available array A list of platforms available of this discipline.
        :param team_size object Sets the minimum and maximum of players in a team.
        :param features array List of features for the discipline.
        """

        super().__init__(**kwargs)

        self.platforms_available = platforms_available
        self.team_size = TeamSize(**team_size)
        self.features = [DisciplineFeature(**feature) for feature in features]


class Group:

    def __init__(self, *, id, stage_id, number, name, closed, settings):
        """
        :param id string The id of the group.
        :param stage_id string The id of the stage that contains the group.
        :param number integer A number used for ordering groups.
        :param name string The name of the group.
        :param closed boolean Whether the group is closed.
        :param settings object Settings that describe the various options related to the group and stage types.
        """

        self.id = int(id)
        self.stage_id = int(stage_id)
        self.number = number
        self.name = name
        self.closed = closed
        self.settings = settings


class ParticipantPlayer:

    def __init__(self, *, id, name, custom_fields):
        """
        :param id string The id of the participant.
        :param name string The name of the participant.
        :param custom_fields object The values of the public custom fields configured in the tournament using the machine names as keys. For more information, please read the [Custom Fields](https://developer.toornament.com/v2/core-concepts/custom-fields) documentation.
        """

        self.id = int(id)
        self.name = name
        self.custom_fields = custom_fields


class TeamPlayerParticipant:

    def __init__(self, *, name, custom_fields):
        """
        :param name string The name of the team player.
        :param custom_fields object The values of the public custom fields configured in the tournament using the machine names as keys. For more information, please read the [Custom Fields](https://developer.toornament.com/v2/core-concepts/custom-fields) documentation.
        """

        self.name = name
        self.custom_fields = custom_fields


class ParticipantTeam(ParticipantPlayer):

    def __init__(self, *, lineup, **kwargs):
        """
        :param lineup array A list of players in a team (Only if the tournament participant type is “team”).
        """

        super().__init__(**kwargs)

        self.lineup = [TeamPlayerParticipant(**player) for player in lineup]


class Playlist:

    def __init__(self, *, id, name, description=None):
        """
        :param id string A unique identifier for the playlist.
        :param name string The name of the playlist.
        :param description string A description of the playlist.
        """

        self.id = int(id)
        self.name = name
        self.description = description


class RankingItemProperties:

    def __init__(self, *, wins, draws, losses, played, forfeits, **undocumented_properties):
        """
        :param wins integer
        :param draws integer
        :param losses integer
        :param played integer
        :param forfeits integer
        :param undocumented_properties: dict Properties that where not documented during the development of the module.
        """

        self.wins = wins
        self.draws = draws
        self.losses = losses
        self.played = played
        self.forfeits = forfeits
        self.undocumented_properties = undocumented_properties


class RankingItemPropertiesWithScore(RankingItemProperties):

    def __init__(self, *, score_for, score_against, score_difference, **kwargs):
        """
        :param score_for integer
        :param score_against integer
        :param score_difference integer
        """

        super().__init__(**kwargs)

        self.score_for = score_for
        self.score_against = score_against
        self.score_difference = score_difference


class RankingItemPropertiesSwiss(RankingItemProperties):

    def __init__(self, *, match_history, **kwargs):
        """
        :param match_history string
        """

        super().__init__(**kwargs)

        self.match_history = match_history


class RankingItem:

    def __init__(self, *, id, group_id, number, position, rank=None, participant=None, points, properties):
        """
        :param id string The id of the ranking item.
        :param group_id string The id of the group associated to this ranking.
        :param number integer A number used as relative identifier within the ranking. It is determined from the seed attributed to the participant during the placement.
        :param position integer A position used for presentation purposes. It is always unique within the same ranking.
        :param rank integer The ranking of the participant in the ranking. Multiple participants can share the same rank if they are tied after involving all configured tiebreakers.
        :param participant
        :param points integer A number of points acquired by the participant in the ranking.
        :param properties object A list of ranking metrics (see ranking properties).
        """

        self.id = int(id)
        self.group_id = int(group_id)
        self.number = number
        self.position = position
        self.rank = rank
        self.participant = Participant(**participant) if participant else None
        self.points = points

        if properties.get('score_for') and properties.get('score_against') and properties.get('score_difference'):
            self.properties = RankingItemPropertiesWithScore(**properties)
        elif properties.get('match_history'):
            self.properties = RankingItemPropertiesSwiss(**properties)
        else:
            self.properties = RankingItemProperties(**properties)


class Round:

    def __init__(self, *, id, stage_id, group_id, number, name, closed, settings):
        """
        :param id string The id of the round.
        :param stage_id string The id of the stage that contains the round.
        :param group_id string The id of the group that contains the round.
        :param number integer A number used for ordering rounds.
        :param name string The name of the round.
        :param closed boolean Whether the round is closed.
        :param settings object Settings that describe the various options related to the round and stage types.
        """

        self.id = int(id)
        self.stage_id = int(stage_id)
        self.group_id = int(group_id)
        self.number = number
        self.name = name
        self.closed = closed
        self.settings = settings


class Stage:

    def __init__(self, *, id, number, name, type, closed, settings):
        """
        :param id string The id of the stage.
        :param number integer A number used for ordering stages.
        :param name string The name of the stage.
        :param type string The type of stage that defines how the stage functions.
        :param closed boolean Whether the stage is closed.
        :param settings object Settings that describe the various options for the stage type.
        """

        self.id = int(id)
        self.number = number
        self.name = name
        self.type = type
        self.closed = closed
        self.settings = settings


class StandingItem:

    def __init__(self, *, id, position, rank=None, participant=None, tournament_id):
        """
        :param id string A unique identifier for the standing item.
        :param position integer A position used for presentation purposes. It is always unique within the same standing.
        :param rank integer The ranking of the participant in the standing. Multiple participants can share the same rank if they are tied after involving all configured tiebreakers.
        :param participant
        :param tournament_id string The id of the tournament.
        """

        self.id = int(id)
        self.position = position
        self.rank = rank
        self.participant = Participant(**participant) if participant else None
        self.tournament_id = int(tournament_id)


class Stream:

    def __init__(self, *, id, name, url, language):
        """
        :param id string An identifier for a stream.
        :param name string The title of the stream.
        :param url string The URL of the stream.
        :param language string The language code of the stream content in ISO 639-1 code
        """

        self.id = int(id)
        self.name = name
        self.url = url
        self.language = language


class Video:

    def __init__(self, *, id, name, url, language, category):
        """
        :param id string An identifier for a video.
        :param name string The title of the video.
        :param url string The URL of the video.
        :param language string Language code of the video content in ISO 639-1 code
        :param category string The category of the video.
        """

        self.id = int(id)
        self.name = name
        self.url = url
        self.language = language
        self.category = category


class VideoTournament(Video):

    def __init__(self, *, match_id=None, **kwargs):
        """
        :param match_id string The match's identifier of this video.
        """

        super().__init__(**kwargs)

        self.match_id = int(match_id) if match_id else None


class TournamentLogo:

    def __init__(self, *, logo_small, logo_medium, logo_large, original):
        """
        :param logo_small string URL of the small version of  the tournament logo.
        :param logo_medium string URL of the medium version of  the tournament logo.
        :param logo_large string URL of the large version of  the tournament logo.
        :param original string URL of the original version of  the tournament logo.
        """

        self.logo_small = logo_small
        self.logo_medium = logo_medium
        self.logo_large = logo_large
        self.original = original


class Tournament:

    def __init__(self, *, id, discipline, name, full_name=None, status, scheduled_date_start=None,
                 scheduled_date_end=None, timezone, public, size, online=None, location=None, country=None, platforms,
                 logo, registration_enabled, registration_opening_datetime=None, registration_closing_datetime=None):
        """
        :param id string The unique identifier of the tournament.
        :param discipline string A unique identifier of the tournament’s discipline.
        :param name string The name of the tournament.
        :param full_name string The complete name of the tournament.
        :param status string The status of the tournament
        :param scheduled_date_start string A starting date in ISO 8601 format (only the date part, with YYYY-MM-DD pattern).
        :param scheduled_date_end string An ending date in ISO 8601 format (only the date part, with YYYY-MM-DD pattern).
        :param timezone string A time zone from the IANA tz database.
        :param public boolean Whether the tournament is published.
        :param size integer The expected number of participants in the tournament.
        :param online boolean Whether the tournament is played on internet.
        :param location string The region, city, address or place of interest where the tournament is held.
        :param country string The country where the tournament is played. Some codes may not be supported. (format is ISO 3166-1 alpha-2)
        :param platforms array A list of platforms on which the tournament can be played.
        :param logo
        :param registration_enabled boolean Whether the registration process is enabled.
        :param registration_opening_datetime string The opening date of the registrations in RFC 3339 format (combined date, time and utc offset)
        :param registration_closing_datetime string The closing date of the registrations in RFC 3339 format (combined date, time and utc offset)
        """

        self.id = int(id)
        self.discipline = discipline
        self.name = name
        self.full_name = full_name
        self.status = status
        self.scheduled_date_start = Converter.date(scheduled_date_start)
        self.scheduled_date_end = Converter.date(scheduled_date_end)
        self.timezone = timezone
        self.public = public
        self.size = size
        self.online = online
        self.location = location
        self.country = country
        self.platforms = platforms
        self.logo = TournamentLogo(**logo) if logo else None
        self.registration_enabled = registration_enabled
        self.registration_opening_datetime = Converter.datetime(registration_opening_datetime)
        self.registration_closing_datetime = Converter.datetime(registration_closing_datetime)


class TournamentDetailed(Tournament):

    def __init__(self, *, participant_type, organization=None, contact=None, discord=None, website=None,
                 description=None, rules=None, prize=None, settings, **kwargs):
        """
        :param participant_type string The type of participants that play in the tournament.
        :param organization string The name of the organizer, be it an individual, group, association or company.
        :param contact string The email address to contact the organizer.
        :param discord string Invite URL to the tournament Discord server.
        :param website string The tournament's official website URL.
        :param description string A description of the tournament.
        :param rules string The rules of the tournament.
        :param prize string The prizes of the tournament.
        :param settings object List of tournament settings, it usually contains discipline information for the entire tournament (maps, champions...).
        """

        super().__init__(**kwargs)

        self.participant_type = participant_type
        self.organization = organization
        self.contact = contact
        self.discord = discord
        self.website = website
        self.description = description
        self.rules = rules
        self.prize = prize
        self.settings = settings
