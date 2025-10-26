from django.db import models

class Game(models.Model):
    player_x = models.CharField(max_length=50)
    player_o = models.CharField(max_length=50)
    winner = models.CharField(max_length=1, choices=[('X','X'),('O','O'),('D','Draw')], blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.player_x} vs {self.player_o}"
