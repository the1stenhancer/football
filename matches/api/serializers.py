from rest_framework import serializers
from ..models import *


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('name',)


class LeagueSerializer(serializers.ModelSerializer):

    class Meta:
        model = League
        fields = ('name',)


class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields = ('fh', 'sh', 'ft', 'o1', 'o2', 'ot')


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('fh', 'sh', 'ft', 'o1', 'o2', 'ot')


class MatchSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    league = LeagueSerializer(read_only=True)
    predictions = PredictionSerializer(read_only=True)
    results = ResultSerializer(read_only=True)

    class Meta:
        model = Match
        fields = ('id', 'country', 'league', 'fixture', 'postponed', 'hot_pick', 'home', 'away', 'date', 'time', 'predictions', 'results')
