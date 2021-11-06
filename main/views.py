from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Game

def main_view(request):
    return render(request, 'games/main.html', {})
def game_detail_view(request, pk):
    obj = get_object_or_404(Game, pk=pk)
    return render(request, 'games/detail.html', {'obj':obj})
def search_results(request):
    if request.is_ajax():
        game = request.POST.get('game')
        # print(game)
        qs = Game.objects.filter(name__icontains=game)
        # print(qs)
        if len(qs) > 0 and len(game) > 0:
            data = []
            for pos in qs:
                item = {
                    'pk':pos.pk,
                    'name':pos.name,
                    'studio':pos.studio,
                    'image':str(pos.image.url)
                }
                data.append(item)
            results = data
        else:
            results = 'No game found...'
        return JsonResponse({'dt':results})
    return JsonResponse({})