import scrapy
from country_list import countries_for_language
import random

from BREAK_FRIDAY.items import BreakFridayBanner

class HurbSpider(scrapy.Spider):
    name = "Hurb"
    allowed_domains = ['hurb.com']
    start_urls = []
    # start_urls = ['https://www.hurb.com/br']
    # start_urls = ["http://127.0.0.1:5500/hurb.html"]

    def __init__(self):
        print("\nINIT PACKAGES\n")
        start_urls = []
        # countries = [("pt_br", "brasil")]
        countries = countries_for_language("pt_br")
        random.shuffle(countries)
        for country in countries:
            options = [
                f"https://www.hurb.com/br/search/packages?q={country[1]}&tab=packages&page={i}"
                for i in range(1, 5)
            ]
            start_urls.extend(options)
        self.start_urls = start_urls

    def parse(self, response):
        print("PACKAGES PAGE: ", response.url)
        options = []
        for div in response.css("a"):
            package = div.css(".Packages_PackageCard__2lqTN").getall()
            if package:
                url = div.css("a::attr(href)").extract_first()
                options.append(url)

        for option in options:
            yield response.follow(option, self.parse_banner)

    def parse_banner(self, response):
        print("PACKAGE: ", response.url)
        for div in response.css("div"):
            banner_break = div.css(".banner-break").getall()
            if banner_break:
                print("\n\n\nFOUND BANNER PACKAGE: ", banner_break, "\n\n\n")
                yield BreakFridayBanner(name=div.css(".banner-break").extract_first(), url=response.url)
