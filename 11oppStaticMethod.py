#oop static method
class Person:
        count_instance=0 # class variable/ class attribute
        def __init__(self,first_name,last_name,age):
                Person.count_instance+=1
                self.first=first_name
                self.last=last_name
                self.age=age
                self.full_name=first_name+''+last_name
        @classmethod
        def from_string(cls,string):#class method as a constuctor
                first,last,age=string.split(",")
                return cls(first,last,age)
        @staticmethod
        def hello():
                print(" hello static method called")

        @classmethod
        def count_instances(cls):# class method
                return f"you have created {cls.count_instance} instance of {cls.__name__} class"
        
        def full_name(self):
                return f"{self.first} {self.last}"
        
        
p1=Person("prakash","gupta",23)
p2=Person("pra","gup",23)
p3=Person.from_string("prakash,gupta,24")
print(p3.age)

print(Person.count_instances())
print(p3.full_name)
Person.hello()