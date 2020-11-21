from .viewer_schemas import ViewerSchema


class Converter:

    @staticmethod
    def none(attribute):
        return attribute

    @staticmethod
    def to_str(attribute):
        return str(attribute)

    @staticmethod
    def range(attribute):
        """:returns A String that Looks like that: 2-45"""
        return '{0.start}-{0.end}'.format(attribute)

    @staticmethod
    def to_date(attribute):
        return attribute

    @staticmethod
    def to_datetime(attribute):
        return attribute


class ResultConverter:

    @staticmethod
    def participant(**participant):
        return ViewerSchema.ParticipantPlayer(**participant) if participant.get(
            'lineup') is None else ViewerSchema.ParticipantTeam(**participant)


class ParameterType:
    HEADER = 0
    PATH = 1
    QUERY = 2
