import unittest
from bs4 import BeautifulSoup
from pagereader import PageReader
from webscraper.tagfinder import TagFinder, TagNotFound
from webscraper.tagutils import TagUtils


class TestTagFinder(unittest.TestCase):

    def setUp(self):
        reader = PageReader()
        self.story = BeautifulSoup(reader('story.html'), 'html.parser')

    def test_find_at_least_one(self):
        found = TagFinder.find_at_least_one(self.story, 'a', class_='sister')
        self.assertGreaterEqual(len(found), 0)
        with self.assertRaises(TagNotFound):
            found = TagFinder.find_at_least_one(self.story, 'a', class_='brother')

    def test_find_exactly(self):
        found = TagFinder.find_exactly(self.story, 3, 'a', class_='sister')
        self.assertEqual(3, len(found))
        with self.assertRaises(TagNotFound):
            found = TagFinder.find_exactly(self.story, 4, 'a', class_='sister')

    def test_find_tag(self):
        # make sure we find the first one
        found = TagFinder.find_tag(self.story, 'p')
        self.assertEqual(TagUtils.contents(found), 'The Dormouse\'s story')
        # make sure we find the next one coming.
        found = TagFinder.find_tag(self.story, 'div', class_='Character1')
        found = TagFinder.find_tag(found, 'a')
        self.assertEqual(TagUtils.contents(found), 'Elsie')
        with self.assertRaises(TagNotFound):
            found = TagFinder.find_tag(self.story, 'div', 'Character4')

    def test_find_first_sibling_tag(self):
        # find a div, then the sibling div, in the sibling search for
        # a link, the contents should be 'Lacie'
        found = TagFinder.find_tag(self.story, 'div', class_='Character1')
        found = TagFinder.find_first_sibling_tag(found)
        found = TagFinder.find_tag(found, 'a')
        self.assertEqual(TagUtils.contents(found), 'Lacie')
        # <a...>Lacie</a> has no siblings
        with self.assertRaises(TagNotFound):
            found = TagFinder.find_first_sibling_tag(found)

    def test_float_contents(self):
        found = TagFinder.find_tag(self.story, 'b')
        price = TagUtils.float_contents(found)
        self.assertEqual(price, 2300.34)

if __name__ == '__main__':
    unittest.main()
