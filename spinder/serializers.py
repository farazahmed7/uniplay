from rest_framework import serializers
from django.contrib.auth.models import User
from spinder.models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields=('isNew',)
