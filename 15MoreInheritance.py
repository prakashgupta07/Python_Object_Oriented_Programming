#more about inheritance,multileve,MRO(method resolution order), method overriding,etc
# can we drive more than one class from base class
# multilevel inheritance
#method resolution order(hrlp(class name) it give mro)
#method overriding 
#isinstance( to find object inside class or not ,its give value in true or false),
# issubclass(to find the class inheritance class or not,it gives true or false value)
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
        def full_name(self): #method overriding
            return f"{self.brand} {self.model_name} {self._price}"

        
class FlagshipPhone(Smartphone):# multilevel inheritance                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
    def __init__(self,brand, model_name,price,ram,memory,camera,back_camera):
        super().__init__(brand, model_name,price,ram,memory,camera)
        self.back_camera=back_camera
    def full_name(self): #method overriding
        return f"{self.brand} {self.model_name} {self._price} {self.camera}"


smartphone=Smartphone('1+',5,23000,"6GB","64GB","20MP")
smartphone1=FlagshipPhone('1+',5,23000,"6GB","64GB","20MP","22MP")

# print(smartphone.full_name())
#print(smartphone.back_camera)
# print(help(smartphone))# method resolution order
#print(smartphone.make_a_call(9465446951))
# print(isinstance(smartphone,FlagshipPhone))# to find object in class or not
# print(isinstance(smartphone1,Phone))#to find object in class or not

print(issubclass(Smartphone,FlagshipPhone))
print(issubclass(Smartphone,Phone))


