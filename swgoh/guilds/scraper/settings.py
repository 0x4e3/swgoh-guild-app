# coding=utf-8
from __future__ import unicode_literals, absolute_import

import os
import sys


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
sys.path.insert(0, os.path.join(PROJECT_ROOT, "../../.."))

BOT_NAME = 'guilds'

LOG_STDOUT = False
LOG_LEVEL = 'INFO'


SPIDER_MODULES = [
    'dynamic_scraper.spiders',
    'swgoh.guilds.scraper',
    'swgoh.units.scraper'
]

USER_AGENT = '{b}/{v}'.format(b=BOT_NAME, v='1.0')

ITEM_PIPELINES = {
    'dynamic_scraper.pipelines.DjangoImagesPipeline': 200,
    'dynamic_scraper.pipelines.ValidationPipeline': 400,
    'swgoh.guilds.scraper.pipelines.DjangoWriterPipeline': 800,
}

DSCRAPER_LOG_ENABLED = True
DSCRAPER_LOG_LEVEL = 'ERROR'
DSCRAPER_LOG_LIMIT = 5
