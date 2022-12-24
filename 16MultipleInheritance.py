#multiple inheritance
class A:
        def class_a_method(self):
                return "I\'m just a class A method"
        def hello(self):
                return "hello from class A"
isinstance_a=A()
print(isinstance_a.class_a_method())


class B:
        def class_b_method(self):
                return "I\'m just a class B method"
        def hello(self):
                return "hello from class B "

class C(B,A):
        pass

isinstance_c=C()
print(isinstance_c.class_a_method())
print(isinstance_c.class_b_method())
print(isinstance_c.hello())
#print(help(C))
print(C.mro())
#print(C.__mro__.)