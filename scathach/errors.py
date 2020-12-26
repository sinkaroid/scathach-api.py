class scathachException(Exception):
    """ Base exception class for scathach.py """

    pass


class NothingFound(scathachException):
    """ The API didn't return anything """

    pass


class EmptyArgument(scathachException):
    """ When no target is defined """

    pass


class InvalidArgument(scathachException):
    """ Invalid argument within the category """

    pass
