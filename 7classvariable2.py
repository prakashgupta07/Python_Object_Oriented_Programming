#class variable part 2
class Laptop:
        discount_percentage=10# class variable
        def __init__(self,brand, model_name, price):
                self.brand=brand
                self.name=model_name
                self.price=price
                self.laptop_name=brand + ' ' + model_name
        
        def discount(self):
                off_price=(self.discount_percentage/100)*self.price
                return self.price-off_price

#Laptop.discount_percentage  =100  #TO FIX YOUR DISCOUNT
laptop1=Laptop("dell","gd11h",45000)
laptop2=Laptop("hp","gd11111h",35000)
laptop2.discount_percentage=50
print(laptop2.__dict__)#to find the element of object
print(laptop2.discount())
print(laptop1.discount())
