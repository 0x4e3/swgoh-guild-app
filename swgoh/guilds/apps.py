# coding=utf-8
from __future__ import unicode_literals, absolute_import

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class GuildsAppConfig(AppConfig):
    name = 'swgoh.guilds'
    verbose_name = _('Гильдия')
