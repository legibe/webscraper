import os
import json
from webscraper.config import Config
from webscraper.pagefetcher import PageFetcher
from webscraper.tagconsumer import TagConsumer
from webscraper.tagutils import TagUtils

class RipeFruits(object):

    def process(self, start, fetcher, scenarios):
        consumer = TagConsumer(scenarios, fetcher)
        results = consumer('ripe fruits', url=start)
        data = []
        total_price = 0
        for result in results:
            item = {}
            # get the <a> tag which contains the title and a url
            tag = result['product.productInfo.link']
            item['title'] = TagUtils.contents(tag)
            page = fetcher(tag['href'])
            # save the size of the sub-page
            item['size'] = '%1.2fkb' % (float(len(page)) / 1024)

            # run the 'description' scenario to find the description in the page
            res = consumer('description', page=page)
            item['description'] = TagUtils.contents(res['itemHeader.description'])

            # get the <p> tag containing the description.
            tag = result['product.price']
            item['unit_price'] = TagUtils.float_contents(tag)
            total_price += item['unit_price']
            data.append(item)

        output = {}
        output['results'] = data
        output['total'] = round(total_price, 2)
        return output

if __name__ == '__main__':
    start = 'http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/5_products.html'
    scenarios = Config.read(os.path.join(os.path.dirname(__file__), 'scenarios.yaml'))
    fetcher = PageFetcher()
    processor = RipeFruits()
    result = processor.process(start, fetcher, scenarios)
    print json.dumps(result, indent=4)
