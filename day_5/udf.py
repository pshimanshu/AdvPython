# some extra features of UDF -> User Defined Functions

# 1.
# def f1(x,y):
#     print(x)
#     print(y)

# f1([12,23])

# # 2 default values for the function parameters!
# def f1(x=100, y=16):
#     print(x)
#     print(y)
# f1(34,56)
# f1()
# # f1(45,56,3)  -> doesn't work


# *args -> n number of parameters 

# def f1(x, y, *args, **kwargs):
#     print(type(x), x)
#     print(type(y), y)
#     print(type(args), args)
#     print(type(kwargs), kwargs)
# f1(10,20,"hello", "py", a=100, b=12, c=23, d="hey")



# Lambda Functions
# we use lamda function

# a = lambda x:2*x
# print(a(28))

# a = lambda x,y:x*y
# print(a(23,30))

func = lambda x,y : x if x>y else y
print(func(23,32))