#inheritance
class Phone:#base class/parent class
        def __init__(self,brand, model_name,price):
                self.brand=brand
                self.model_name=model_name
                self._price=price
        def make_a_call(self,phone_number):
                print(f"calling {phone_number}....")
        
        def full_name(self):
                return f"{self.brand} {self.model_name}"
        
class Smartphone(Phone): #drived/child class
        def __init__(self,brand, model_name,price,ram,memory,camera):
                #two away
                #Phone.__init__(self,brand,model_name,price)#uncomman away
                super().__init__(brand,model_name,price)# two away
                self.ram=ram
                self.memory=memory
                self.camera=camera

        

        

p1=Phone("nokia","1100",1200)
s1=Smartphone("one+","1+12",25000,"4gb","64gb","16mp")
print(p1.full_name())
print(s1.full_name())