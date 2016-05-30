

class Member(object):
    """
        Root class for members of an HTML family tree
    """
    def __init__(self, definition, name):
        self._definition = definition
        self._name = name