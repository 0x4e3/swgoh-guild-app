# coding=utf-8
from __future__ import unicode_literals, absolute_import

from django.contrib import admin
from django.contrib.admin.decorators import register

from . import models


@register(models.UnitPage)
class UnitPageAdmin(admin.ModelAdmin):
    pass


@register(models.Character)
class CharacterAdmin(admin.ModelAdmin):
    pass


@register(models.Ship)
class ShipAdmin(admin.ModelAdmin):
    pass
