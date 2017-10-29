from allauth.socialaccount.helpers import complete_social_login
from allauth.socialaccount.models import SocialApp, SocialToken, SocialLogin
from allauth.socialaccount.providers.facebook.views import fb_complete_login
from django.contrib.auth.models import User
from django.contrib.gis.geos import Point
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from spinder.models import Game, UserProfile
from spinder.serializers import UserSerializer


@csrf_exempt
def get_token(request):
    if request.method=="POST":
        response=HttpResponse
        access_token =str(request.POST['access_token'])
        #email=str(request.POST['email'])
        try:
            app=SocialApp.objects.get(provider="facebook")
            token=SocialToken(app=app,token=access_token)
             # Check token against facebook
            login = fb_complete_login(request, app, token)
            login.token = token
            login.state = SocialLogin.state_from_request(request)
            # Add or update the user into users table
            ret = complete_social_login(request, login)
            a=SocialToken.objects.get(token=access_token)
            try:
                account=a.account
                user=account.user
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                token=Token.objects.get(user=user)
                return HttpResponse(serializers.serialize("json",[token]))
            except User.DoesNotExist:
                return HttpResponse("User Dosent Exist")
            return HttpResponse("wuhoo")
        except Exception as e:
            # If we get here we've failed
           return HttpResponse("ASdsa "+str(e))

@csrf_exempt
def mobile_facebook_login(request):
    if request.method=="POST":
        response=HttpResponse
        access_token =str(request.POST['access_token'])
        #email=str(request.POST['email'])
        try:
            app=SocialApp.objects.get(provider="facebook")
            token=SocialToken(app=app,token=access_token)
             # Check token against facebook
            login = fb_complete_login(request, app, token)
            login.token = token
            login.state = SocialLogin.state_from_request(request)
            # Add or update the user into users table
            ret = complete_social_login(request, login)
            a=SocialToken.objects.get(token=access_token)
            try:
                account=a.account
                user=account.user
                tuple=UserProfile.objects.get_or_create(user=user,dp=account.get_avatar_url(),fullName=user.get_full_name())

                if tuple[1]==True:
                     Token.objects.create(user=user)
                     UserProfile.objects.update(user=user,isNew=False)
                else:
                    UserProfile.objects.update(user=user,isNew=False)
                ser=UserSerializer(tuple[0])
                return HttpResponse(serializers.serialize("json",[tuple[0]]))
            except User.DoesNotExist:
                return HttpResponse("User Dosent Exist")
            return HttpResponse("wuhoo")
        except Exception as e:
            # If we get here we've failed
           return HttpResponse(str(e)+"")

@csrf_exempt
@api_view(['POST','GET'])
def create_game(request):
    if request.method=="POST":
        user=request.user
        lon=str(request.POST['longitude'])
        lat=str(request.POST['latitude'])
        location = Point((float(lon), float(lat)))
        game=Game.objects.create(host=user,location=location)
        return HttpResponse("done")


