def myfunct(*args):
    for arg in args:
        print(arg)

myfunct('Hello', 'Welcome', 'to', 'GeeksforGeeks')
# Hello, Welcome, to, GeeksforGeeks
#######################################################################
def myfunct2(arg1, *args):
    print("First argument: ", arg1)
    for arg in args:
        print("Next argument in args: ", arg)

myfunct2('Hello', 'Welcome', 'to', 'GeeksforGeeks')
# First argument:  Hello
# Next argument in args:  Welcome
# Next argument in args:  to
# Next argument in args:  GeeksforGeeks
#######################################################################
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


myFun(first='Geeks', mid='for', last='Geeks')
# first == Geeks
# mid == for
# last == Geeks
#######################################################################
def myFun(arg1, **kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

myFun("Hi", first='Geeks', mid='for', last='Geeks')
# first == Geeks
# mid == for
# last == Geeks
#######################################################################
def myFun(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)

myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")
# args:  ('geeks', 'for', 'geeks')
# kwargs:  {'first': 'Geeks', 'mid': 'for', 'last': 'Geeks'}

