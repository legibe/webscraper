

class Factory(object):

    """
        Just registering classes and creating instances them
    """

    registry = {}

    @classmethod
    def register(cls, name, class_):
        cls.registry[name] = class_

    @classmethod
    def create(cls, definition, *args, **kwargs):
        class_ = definition['type']
        if not class_ in cls.registry:
            raise IndexError('Unkown type: %s' % class_)
        return cls.registry[class_](definition, *args, **kwargs)