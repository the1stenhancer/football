from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'cc']
    list_filter = ['name', 'cc']


@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = ['id', 'country', 'name']
    list_filter = ['id', 'country', 'name']


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ['league', 'fixture', 'home', 'away', 'date', 'time', 'results', 'motd']
    list_filter = ['league', 'fixture', 'home', 'away', 'date', 'motd']
    ordering = ('date', 'time')


@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = ['id', 'fh', 'sh', 'ft', 'o1', 'o2', 'ot']


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'fh', 'sh', 'ft', 'o1', 'o2', 'ot']
