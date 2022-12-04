from django.urls import path
from . import views


app_name = 'matches'


urlpatterns = [
    path('', views.match_list, name='match_list'),
    path('terms_of_use', views.terms_of_use, name='tou'),
]
