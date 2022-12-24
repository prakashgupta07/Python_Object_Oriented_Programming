#Encapsulation
#Abstraction
#Some special namimg convention
#Name Mangling#  __name()  not a convension
class Phone:
        def __init__(self,brand, model_name,price):
                self.brand=brand
                self.model_name=model_name
                self.__price=price
        def make_a_call(self,phone_number):
                print(f"calling {phone_number}....")
        
        def full_name(self):
                return f"{self.brand} {self.model_name}"
        
        #def send_message(self):
         #       pass#twilio

#_name # convenstion of private name
#__name__ #dunder/magice methods
 
p1=Phone("nokia","huh56",12000)
# print(p1._price)
# p1.__price=11000
#print(p1.__price)
print(p1.__dict__)
#{'brand': 'nokia', 'model_name': 'huh56', '_Phone__price': 12000}
print(p1._Phone__price)
p1._Phone__price=10000
print(p1._Phone__price)
