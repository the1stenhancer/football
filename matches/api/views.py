from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import MatchSerializer
from .mfilters import MatchFilter
from ..models import Match


class MatchListView(generics.ListAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MatchFilter


class MatchDetailView(generics.RetrieveAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
