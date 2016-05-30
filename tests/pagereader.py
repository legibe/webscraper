import os


class PageReader(object):

    def __init__(self):
        self._path = os.path.join(os.path.dirname(__file__),'html')

    def __call__(self, filename):
        with open(os.path.join(self._path, os.path.basename(filename))) as f:
            return f.read()
