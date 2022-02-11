# ForeignKey - generally known as a many-to-one relationship. Person >--| Birthplace
                                                                ^            ^
                                                                |            |
                                                                Many        One 

class Birthplace(models.Model):
    city = models.CharField(max_length=75)
    state = models.CharField(max_length=25)

    def __unicode__(self):
        return "".join(self.city, ", ", self.state)

class Person(models.Model):
    name = models.CharField(max_length=50)
    birthplace = models.ForeignKey(Birthplace)

    def __unicode__(self):
        return self.name
    
>> from somewhere.models import Birthplace, Person
>> Person.objects.all()
[<Person: John Smith>, <Person: Maria Lee>, <Person: Daniel Lee>]
>> Birthplace.objects.all()
[<Birthplace: Dallas, Texas>, <Birthplace: New York City, New York>]

>> person = Person.object.get(name="John Smith")
>> person.birthplace
<Birthplace: Dallas, Texas>
>> person.birthplace.city
Dallas

>> place = Birthplace.objects.get(city="Dallas")
>> place.person_set.all()
[<Person: John Smith>, <Person: Maria Lee>]

# One-to-one - two objects to having a unique relationship.     User |--| Profile
                                                                  ^          ^
                                                                  |          |
                                                                 One        One
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL) # Note that Django suggests getting the User from the settings for relationship definitions
    fruit = models.CharField(max_length=50, help_text="Favorite Fruit")
    facebook = models.CharField(max_length=100, help_text="Facebook Username")

    def __unicode__(self):
        return "".join(self.fruit, " ", self.facebook)
    
# Many-to-many - Order >--< Project
                   ^           ^
                   |           |
                  Many        Many
class Order(models.Model):
    product = models.CharField(max_length=150)  # Note that in reality, this would probably be better served by a Product model
    customer = models.CharField(max_length=150)  # The same may be said for customers

    def __unicode__(self):
        return "".join(self.product, " for ", self.customer)

class Project(models.Model):
    orders = models.ManyToManyField(Order)

    def __unicode__(self):
        return "".join("Project ", str(self.id))
    
>> Project.objects.all()
[<Project: Project 0>, <Project: Project 1>, <Project: Project 2>]
>> for proj in Project.objects.all():
..     print(proj)
..     proj.orders.all()  # Note that we must access the `orders`
..                        # field through its manager
..     print("")
Project 0
[]
Project 1
[<Order: Spaceship for NASA>]
Project 2
[<Order: Spaceship for NASA>, <Order: Race car for NASCAR>]

>> order = Order.objects.filter(customer="NASA")[0]
>> order.project_set.all()
[<Project: Project 0>, <Project: Project 2>]
