from django.db import models

class Game(models.Model):
    player_x = models.CharField(max_length=50)
    player_o = models.CharField(max_length=50)
    winner = models.CharField(max_length=1, choices=[('X','X'),('O','O'),('D','Draw')], blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.player_x} vs {self.player_o}"

class GameMove(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='moves')
    position = models.IntegerField()  # 0-8
    player = models.CharField(max_length=1, choices=[('X','X'),('O','O')])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('game', 'position')  # одна клетка только один раз
