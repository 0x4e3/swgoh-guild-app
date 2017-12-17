# coding=utf-8
from __future__ import unicode_literals, absolute_import

from django.db import models
from django.utils.translation import ugettext as _

import scrapy

from dynamic_scraper.models import Scraper, SchedulerRuntime
from scrapy_djangoitem import DjangoItem


UNIT_TYPE_CHOICES = (
    (0, _('Character')),
    (1, _('Ship'))
)


class UnitPage(models.Model):
    title = models.CharField(
        _('Title'),
        max_length=32)
    url = models.URLField()
    unit_type = models.PositiveSmallIntegerField(
        _('Unit type'),
        choices=UNIT_TYPE_CHOICES, default=0)
    scraper = models.ForeignKey(
        Scraper,
        blank=True, null=True,
        on_delete=models.SET_NULL)
    scraper_runtime = models.ForeignKey(
        SchedulerRuntime,
        blank=True, null=True,
        on_delete=models.SET_NULL)

    class Meta:
        verbose_name = _('Unit page')
        verbose_name_plural = _('Unit pages')

    def __str__(self):
        return self.title


class Character(models.Model):
    unit_page = models.ForeignKey(UnitPage)

    name = models.CharField(
        _('Name'),
        max_length=64)
    unit_type = models.PositiveSmallIntegerField(
        _('Unit type'),
        choices=UNIT_TYPE_CHOICES, default=0)

    checker_runtime = models.ForeignKey(
        SchedulerRuntime,
        blank=True, null=True,
        on_delete=models.SET_NULL)

    class Meta:
        verbose_name = _('Персонаж')
        verbose_name_plural = _('Персонажи')

    def __str__(self):
        return self.name


class Ship(models.Model):
    unit_page = models.ForeignKey(UnitPage)

    name = models.CharField(
        _('Name'),
        max_length=64)
    unit_type = models.PositiveSmallIntegerField(
        _('Unit type'),
        choices=UNIT_TYPE_CHOICES, default=1)

    checker_runtime = models.ForeignKey(
        SchedulerRuntime,
        blank=True, null=True,
        on_delete=models.SET_NULL)

    class Meta:
        verbose_name = _('Корабль')
        verbose_name_plural = _('Корабли')

    def __str__(self):
        return self.name


class CharacterItem(DjangoItem):
    django_model = Character


class ShipItem(DjangoItem):
    django_model = Ship
