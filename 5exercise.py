#exercise 2
class Laptop:
        def __init__(self,brand, model_name, price):
                self.brand=brand
                self.name=model_name
                self.price=price
        
        def discount(self,num):
                off_price=(num/100)*self.price
                return self.price-off_price

laptop=Laptop("dell","gd11h",45000)
#both are same
print(laptop.discount(10))
print(Laptop.discount(laptop,10))
