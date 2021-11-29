import scrapy
from country_list import countries_for_language
import random

from BREAK_FRIDAY.items import BreakFridayBanner
#https://www.hurb.com/br/search/hotels?q=brasil&tab=hotels&rooms=2&page=30
class HurbSpider(scrapy.Spider):
    name = "Hurb"
    allowed_domains = ['hurb.com']
    start_urls = []
    # start_urls = ['https://www.hurb.com/br']
    # allowed_domains = ["http://127.0.0.1:5500"]
    # start_urls = ["http://127.0.0.1:5500/hurb.html"]

    def __init__(self):
        start_urls = []
        countries = countries_for_language("pt_br")
        random.shuffle(countries)
        for country in countries:#[:10]:
            options = [
                f"https://www.hurb.com/br/search/packages?q={country[1]}&tab=packages&page={i}"
                for i in range(1, 5)
            ]
            start_urls.extend(options)
        self.start_urls = start_urls

    def parse(self, response):
        options = []
        for div in response.css("a"):
            banner_break = div.css(".hrc-1_8b9").getall()
            if banner_break:
                url = div.css("a::attr(href)").extract_first()
                options.append(url)

        for option in options:
            yield response.follow(option, self.parse_banner)

    def parse_banner(self, response):
        print(response.url)
        for div in response.css("div"):
            banner_break = div.css(".banner-break").getall()
            if banner_break:
                yield BreakFridayBanner(name=div.css(".banner-break").extract_first(), url=response.url)
