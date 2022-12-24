#exercise 3
class Person:
        count_instance=0
        def __init__(self,first_name,last_name,age):
                Person.count_instance+=1
                self.first=first_name
                self.last=last_name
                self.age=age
                
        
p1=Person("pra","gup",23)
p2=Person("pra","gup",23)
p3=Person("pra","gup",23)
p4=Person("pra","gup",23)
print(Person.count_instance)