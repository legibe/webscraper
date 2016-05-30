from bs4 import BeautifulSoup
from factory import Factory


class TagConsumer(object):

    """
        Entry-point class to search for tags
    """

    def __init__(self, scenarios, fetcher):
        self._scenarios = scenarios
        self._fetcher = fetcher

    @property
    def fetcher(self):
        return self._fetcher

    def __call__(self, scenario_name, url = None, page = None):
        if url is not None:
            page = self._fetcher(url)
        soup = BeautifulSoup(page, 'html.parser')
        scenario = self._scenarios[scenario_name]
        p = Factory.create(scenario, scenario['name'])
        return p.process(soup, self)
