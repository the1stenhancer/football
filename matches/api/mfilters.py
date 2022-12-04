from django_filters import rest_framework as filters
from django.db import models
from ..models import Match


class MatchFilter(filters.FilterSet):
    country = filters.CharFilter(field_name="country__name", lookup_expr='icontains')
    class Meta:
        model = Match
        fields = ('country', 'hot_pick')

