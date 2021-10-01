s = {65,41,27,77,77,65} # Unordered collection of unique elements, unchangable
type(s) # <class 'set'>
l = [65,41,27,27,77,77] # List items are ordered, changeable, and allow duplicate values.
type(l)

l[0] # 65
l[1] #41
s[0] #set object does not support indexing

l # [65,41,27,27,77,77]
s #{65, 27, 77, 41} sets does not output tuples
s.add(99)
s # {65, 99, 41, 77, 27}
s.remove(77) #{65, 99, 41, 27}
s
l.append(88)
l #[65,41,27,27,77,77,88] 
l.append[33,44]
l #[65,41,27,27,77,77,88,[33,44]] 
l.extend([4,5,6,7])
l #[65,41,27,27,77,77,88,[33,44],4,5,6,7 ]
l.insert(2, 34)
l #[65,41,34,27,27,77,77,88,[33,44],4,5,6,7 ]
s = {'str', 1, 3}
s # {1, 3, 'str'}
s.add(-8)
s #{-8, 1, 3, 'str'}


# l = [x for x in range(100)]
# s = {x for x in range(100)}
l = [65,41,27,27,77,77,99]
def insertList(j):
    lookingFor=41
    for i, el in enumerate(l): # i is index and el is element of i index
        if el == lookingFor:
            l.append(i)
insertList(55)
print(l)
# lookingFor in s
# s.add(333)
# s.remove(5)
# s

listofnum=[i for i in range(0,10)]
print(listofnum) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#this is equal to 
listofnum = list(range(10))
print(listofnum) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#////////////////////////////*************\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
listofnum2 = [i for i in range(0,10,2)]
print(listofnum2) #[0, 2, 4, 6, 8]
#this is equal to
listofnum2 = list(range(0,10,2))
print(listofnum2) #[0, 2, 4, 6, 8]

text = "word1anotherword23nextone456lastone333"
numbers = [x for x in text if x.isdigit()] #  "for each x in text, if x.isdigit() is True, add it to the list"
print(numbers) # ['1', '2', '3', '4', '5', '6', '3', '3', '3']

li = [x for x in range(20)]
print(li) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
licopy = li[:]
print(licopy) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
#//////////////////////////***************\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

stringWithCommas='Hi,Python,is,awsome'
strlist = stringWithCommas.split(',')
print(strlist) #['Hi', 'Python', 'is', 'awsome']

#put all characters in a string to list
str2 = "hello"
str2lst=list(str2)
print(str2lst) #['h', 'e', 'l', 'l', 'o']

#put each digit in integer to list

integer=123456
int2lst=[int(i) for i in str(integer)]
print (int2lst) #[1, 2, 3, 4, 5, 6]

#converting dictionary keys/values to list
my_dict = {'a':1, 'b':2, 'c':3, 'd':4}
print(my_dict) #{'a': 1, 'b': 2, 'c': 3, 'd': 4}
key_list=list(my_dict.keys())
print(key_list)
value_list = list(my_dict.values())
print(value_list) #[1, 2, 3, 4]

#list.insert() method
list2 = ['penguin', 'parrot', 'crane', 'sparrow', 'goose']
print(list2) #['penguin', 'parrot', 'crane', 'sparrow', 'goose']

list2.insert(2,'owl')
print(list2) #['penguin', 'parrot', 'owl', 'crane', 'sparrow', 'goose']
Sparrowindex=list2.index('sparrow')
print(Sparrowindex) #4
list2.insert(Sparrowindex+1,'duck')
print(list2) # ['penguin', 'parrot', 'owl', 'crane', 'sparrow', 'duck', 'goose']

#list.remove() method
list2 = ['penguin', 'parrot', 'owl', 'crane']
print(list2) #['penguin', 'parrot', 'owl', 'crane']

list2.remove('parrot')
print(list2) #['penguin', 'owl', 'crane']

#list.pop() method
list3 = ['penguin', 'parrot', 'owl', 'crane']
print(list3) #['penguin', 'parrot', 'owl', 'crane']

