# coding=utf-8
from __future__ import unicode_literals, absolute_import

from dynamic_scraper.spiders.django_spider import DjangoSpider

from swgoh.units import models


class UnitsSpider(DjangoSpider):
    name = 'units_spider'
    custom_settings = {
        'ITEM_PIPELINES': {
            'dynamic_scraper.pipelines.DjangoImagesPipeline': 200,
            'dynamic_scraper.pipelines.ValidationPipeline': 400,
            'swgoh.units.scraper.pipelines.DjangoWriterPipeline': 800,
        }
    }

    def __init__(self, *args, **kwargs):
        self._set_ref_object(models.UnitPage, **kwargs)
        self.scraper = self.ref_object.scraper
        self.scrape_url = self.ref_object.url
        self.scheduler_runtime = self.ref_object.scraper_runtime
        if self.ref_object.unit_type == 0:
            self.scraped_obj_class = models.Character
            self.scraped_obj_item_class = models.CharacterItem
        else:
            self.scraped_obj_class = models.Ship
            self.scraped_obj_item_class = models.ShipItem
        super(UnitsSpider, self).__init__(self, *args, **kwargs)
