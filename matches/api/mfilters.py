from django_filters import rest_framework as filters
from django.db import models
from ..models import Match


class MatchFilter(filters.FilterSet):
    class Meta:
        model = Match
        fields = ('league', 'motd', 'home', 'away', 'date')
        filter_overrides = {
            models.CharField: {
                'filter_class': filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
            models.DateField: {
                'filter_class': filters.DateFilter,
                'extra': lambda f: {
                    'lookup_expr': 'exact',
                },
            },
        }