popped = list3.pop()
print(popped) #crane
print(list3) #['penguin', 'parrot', 'owl']

popped1 = list3.pop(1)
print(popped1) #parrot
print(list3) # ['penguin', 'owl']

#list.sort() method
list4 = [65,41,37,77,55]
list4.sort()
print(list4) #[37, 41, 55, 65, 77]

list4.sort(reverse=True)
print(list4) #[77, 65, 55, 41, 37]

#list.reverse() method
list4.reverse()
print(list4) #[37, 41, 55, 65, 77]

#len, min, max methods
list1 = [65,44,33,78,90]
print(list1) #[65, 44, 33, 78, 90]
list1len = len(list1)
print(list1len) #5
maxValue=max(list1)
print(maxValue) #90
minValue = min(list1)
print(minValue) #33

#list.count method
list1 = ['A', 'A', 'B', 'C', 'A']
print(list1) #['A', 'A', 'B', 'C', 'A']
countA = list1.count('A')
print(countA)  #3
if 'D' in list1:
    print("list1 has 'D'") 
else:
    print("list1 has no D") #list1 has no D

#for loops on lists
a = ['cat', 'dog', 'duck', 'parrot']
print(a) #['cat', 'dog', 'duck', 'parrot']

for i in a:
    print(i)
# cat
# dog
# duck
# parrot
for i in range(0,len(a)):
    print('index:' + str(i) + " | value:" + a[i]) 
#index:0 | value:cat
# index:1 | value:dog
# index:2 | value:duck
# index:3 | value:parrot
# l = [x for x in range(10)]
# print(l)
# l = [65,41,27,77,52]
# for x in range(len(a)):
#     if l[x] == 77:
#         print("list contains 77") 
#     else: 
#         print('List has no 77')
my_list = ['apples','pears','oranges','fruits']
for x, element in enumerate(my_list):
    print(x,element)
# 0 apples
# 1 pears
# 2 oranges
# 3 fruits
    if element == 'pears':
        print("index " + str(i) + " contains pears")
    else:
        print("Pears not found")
        #Pears not found
        #index 2 contains pears
        #Pears not found
        #Pears not found

    
my_list2 = ['apples', 'bananas', 'oranges', 'kiwies', 'pears']
for x in range (0,len(my_list2)):
    if my_list2[x] == 'bananas':
        my_list2.insert(x+1,'fruits')
print(my_list2) # ['apples', 'bananas', 'fruits', 'oranges', 'kiwies', 'pears']

index = 0 
values = [65,41,27,77]
for value in values:
    print(index, value)
    index += 1
# 0 65
# 1 41
# 2 27
# 3 77
#//////////////Random function\\\\\\\\\\\\\\\\\\\\
def randomR(li):
    import random
    li = [x for x in range(100) if x % 2 == 0] # for each x in range 100 if x % 2 == 0 is true put in list x 
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

randomR(li)

#///////////////dictionary\\\\\\\\\\\\\\\\\
s = 'hellomynameis'
counts = {}
for char in s:
    if char in counts:
        counts[char] += 1
    else:
        counts[char] = 1
for key,i in counts.items():
    print(key,i)


mydict = {'name' : 'Max', 'age' : 28, 'city' : 'new-york'}
print(mydict) # {'name': 'Max', 'age': 28, 'city': 'new-york'}

#looping throught dictionaries
for k,v in mydict.items():
    print(k,v)
# name Max
# age 28
# city new-york

#looping throught sequence
for i,v in enumerate(['tic', 'tac', 'toe']):
    print(i,v)
# 0 tic
# 1 tac
# 2 toe

# To loop over two or more sequences at the same time, the entries can be paired with the zip() function
questions = (['name', 'quest', 'favorite color'])
answers = (['loncelot', 'the holy grale', 'black'])
for q,a in zip(questions, answers):
    print("What is your {0}? : It is {1}".format(q,a))

