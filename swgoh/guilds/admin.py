# coding=utf-8
from __future__ import unicode_literals, absolute_import

from django.contrib import admin
from django.contrib.admin.decorators import register

from . import models


@register(models.Guild)
class GuildAdmin(admin.ModelAdmin):
    pass


@register(models.GuildMember)
class GuildMemberAdmin(admin.ModelAdmin):
    pass
