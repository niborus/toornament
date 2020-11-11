class ToornamentException(Exception):
    """The Base Exception for all Exceptions raised in toornament"""


class BadRange(ToornamentException):
    """Raised if a Range is bad."""
