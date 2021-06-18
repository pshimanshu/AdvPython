
# special methods or magic methods or dunder methods
# __init__  -> constructor -> to initialize all intance attributes
# __str__ -> string representation of the class


# class Employee:
#     def __init__(self, first, last, address, phone, salary):
#         self.first = first
#         self.last = last
#         self.address = address
#         self.phone = phone
#         self.salary = salary
#     def fullName(self):
#         return "{} {}".format(self.first, self.last)
#     def __str__(self):
#         return "{} - {}".format(self.fullName(), self.phone)
#     def __add__(self, other):
#         return self.salary + other.salary
#     def __len__(self):
#         return len(self.fullName())

# emp1 = Employee("sam", "white", "delhi", 789678, 100000)
# emp2 = Employee("john", "wick", "us", 567345, 200000)

# print(emp1.fullName())
# print(emp1)
# print(emp1+emp2)

# print(len(emp1))