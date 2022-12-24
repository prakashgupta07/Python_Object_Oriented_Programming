  #instance method
class Person:
        def __init__(self,first_name,last_name,age):
                self.first_name=first_name
                self.last_name=last_name
                self.age=age
        def full_name(self):
                return (f"{self.first_name} {self.last_name}")
        
        def is_above(self):
                return self.age>18
                        
p1=Person("prakash","kumar",10)
#print(p1.full_name())#print(Person.full_name(p1))#(both line are same)
print(p1.is_above())#print(Person.is_above(p1)) both are same


# l=[1,2,3]
# clear,pop
#l.clear()#list.clear(l)# both are same
#print(l)

#l.append(10)
# list.append(l,10)
# print(l)