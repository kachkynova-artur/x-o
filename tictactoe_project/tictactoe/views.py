from django.shortcuts import render, redirect, get_object_or_404
from .models import Game

def game_list(request):
    games = Game.objects.all().order_by('-created_at')
    return render(request, 'tictactoe/game_list.html', {'games': games})

def add_game(request):
    if request.method == 'POST':
        Game.objects.create(
            player_x=request.POST['player_x'],
            player_o=request.POST['player_o']
        )
        return redirect('game_list')
    return render(request, 'tictactoe/add_game.html')

def edit_game(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.method == 'POST':
        game.player_x = request.POST['player_x']
        game.player_o = request.POST['player_o']
        game.winner = request.POST.get('winner', '')
        game.save()
        return redirect('game_list')
    return render(request, 'tictactoe/edit_game.html', {'game': game})

def delete_game(request, pk):
    game = get_object_or_404(Game, pk=pk)
    game.delete()
    return redirect('game_list')

def play_game(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return render(request, 'tictactoe/play_game.html', {'game': game})
