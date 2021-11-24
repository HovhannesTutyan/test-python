class example:
    def __init__(self):
        print('one')
    def __init__(self):
        print('second')
    def __init__(self):
        print('three')

e=example() # three ## the last constructor will overwrite the previous ones.
# In programming, polymorphism means the same function name (but different signatures) being used for different types.
# The class constructors can be made to exhibit polymorphism in three ways which are listed below.
# Overloading constructors based on arguments.
# Calling methods from __init__.
# Using @classmethod decorator.
#################################################################################################################################
class sample:

    # constructor overloading
    # based on args
    def __init__(self, *args):

        # if args are more than 1
        # sum of args
        if len(args) > 1:
            self.ans = 0
            for i in args:
                self.ans += i

        # if arg is an integer
        # square the arg
        elif isinstance(args[0], int):
            self.ans = args[0] * args[0]

        # if arg is string
        # Print with hello
        elif isinstance(args[0], str):
            self.ans = "Hello! " + args[0] + "."


s1 = sample(1, 2, 3, 4, 5)
print("Sum of list :", s1.ans)   # Sum of list : 15

s2 = sample(5)
print("Square of int :", s2.ans) # Square of int : 25

s3 = sample("GeeksforGeeks")
print("String :", s3.ans) # String : Hello! GeeksforGeeks.

#################################################################################################################################

class eval_equations:

    # single constructor to call other methods
    def __init__(self, *inp):

        # when 2 arguments are passed
        if len(inp) == 2:
            self.ans = self.eq2(inp)

        # when 3 arguments are passed
        elif len(inp) == 3:
            self.ans = self.eq1(inp)

        # when more than 3 arguments are passed
        else:
            self.ans = self.eq3(inp)

    def eq1(self, args):
        x = (args[0] * args[0]) + (args[1] * args[1]) - args[2]
        return x

    def eq2(self, args):
        y = (args[0] * args[0]) - (args[1] * args[1])
        return y

    def eq3(self, args):
        temp = 0
        for i in range(0, len(args)):
            temp += args[i] * args[i]

        temp = temp / max(args)
        z = temp
        return z


inp1 = eval_equations(1, 2)
inp2 = eval_equations(1, 2, 3)
inp3 = eval_equations(1, 2, 3, 4, 5)

print("equation 2 :", inp1.ans) # equation 2 : -3
print("equation 1 :", inp2.ans) # equation 1 : 2
print("equation 3 :", inp3.ans) # equation 3 : 11.0

#################################################################################################################################

# Using @classmethod decorator

class eval_equations:

    # basic constructor
    def __init__(self, a):
        self.ans = a

    # expression 1
    @classmethod
    def eq1(cls, args):
        # create an object for the class to return
        x = cls((args[0] * args[0]) + (args[1] * args[1]) - args[2])
        return x

    # expression 2
    @classmethod
    def eq2(cls, args):
        y = cls((args[0] * args[0]) - (args[1] * args[1]))
        return y

    # expression 3
    @classmethod
    def eq3(cls, args):
        temp = 0

        # square of each element
        for i in range(0, len(args)):
            temp += args[i] * args[i]

        temp = temp / max(args)
        z = cls(temp)
        return z


li = [[1, 2], [1, 2, 3], [1, 2, 3, 4, 5]]
i = 0

# loop to get input three times
while i < 3:

    inp = li[i]

    # no.of.arguments = 2
    if len(inp) == 2:
        p = eval_equations.eq2(inp)
        print("equation 2 :", p.ans)

    # no.of.arguments = 3
    elif len(inp) == 3:
        p = eval_equations.eq1(inp)
        print("equation 1 :", p.ans)

    # More than three arguments
    else:
        p = eval_equations.eq3(inp)
        print("equation 3 :", p.ans)

    # increment loop
    i += 1

    # equation
    # 2: -3
    # equation
    # 1: 2
    # equation
    # 3: 11.0