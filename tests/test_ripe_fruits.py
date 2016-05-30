import unittest
import os
from pagereader import PageReader
from webscraper.config import Config
from ripefruits import RipeFruits

class TestRipeFruits(unittest.TestCase):

    """
        We test the application with the data it has been written against. Web pages were
        save statically to enable us to reproduce the result at the time of deployment.
        If there is a regression in the code, it will be spotted immediately,
        if the application breaks, it would help to have reference data.
    """

    def test_assessement(self):
        start = 'http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/5_products.html'
        scenarios = Config.read(os.path.join(os.path.dirname(__file__), '..', 'scenarios.yaml'))
        fetcher = PageReader()
        processor = RipeFruits()
        result = processor.process(start, fetcher, scenarios)
        self.assertGreater(len(result), 0)

        reference = Config.read(os.path.join(os.path.dirname(__file__), 'result.json'))
        self.assertEqual(result, reference)

if __name__ == '__main__':
    unittest.main()
