import requests


class PageFetcher(object):

    """
        Uses the requests library to retrieve web pages through HTTP.
    """

    def __call__(self, reference):
        r = requests.get(reference)
        if r.status_code != 200:
            raise IOError('Could not found %s, reason: %d %s' % (reference, r.status_code, r.reason), r.status_code)
        return r.text