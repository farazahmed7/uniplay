from django.contrib.gis.geos import Point
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from spinder.models import Game


@csrf_exempt
@api_view(['POST','GET'])
def create_game(request):
    if request.method=="POST":
        lon=str(request.POST['longitude'])
        lat=str(request.POST['latitude'])
        type=str(request.POST['type'])
        location = Point((float(lon), float(lat)))
        game=Game.objects.create(location=location)
        return HttpResponse("done")


