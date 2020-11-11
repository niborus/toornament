from .exceptions import BadRange


def check_for_range(a, b):
    if a > b:
        raise BadRange("Range start value has to be lower or equal to end value. Received: start:{} end:{}".format(a, b))


class Range:

    def __init__(self, start=None, end=None, *, unit=None):
        """This sets the Range for the Request.
        :param start The Start of the Range
        :param end The End of the Range
        :param unit The unit of the Range. If not given, this is set by tournament.py. We recommend to not set this by yourself."""
        self.start = None
        self.end = None
        self.unit = None

        if start is not None:
            self.set_start(start)
        if end is not None:
            self.set_end(end)
        if unit is not None:
            self.set_unit(unit)

    def set_start(self, start):
        if start < 0:
            raise ValueError('Range can not start on negative Value. Received: {}'.format(start))
        self.start = int(start)

    def set_end(self, end):
        if end < 0:
            raise ValueError('Range can not end on negative Value. Received: {}'.format(end))
        self.end = int(end)

    def set_unit(self, unit: str):
        self.unit = unit.strip().lower()

    def set_range(self, range: list):
        if len(range) != 2:
            raise ValueError("Range needs exactly two entries. Received: {}".format(len(range)))
        check_for_range(*range)
        self.set_start(range[0])
        self.set_end(range[1])

    def get_header_value(self):
        check_for_range(self.start, self.end)
        return '{0.unit}={0.start}-{0.end}'.format(self)
