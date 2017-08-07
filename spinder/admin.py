from django.contrib import admin

# Register your models here.
from spinder.models import Game, UserProfile

admin.site.register(UserProfile)
admin.site.register(Game)