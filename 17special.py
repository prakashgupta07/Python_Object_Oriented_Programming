# special magic methods/ dunder methods ,
# operator overloading
# polymorphism-method overriding 
class Phone:
        def __init__(self,name,model_name,price):
                self.name=name
                self.model=model_name
                self.price=price
        def phone_name(self):
                return f"{self.name} {self.model}"
        
        # dunder method# /special magic method 
        # str,repr# # to use to print object as it is
        def __str__(self):
                return f"{self.name} {self.model}"
        
        def __repr__(self):
                # return f"{self.name} {self.model} {self.price}"
                 return f'Phone(\'{self.name}\',\'{self.model}\',\'{self.price}\')'
        def __len__(self):
                return len(self.phone_name())
        
# operator overloading
        def __add__(self,other): # operator overloading
                return self.price +other.price
#polymorphism
class SmartPhone(Phone):
        def __init__(self,name,model_name,price,camera):
                Phone.__init__(self,name,model_name,price)
                # super().__init__(name,model_name,price)
                self.camera=camera
        def phone_name(self):
            return f"{self.name} {self.model} {self.price} {self.camera}"

my_phone=Phone("nokia","1100",1200)
my_phone2=Phone("nokia","1600",1300)
my_smartphone=SmartPhone("oneplus","5t",33000,"16mp")
print(my_smartphone.phone_name())
print(my_phone.phone_name())





# print(my_phone + my_phone2)
# print(str(my_phone))
# print(len(my_phone))
# print(my_phone.__len__())
# print(repr(my_phone))
# print(my_phone.__str__())
# print(my_phone)


