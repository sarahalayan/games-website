from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Game(models.Model):
    name=models.TextField(max_length=100, default="gameA")
    description=models.TextField(max_length=10000, default="Your Default Description Here")
    def __str__(self):
        return self.name
class Player(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,unique=False)
    selected_game = models.ForeignKey(Game, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.user.username


class GamePlayer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE,unique=False)
    game_data = models.JSONField()
    timestamp = models.DateTimeField(default=timezone.now)
    

    
