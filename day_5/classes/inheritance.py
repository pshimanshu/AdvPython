# INHERITANCE -> 
# enables us to define a class that takes all the functionality from perent class and aloows us to add more,
# the new class is called derived or child class and the one from which it inherits is called base classor parent class

# direct inheritance

# class A:
#     def f1(self):
#         print("f1 from class A")
# class B(A):
#     def f2(self):
#         print("f2 from class B")

# a = A()
# b = B()
# b.f2()
# b.f1()


#Multi-Level Inheritance
# class A:
#     def f1(self):
#         print("f1 from class A")
# class B(A):
#     def f2(self):
#         print("f2 from class B")
# class C(B):
#     def f3(self):
#         print("f3 from class C")

# a = A()
# a.f1()

# b = B()
# b.f2()
# b.f1()

# c = C()
# c.f3()
# c.f2()
# c.f1()


#Multiple Inheritance -> class A and B are not related to each other
# class A:
#     def f1(self):
#         print("f1 form A")
# class B:
#     def f2(self):
#         print("f2 form B")
# class C(A,B):
#     #def f1(self):
#     #    print("f1 from C")
#     def f3(self):
#         print("f3 form C")

# c = C()
# c.f3()
# c.f1()
# c.f2()



# class Vehicle:
#     def generalUsage(self):
#         print("General Usage: Transportation")
# class Car(Vehicle):
#     def __init__(self):
#         print("I am a CAR")
#         self.wheels = 4
#         self.roof = True
#     def specificUsage(self):
#         print("Vacation with family")
# class Bike(Vehicle):
#     def __init__(self):
#         print("I am a BIKE")
#         self.wheels = 2
#         self.roof = False
#     def specificUsage(self):
#         print("Vacation with partner")
        
# c = Car()
# c.generalUsage()
# c.specificUsage()

# b = Bike()
# b.generalUsage()
# b.specificUsage()

