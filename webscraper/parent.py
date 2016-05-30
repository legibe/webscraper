from factory import Factory
from tagfinder import TagFinder
from member import Member


class Parent(Member):

    """
        Defines a class for tags containing other tags
        a match can return more than one result
    """

    def process(self, soup, processor, mapping=None):
        found = self.find_tag(soup)
        if len(found) > 1:
            result = []
            for item in found:
                mapping = {}
                result.append(self.process_inner(item, self._definition['inner'], processor, mapping))
        else:
            if mapping is None:
                mapping = {}
            result = self.process_inner(found[0], self._definition['inner'], processor, mapping)
        return result

    def process_inner(self, item, definition, processor, mapping):
        for inner in definition:
            p = Factory.create(inner, self._name + '.' + inner['name'])
            mapping = p.process(item, processor, mapping)
        return mapping

    def find_tag(self, soup):
        if 'contents' in self._definition:
            return [TagFinder.find_tag_by_contents(soup,
                                                   self._definition['contents'],
                                                   self._definition['tag_name'],
                                                   **self._definition['attr'])]
        return TagFinder.find_at_least_one(soup, self._definition['tag_name'], **self._definition['attr'])


Factory.register('parent', Parent)
