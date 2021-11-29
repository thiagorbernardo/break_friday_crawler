import scrapy
from country_list import countries_for_language
import random

from BREAK_FRIDAY.items import BreakFridayBanner

class HotelsSpider(scrapy.Spider):
    name = 'Hotels'
    allowed_domains = ['hurb.com']
    start_urls = []

    def __init__(self):
        print("\nINIT HOTELS\n")
        start_urls = []
        countries = [("pt_br", "brasil")]
        # countries = countries_for_language("pt_br")
        random.shuffle(countries)
        for country in countries:
            options = [
                f"https://www.hurb.com/br/search/hotels?q={country[1]}&tab=hotels&rooms=2&page={i}"
                for i in range(1, 2)
            ]
            start_urls.extend(options)
        self.start_urls = start_urls

    def parse(self, response):
        print("HOTELS PAGE: ", response.url)
        options = []
        for div in response.css("a"):
            hotel = div.css(".hrc-1_8b9").getall()
            print(div.get())
            if hotel:
                url = div.css("a::attr(href)").extract_first()
                options.append(url)

        for option in options:
            yield response.follow(option, self.parse_banner)

    def parse_banner(self, response):
        print("HOTEL: ", response.url)
        for div in response.css("div"):
            banner_break = div.css(".banner-break").getall()
            if banner_break:
                print("\n\n\nFOUND BANNER HOTEL: ", banner_break, "\n\n\n")
                yield BreakFridayBanner(name=div.css(".banner-break").extract_first(), url=response.url)
