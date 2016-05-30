from factory import Factory
from tagfinder import TagFinder
from parent import Parent


class Sibling(Parent):

    """
        Returns the first sibling which is a tag of a tag matched
    """

    def find_tag(self, soup):
        found = super(Sibling, self).find_tag(soup)[0]
        return [TagFinder.find_first_sibling_tag(found)]


Factory.register('sibling', Sibling)