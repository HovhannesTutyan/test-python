from .basket import Basket

def basket(request):
    return {'basket':Basket(request)} # after basket.py and __init__ need to add context_proc also to settings and command.txt to test sessions
