# -*- coding: utf-8 -*-
import scrapy


class MowSpider(scrapy.Spider):
    name = "mow"
    allowed_domains = ["eventcinemas.com.au"]
    start_urls = ['https://www.eventcinemas.com.au/Promotions/MemberMovieOfTheWeek']

    def parse(self, response):
        mow_text = response.css('.movie-data')[0].xpath('@data-movies').extract_first()
        yield {
            'movie_name': mow_text,
        }
