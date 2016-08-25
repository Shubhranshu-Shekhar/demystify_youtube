import scrapy
from scrapy.selector import Selector
from demystify_youtube.items import YoutubeItem

__author__ = 'shubhranshu.shekhar'

class YouTubeSpider(scrapy.Spider):
    name = "youtube"
    allowed_domains = ["www.youtube.com"]
    #start_urls = [
    #    "https://www.youtube.com/watch?v=WXHM_i-fgGo",
    #    "https://www.youtube.com/watch?v=Tk4ubu7BlSk",
    #    "https://www.youtube.com/watch?v=3mNJHceB08M"
    #]

    def __init__(self, filename=None):
       if filename:
           with open(filename, 'r') as f:
               self.start_urls = [url.strip() for url in f.readlines()]

    def parse(self, response):
        """ This functions reads YouTube response and extracts all that we need :)"""
        hxs = Selector(response)
        #This item is required to save all the data
        item = YoutubeItem()


        video_name = hxs.xpath("//div[@id='watch-headline-title']//span[@class='watch-title']/@title").extract()[0]
        video_url = response.url

        #description contains html tags as well because description has embedded links etc.
        p_tag_desc = hxs.xpath("//div[@id='watch-description-text']//p[@id='eow-description']/text()").extract()
        video_description = " ".join(p_tag_desc)
        video_category = hxs.xpath("//div[@id='watch-description-extras']//ul[@class='content watch-info-tag-list']//a/text()").extract()[0]
        num_views = hxs.xpath("//div[@class='watch-view-count']/text()").extract()

        user_sentiment = hxs.xpath("//div[@id='watch8-sentiment-actions']//button//span[@class='yt-uix-button-content']/text()").extract()
        num_like = user_sentiment[0]
        num_dislike = user_sentiment[2]

        user = hxs.xpath("//div[@id='watch7-user-header']//div[@class='yt-user-info']/a/@href").extract()[0]
        suggested_videos = list(set(hxs.xpath("//ul[@id='watch-related']//a/@href").extract()))
        next_video = hxs.xpath("//div[@class='autoplay-bar']//ul[@class='video-list']//a/@href").extract()[0]
        crawl_depth = str(response.meta['depth'])

        #Populate our youtube item to be saved
        item['video_url'] = video_url
        item['video_name'] = video_name
        item['video_description'] = video_description
        item['video_category'] = video_category
        item['num_views'] = num_views
        item['num_likes'] = num_like
        item['num_dislikes'] = num_dislike
        item['user'] = user
        item['suggested_videos'] = suggested_videos
        item['next_video'] = next_video
        item['crawl_depth'] =  crawl_depth
        yield item

        for watch_url in suggested_videos:
            yield scrapy.Request("https://www.youtube.com"+watch_url, callback=self.parse)
        yield scrapy.Request("https://www.youtube.com"+next_video, callback=self.parse)














