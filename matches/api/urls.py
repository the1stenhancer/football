from django.urls import path
from . import views


app_name = 'matches'


urlpatterns = [
    path('predictions/', views.MatchListView.as_view(), name="match_api_list"),
    path('predictions/<pk>/', views.MatchDetailView.as_view(), name="match_api_detail"),
]
