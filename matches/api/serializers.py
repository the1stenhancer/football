from rest_framework import serializers
from ..models import *


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('name', 'cc')


class LeagueSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)

    class Meta:
        model = League
        fields = ('name', 'country')


class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields = ('fh', 'sh', 'ft', 'o1', 'o2', 'ot')


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('fh', 'sh', 'ft', 'o1', 'o2', 'ot')


class MatchSerializer(serializers.ModelSerializer):
    league = LeagueSerializer(read_only=True)
    predictions = PredictionSerializer(read_only=True)
    results = ResultSerializer(read_only=True)

    class Meta:
        model = Match
        fields = ('id', 'league', 'fixture', 'home', 'away', 'date', 'time', 'predictions', 'results')
