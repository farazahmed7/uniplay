from rest_framework import serializers
from django.contrib.auth.models import User
from spinder.models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    isNew=serializers.BooleanField(default=True)
    class Meta:
        model=UserProfile
        fields = '__all__'