# What is your name? : It is loncelot
# What is your quest? : It is the holy grale
# What is your favorite color? : It is black


mydict2 = dict(name = "max", age = 25, city = "York")
print(mydict2) # {'name': 'max', 'age': 25, 'city': 'York'}

value = mydict['name']
print(value) # Max

mydict['email'] = 'cincopa@online.py'
print(mydict) # {'name': 'Max', 'age': 28, 'city': 'new-york', 'email': 'cincopa@online.py'}

del mydict['age']
print(mydict) #{'name': 'Max', 'city': 'new-york', 'email': 'cincopa@online.py'}
if 'name' in mydict:
    print(mydict['name']) #Max
for value in  mydict.values():
    print(value)
    # Max
    # new-york
    # cincopa@online.py
for key, value in mydict.items():
    print(key, value)
    # name Max
    # city new-york
    # email cincopa@online.py
mydict_cpy = mydict
print(mydict_cpy) #{'name': 'Max', 'city': 'new-york', 'email': 'cincopa@online.py'}
mydict_cpy['email'] = 'akfhjd@aldjf.com'
print(mydict_cpy) #{'name': 'Max', 'city': 'new-york', 'email': 'akfhjd@aldjf.com'}
print(mydict)    # {'name': 'Max', 'city': 'new-york', 'email': 'akfhjd@aldjf.com'}

mydict_cpy2 = mydict2.copy()
print(mydict_cpy2) #{'name': 'max', 'age': 25, 'city': 'York'}
mydict_cpy2['email'] = 'akfjkdf@main.online'
print(mydict_cpy2) # {'name': 'max', 'age': 25, 'city': 'York', 'email': 'akfjkdf@main.online'}
print(mydict2) # {'name': 'max', 'age': 25, 'city': 'York'}
mydict.update(mydict2)
print(mydict) #{'name': 'max', 'city': 'York', 'email': 'akfhjd@aldjf.com', 'age': 25}

# ////////////////Collections in Python //////////////////////////
from collections import Counter
a = 'aaaaaaaaaaaacccccccdddfffffff'
my_count = Counter(a)
print(my_count) # Counter({'a': 12, 'c': 7, 'f': 7, 'd': 3})
print(my_count.values()) # dict_values([12, 7, 3, 7])
print(my_count.keys()) #dict_keys(['a', 'c', 'd', 'f'])
print(my_count.most_common(1)) #[('a', 12)]
for i in my_count.values():
    if i == 12:
        print("12 exists") #12 exists

from collections import namedtuple
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt) #Point(x=1, y=-4)
print(pt.x, pt.y) # 1 -4

from collections import deque
d = deque()
d.append(1)
d.append(2)
print(d) #deque([1, 2])
d.appendleft(3)
print(d) #deque([3, 1, 2]) 
for i in d:
    if i == 3:
        print("i esixts") #i esixts
d.extendleft([4,5,6])
print(d) #deque([6, 5, 4, 3, 1, 2])
d.rotate()
print(d) # deque([2, 6, 5, 4, 3, 1])

#////////////// Itertools \\\\\\\\\\\\\\\\
from itertools import product
a = [1,2]
b = [3,4]
prod = product(a,b)
print(list(prod)) # [(1, 3), (1, 4), (2, 3), (2, 4)]

#///////////// Lambda Functions \\\\\\\\\\\\\\\\\\\
add10 = lambda x: x + 10
print(add10(5)) #15

mult = lambda x,y: x * y
print(mult(4,5)) # 20

points2D = [(1,2), (15,1), (5,-1), (10,4)]
points2D_sorted = sorted(points2D)
print(points2D) #[(1, 2), (15, 1), (5, -1), (10, 4)]
print(points2D_sorted) # [(1, 2), (5, -1), (10, 4), (15, 1)] sorted by x[0]
points2D_sorted = sorted(points2D, key = lambda x: x[1])
print(points2D_sorted) # [(5, -1), (15, 1), (1, 2), (10, 4)] sorted by x[1]

