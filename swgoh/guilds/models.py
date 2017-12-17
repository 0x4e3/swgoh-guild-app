# coding=utf-8
from __future__ import unicode_literals, absolute_import

from django.db import models
from django.utils.translation import ugettext as _

from dynamic_scraper.models import Scraper, SchedulerRuntime
from scrapy_djangoitem import DjangoItem


class Guild(models.Model):
    name = models.CharField(
        _('Название гильдии'),
        max_length=64)
    url = models.URLField(
        _('Ссылка на профиль'))
    scraper = models.ForeignKey(
        Scraper,
        blank=True, null=True,
        on_delete=models.SET_NULL)
    scraper_runtime = models.ForeignKey(
        SchedulerRuntime,
        blank=True, null=True,
        on_delete=models.SET_NULL)

    class Meta:
        verbose_name = _('Гильдия')
        verbose_name_plural = _('Гильдии')

    def __str__(self):
        return self.name


class GuildMember(models.Model):
    guild = models.ForeignKey(Guild)
    username = models.CharField(
        _('Username'),
        max_length=64)
    nickname = models.CharField(
        _('Nickname'),
        max_length=64)
    profile_url = models.URLField(
        _('Ссылка на профиль'))
    galactic_power = models.FloatField(
        _('Galactic power'))
    collection_score = models.FloatField(
        _('Collection score'))

    checker_runtime = models.ForeignKey(
        SchedulerRuntime,
        blank=True, null=True,
        on_delete=models.SET_NULL)

    class Meta:
        verbose_name = _('Профиль игрока')
        verbose_name_plural = _('Профили игроков')

    def __str__(self):
        return self.username


class GuildMemberItem(DjangoItem):
    django_model = GuildMember
