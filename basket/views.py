from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from basket.basket import Basket
from store.models import Product


def basket_summary(request):
    basket = Basket(request)
    return render(request, 'store/basket/summary.html', {'basket': basket})
def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)
        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty})
        return response

def basket_list(request):
    game = request.POST.get('game')
    qs = Product.objects.filter(title__icontains=game)
    if len(qs) > 0 and len(game) > 0:
        data=[]
        for pos in qs:
            item = {
                'pk': pos.pk,
                'title': pos.title,
                'author': pos.author,
                'description': pos.description,
                'image': pos.image.url
            }
            data.append(item)
        res = data
    else:
        res = 'No games found...'
    return JsonResponse({'data':res})


