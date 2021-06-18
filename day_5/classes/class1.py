# # Classes and objects
#  # class -> group of methods
#  # class -> collection of attributes and methods
#  # class attribute and instance attribute

# class Employee:
#     hours = 40  # class attr. -> common to all instances

# emp1 = Employee()
# emp2 = Employee()

# print(emp1.hours)
# print(emp2.hours)
# #print(emp1.hours==emp2.hours)

# # incstance attr. -> these attributes are specific to each instance/object of the classes
# emp1.name = "john"
# emp2.name = "sam"

# print(emp1.name)
# print(emp2.name)


# # self parameter
# class Employee:
#     def f1(self):       # self parameter refers to the object itself
#         print("Hello World")
#     def f2(self):
#         print("Hello python")
# emp1 = Employee()
# emp1.f1()
# Employee.f1(emp1)
# emp1.f2()


# class Employee:
#     def f1(self):
#         self.name = "Sam"   # instance attribute
#         age = 25
#         # the lifespan of this attribute is this function
#         # once the method is terminates you cannot use this attribute in any other method
#         print(self.name)
#         print(age)
#         #self.f2()

#     def f2(self):
#         print(self.name)
#         # print(age) -> age isnt defined, hence cant be accessed here, only exists in f1
#         #self.f1()

# emp1 = Employee()
# emp1.f1()
# emp1.f2()

# # special method -> __init__ -> constructor in python
# class Employee:
#     def __init__(self): # we use __init__ to intialize all th attributes of our objects of our class before they are being used
#     # it is the first method that is being at the time of the creation of object
#         self.name = "sam"
#     def f2(self):
#         print(self.name)
# emp1 = Employee()
# emp1.f2()


# final structure

# class Employee:
#     def __init__(self, first, last, phone, address):
#         self.first = first
#         self.last = last
#         self.phone = phone
#         self.address = address
#     def fullName(self):
#         return "{} {}".format(self.first, self.last)
#     def fullAddress(self):
#         return "{}, {}".format(self.fullName(), self.address)

# emp1 = Employee("sam", "kumar", 78043, "delhi")
# emp2 = Employee("john", "wick", 23452, "bangalore")

# # print(emp1.fullName())
# # print(emp2.fullName())

# print(emp1.fullAddress())
# print(emp2.fullAddress())


