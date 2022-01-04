from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .basket import Basket, Product
from django.db.models import Q

def basket_summary(request):
    basket = Basket(request)
    return render(request, 'shop/basket/summary.html', {'basket':basket})

def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)
        basketqty = basket.__len__()
        response = JsonResponse({'qty':basketqty})
        return response
def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        basket.delete(product=product_id)
        response = JsonResponse({'Success':True})
        return response
def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        basket.update(product=product_id, qty=product_qty)
        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({'qty':basketqty, 'total':baskettotal})
        return response
def basket_list(request):
    kw = request.GET.get('keyword')
    results = Product.objects.filter(Q(title__icontains=kw) |Q(description__icontains=kw)|Q(author__icontains=kw))
    return render(request, 'shop/list.html', {'results':results})
