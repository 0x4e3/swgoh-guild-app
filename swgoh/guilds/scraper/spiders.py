# coding=utf-8
from __future__ import unicode_literals, absolute_import

from dynamic_scraper.spiders.django_spider import DjangoSpider

from swgoh.guilds import models


class GuildSpider(DjangoSpider):
    name = 'guild_spider'

    def __init__(self, *args, **kwargs):
        self._set_ref_object(models.Guild, **kwargs)
        self.scraper = self.ref_object.scraper
        self.scrape_url = self.ref_object.url
        self.scheduler_runtime = self.ref_object.scraper_runtime
        self.scraped_obj_class = models.GuildMember
        self.scraped_obj_item_class = models.GuildMemberItem
        super(GuildSpider, self).__init__(self, *args, **kwargs)