a = [1,2,3,4,5]
b = map(lambda x: x*2, a)
print(list(b)) # [2, 4, 6, 8, 10]
# this is the same as
c = [x * 2 for x in a]
print(c) # [2, 4, 6, 8, 10]

d = filter(lambda x: x % 2 == 0, a)
print(list(d)) # [2,4]
#this is the same as 
e = [x for x in a if x % 2 == 0]
print(e) # [2,4]

#////////////////map function///////////////
# map() function takes two arguments: a function and a list. It then applies the function 
# to all of the values of the list and creates new values with the returned values from the function.
li = [x for x in range(10)]
def funct(x):
    return x ** x 
new_li = []
for i in li:
    new_li.append(funct(i))
print(new_li) # [1, 1, 4, 27, 256, 3125, 46656, 823543, 16777216, 387420489]

# this is the same as  

print(list(map(funct, li))) #[1, 1, 4, 27, 256, 3125, 46656, 823543, 16777216, 387420489]

# this is the same as
print([funct(x) for x in li]) #[1, 1, 4, 27, 256, 3125, 46656, 823543, 16777216, 387420489]

#/////////////////filter function/////////////
#filter() function takes two arguments (function, iterable) and applies the function 
# to all of the items in the iterable. If the function returns a True value then that item will be added to a new list.
def add7(y):
    return y + 7
def isOdd(x):
    return x % 2 == 0
a = [x for x in range(10)]
print(a) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(filter(isOdd,a))) #  [0, 2, 4, 6, 8]
print(list(map(add7,filter(isOdd,a)))) # [7, 9, 11, 13, 15]
 
#////////////////////// Nested List Comprehension /////////////////////////
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed) # [[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]]

print([[row[i] for row in matrix] for i in range(4)]) #[[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]]

matr = [
    [65,41,27],
    [77,52,33],
    [18,99,79]
]
transp = []
# for i in range(3):
#     transp.append([col[i] for col in matr])
# print(transp)

# for i in range(3):
#     for j in range(3):
#         print(matr[i][j])
for i in range(3):
    transp.append(matr[i])
print(transp) #[[65, 41, 27], [77, 52, 33], [18, 99, 79]]

for i in range(3):
    for col in matr:
        transp.append(col[i])
print(transp) # [65, 77, 18, 41, 52, 99, 27, 33, 79]

#///////////////////////////CLASS - PARAMETR, INSTANCE OBJECT - ATTRIBUTE REFERENCE/////////////////////////////////////////////////////
#Class objects support two kinds of operations: attribute references and instantiation (obj.name).
#The only operations understood by instance objects(x) are attribute references(r,i).
#A method is a function that “belongs to” an object.
class Complex:
    def __init__(self, realPart, imaginaryPart):
        self.r = realPart
        self.i = imaginaryPart
    def addRI(self,r,i):
        return (self.r + self.i)
x = Complex(4.6, 3.8)
print (x.r , x.i) # 4.6 3.8
print (x.addRI(x.r, x.i)) # 8.399999999999999

class Dog:
    kind = "Canine"
    tricks = []
    def __init__(self, name):
        self.n = name
    def addTrick(self, n, trick):
        self.tricks.append(trick)
        print(self.n, "can now do ",trick)
        print(self.n, "can now do ", self.tricks)

x = Dog("Banny")
print (x.n) # Banny
x.addTrick(x.n, "give a hand") # Banny can now do  give a hand
                               # Banny can now do  ['give a hand']

class Cat:
    def __init__(self, name):
        self.n = name
    def addTrick(self, n, trick):
        print(self.n, "can now " , trick)

C = Cat("Joy")
print(C.n) #Joy
trick = "MOW"
C.addTrick(C.n, trick) # Joy can now  MOW


def adder(*args):
    sum=0
    for n in args:
        sum=sum+n
    print("sum: ", sum)

adder(34,45,56,67,78,89)

def intro(**kwargs):
    for key, value in kwargs.items():
        print("{} is {}".format(key, value))

intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)