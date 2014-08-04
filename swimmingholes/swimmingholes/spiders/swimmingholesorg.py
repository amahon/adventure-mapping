import re
from urlparse import urlparse

from bs4 import BeautifulSoup
import scrapy

from swimmingholes.items import SwimmingHole

class SwimmingholesSpider(scrapy.Spider):
    name = 'swimmingholesorg'
    allowed_domains = [
        'swimmingholes.org',
    ]
    start_urls = [
        'http://www.swimmingholes.org/vt.html',
    ]

    def parse(self, response):
        for table_sel in response.xpath('//*[@id="width"]/tbody/tr/td/table'):
            
            # making soup from a table
            table_soup = BeautifulSoup(table_sel.extract())


            # let's extract the primary name
            # we'll just xpath because it's pretty well defined
            name_extract = table_sel.xpath('tbody/tr[1]/th/h3[1]/font/text()').extract()
            if not len(name_extract):
                continue
            name = name_extract[0].strip()

            metadata_dict = {}

            for tr_sel in table_sel.xpath('tbody/tr'):
                th_extract = tr_sel.xpath('th/text()').extract()
                if not len(th_extract):
                    continue
                key_name = th_extract[0].strip().lower().replace('\n','').replace(' ','')
                if not len(key_name):
                    continue
                if key_name == 'lat,lon':
                    continue
                metadata_dict[key_name] = ''.join(tr_sel.xpath('td//text()').extract())\
                    .strip()\
                    .replace('\t','')\
                    .replace('\n','')

            # let's extract the swimming hole locations
            # associate the metadata
            # and save the SwimmingHole Items
            # we're searching through the soup because our data is not well structured
            google_maps_links = table_soup.find_all('a', text=re.compile('Link to Google Map'))
            if not(len(google_maps_links)):
                continue
            if len(google_maps_links) == 1:
                my_item = SwimmingHole()
                my_item.update(metadata_dict)
                my_item['name'] = name
                my_item['latlon'] = urlparse(google_maps_links[0]['href']).query
                yield my_item 
            elif len(google_maps_links) > 1:
                for link in google_maps_links:
                    my_name = link.find_previous_sibling('font')
                    if not(my_name):
                        my_name = link.parent.find_previous_sibling('font')
                    if not(my_name):
                        print(name)
                        continue
                    row_header = link.parent.parent.parent.parent.find('th')
                    if row_header:
                        replace_field = row_header.find(text=True).lower().strip()
                    if not replace_field or not len(replace_field):
                        replace_field = 'directions'
                    my_descriptive = my_name.next_sibling
                    if not hasattr(my_name, 'text'):
                        print (name)
                    my_item = SwimmingHole()
                    my_item.update(metadata_dict)
                    my_item['parent_name'] = name
                    my_item['name'] = my_name.text
                    my_name[replace_field] = my_descriptive
                    my_item['latlon'] = urlparse(link['href']).query
                    yield my_item
