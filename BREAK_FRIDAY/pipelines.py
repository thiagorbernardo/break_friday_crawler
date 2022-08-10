# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
import json
from datetime import datetime


class BreakFridayPipeline:
    def open_spider(self, spider):
        current_time = datetime.now().strftime("%H-%M-%S")
        print("\n\n\nOPENING PACKAGES PIPELINE\n\n\n")
        self.file = open(f"results_break_packages-{current_time}.txt", "w")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item

class HotelsPipeline:
    def open_spider(self, spider):
        current_time = datetime.now().strftime("%H-%M-%S")
        print("\n\n\nOPENING HOTELS PIPELINE\n\n\n")
        self.file = open(f"results_break_hotels-{current_time}.txt", "w")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item