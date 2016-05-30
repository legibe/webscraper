from factory import Factory
from tagfinder import TagFinder
from member import Member


class Child(Member):

    """
        Represents a final tag with no sub-tags
    """

    def process(self, soup, processor, mapping = None):
        found = self.find_tag(soup)
        if mapping is None:
            mapping = {}
        mapping[self._name] = found
        return mapping

    def find_tag(self, soup):
        return TagFinder.find_tag(soup, self._definition['tag_name'], **self._definition['attr'])


Factory.register('child', Child)
