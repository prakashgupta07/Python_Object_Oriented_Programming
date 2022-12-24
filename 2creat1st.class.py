#objective
#what is class
#how to create an class
# what is init method/constructor
# what are attributes, instance variable
# how to create our object
class Person:
        def __init__(self, first_name, last_name, age):
                #instancr variable
                self.first_name=first_name
                self.last_name=last_name
                self.age=age
        

p1=Person("prakash","kumar",24)
p2=Person("rohit","kumar",22)
print(p1.last_name)
