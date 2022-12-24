#class method
#difference between class method and instance method
#exercise 3
class Person:
        count_instance=0 # class variable/ class attribute
        def __init__(self,first_name,last_name,age):
                Person.count_instance+=1
                self.first=first_name
                self.last=last_name
                self.age=age
        @classmethod
        def count_instances(cls):# class method
                return f"you have created {cls.count_instance} instance of {cls.__name__} class"
        
        def full_name(self):
                return f"{self.first} {self.last}"
        
        
p1=Person("prakash","gupta",23)
p2=Person("pra","gup",23)
p3=Person("pra","gup",23)

print(Person.count_instances())