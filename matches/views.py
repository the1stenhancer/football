from django.shortcuts import render
from .models import Match


# Create your views here.
def match_list(request):
    object_list = Match.objects.all()
    return render(request, 'matches/list.html', {'matches': object_list})


def terms_of_use(request):
    return render(request, 'matches/terms_of_use.html')
