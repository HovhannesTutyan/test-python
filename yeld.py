def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3

for value in simpleGeneratorFun():
    print(value)
# 1
# 2
# 3

################################################################
def nextSquare():
    i = 1
    # An Infinite loop to generate squares
    while True:
        yield i * i
        i += 1

for num in nextSquare():
    if num > 100:
        break
    print(num)
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# 100
################################################################