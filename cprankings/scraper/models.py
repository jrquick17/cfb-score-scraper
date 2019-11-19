from django.db import models

# Create your models here.
from django.db import models
from django.db import models
from django.utils import timezone


class Team(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Game(models.Model):
    date = models.DateTimeField('date played')

    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name = 'away_team')
    away_score = models.IntegerField(default=0)

    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name = 'home_team')
    home_score = models.IntegerField(default=0)

    def __str__(self):
        return str(self.date) + ': ' + str(self.home_team) + ' ' + str(self.home_score) + ' vs ' + str(self.away_team) + ' ' + str(self.away_score)
