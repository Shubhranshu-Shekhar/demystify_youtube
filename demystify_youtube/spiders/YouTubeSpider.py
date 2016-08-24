import scrapy
from scrapy.selector import Selector
from demystify_youtube.items import YoutubeItem

__author__ = 'shubhranshu.shekhar'

class YouTubeSpider(scrapy.Spider):
    name = "youtube"
    allowed_domains = ["www.youtube.com"]
    start_urls = [
        "https://www.youtube.com/watch?v=WXHM_i-fgGo"
    ]

    def parse(self, response):
        """ This functions reads YouTube response and extracts all that we need :)"""
        hxs = Selector(response)
        #This item is required to save all the data
        item = YoutubeItem()

        video_title = hxs.xpath("//div[@id='watch-headline-title']//span[@class='watch-title']/@title").extract()[0]


