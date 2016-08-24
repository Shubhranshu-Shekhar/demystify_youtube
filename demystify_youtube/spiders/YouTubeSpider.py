import scrapy

__author__ = 'shubhranshu.shekhar'

class YouTubeSpider(scrapy.Spider):
    name = "youtube"
    allowed_domains = ["www.youtube.com"]
    start_urls = [
        "https://www.youtube.com/watch?v=WXHM_i-fgGo"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)