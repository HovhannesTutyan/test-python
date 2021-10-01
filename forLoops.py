b = [65,41,27,77]
for i in b:
    print(i) #65 41 27 77

for i in range(0,len(b)):
    print(i) # 0 1 2 3

for i in range(0,3):
    for j in range(0,4):
        print(i,j)

repeat = input("Enter a whole number:")
repeat = int(repeat)

for i in range(repeat):
    print(i) # 0 1 2 3

list_a = [65,41,27]
for i in range(len(list_a)):
    print(list_a[i]) # 65,41,27