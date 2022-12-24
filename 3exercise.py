#create a laptop class with attributes like brand name, model name, price 
#craete two object /instance of your laptop class
class Laptop:
        def __init__(self,brand_name,model_name,price):
                self.brand_name=brand_name
                self.model_name=model_name
                self.p=price
                self.laptop_name=brand_name+" "+model_name

lap=Laptop("realme","Dk2513d",57000)
print(lap.laptop_name)