from django.shortcuts import render,get_object_or_404
import json

from django.http import JsonResponse
from .models import Game, GamePlayer,Player,User

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import redirect
from django.urls import reverse

@login_required
def index(request):
    games = Game.objects.all()
    return render(request, 'game/index.html', {'games': games})

@login_required
@require_POST
def save_game_score(request):
    if request.method == "POST":
        
       
            # Parse the JSON data from the request body
        data = json.loads(request.body.decode("utf-8"))

        game_name = data.get("game")
        print(game_name)
        player_id = data.get("player_id")
        print(player_id)
        gameData = data.get("gameData")
        print(f"game data is {gameData}")
        user = User.objects.get(id=player_id)
        game=Game.objects.get(name=game_name)
        if not player_id:
            return JsonResponse({"success": False, "message": "Player ID not found."}, status=400)

        # Create a new Player instance for each play session
        player = Player.objects.create(user=user, selected_game=game)

        # Create a new GamePlayer instance for the score
        game_player = GamePlayer.objects.create(
            player=player,
            game_data=gameData
        )
       
        return JsonResponse({"success": True, "message": "Score saved"}, status=200)
        
    else:
        return JsonResponse({"message": "Invalid request method."})
    

def game_play(request):
    game_name = request.GET.get('game_name')
    previous_score = request.GET.get('score')
    template_name = f'games/{game_name.lower()}_game.html'
    return render(request, template_name, context={'game_name': game_name, 'previous_score': previous_score})


def flappy(request):
    flappy_game = Game.objects.filter(name="Flappy Bird").first()

    
    game_id = flappy_game.id
    return render(request, 'game/flappybird.html',{'flappy_game_id': game_id})
def base(request):
    rock_game = Game.objects.filter(name="Rock Paper Scissors").first()

    
    game_id = rock_game.id
    
    return render(request, 'game/base.html',{'rock_game_id': game_id})
def alternative(request):
    asteroid_game = Game.objects.filter(name="Asteroids").first()

    
    game_id = asteroid_game.id
    return render(request, 'game/alternative.html',{'asteroids_game_id': game_id})

def game_about(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'game/about.html', {'game': game})

def high_scores(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    high_scores = GamePlayer.objects.filter(player__selected_game=game).order_by('-game_data__score')
    
    print(high_scores)
    for score in high_scores:
        print(score.game_data)
    return render(request, 'game/high_scores.html', {'game': game, 'high_scores': high_scores})