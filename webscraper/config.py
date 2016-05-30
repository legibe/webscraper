import os
import re


class Config(object):

    """
        Utility class from my private library
    """

    cache = {}

    @classmethod
    def read(cls, path, cache=True):
        """
            Reads either json or yaml files. Recognises the format using
            the file extension. If environment variable are part of the
            path, they are substituted with their values.
        """
        path = cls.substitute_env_variables(path)
        if not cache or not path in cls.cache:
            l = path.split('.')
            with open(path) as f:
                if l[-1] == 'json':
                    import json

                    cls.cache[path] = json.load(f)
                elif l[-1] == 'yaml':
                    import yaml

                    cls.cache[path] = yaml.load(f)
                else:
                    raise IOError('Cannot handle that kind of file %s' % l[-1])
        return cls.cache[path]

    @classmethod
    def substitute_env_variables(cls, a):
        """
        Finds variables in string in the form: ${varname} and replaces
        their value if an environment variable with the same name is found
        """
        if isinstance(a, basestring):
            variables = re.findall('\${(.*?)}', a)
            for var in variables:
                default = var.split(':-')
                v = os.getenv(default[0])
                if v is None and len(default) > 1:
                    v = default[1]
                if v is not None:
                    a = re.sub('\${%s}' % var, v, a)
        return a
