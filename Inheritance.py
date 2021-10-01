class Pet:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f"i am {self.name} and i am {self.age} years old and my color is {self.color}")
    def speak(self):
        print("I dont know what i say")
    
class Cat(Pet):
    def speak(self):
        print("Meaw")

class Dog(Pet):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color=color

    def spead(self):
        print("Bark")

# p=Pet("Tim",19)
# p.speak()

# c=Cat("Mishel",23)
# c.show()

d=Dog('name', 12,23)
d.show()