class ToornamentException(Exception):
    """The Base Exception for all Exceptions raised in toornament"""


class BadRange(ToornamentException):
    """Raised if a Range is bad."""


class ScopeError(ToornamentException):
    """Raised if there where Problems with a scope"""


class UnknownScope(ScopeError):
    """Raised if a scope was provided, that is unknown."""

    def __init__(self, unknown_scope=None):
        self.unknown_scope = unknown_scope
        if unknown_scope is None:
            m = "A Scope was unknown."
        else:
            m = "The scope(s) `{}` is unknown.".format(unknown_scope)

        super().__init__(m)
