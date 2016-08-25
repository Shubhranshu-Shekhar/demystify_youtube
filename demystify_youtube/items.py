# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YoutubeItem(scrapy.Item):
    # define the fields for your item here like:
    video_url = scrapy.Field()
    video_name = scrapy.Field()
    video_description = scrapy.Field()
    video_category = scrapy.Field()
    num_views = scrapy.Field()
    num_likes = scrapy.Field()
    num_dislikes = scrapy.Field()
    user = scrapy.Field()
    suggested_videos = scrapy.Field()
    next_video = scrapy.Field()
    #num_comments = scrapy.Field()
    #commentors = scrapy.Field()
    crawl_depth = scrapy.Field()