from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Game, Team

admin.site.register(Game)
admin.site.register(Team)
