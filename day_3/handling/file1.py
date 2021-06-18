# Error handling in python

    # Example 1
# try:
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))

#     result = num1/num2  # ZeroDivisionError
#     print("%0.3f"%result)

# except ZeroDivisionError:
#     print("You cannot divide a number by zero.")
# except ValueError:
#     print("Invalid input, must be numbers.")
    

    # Example 2
# def func():
#     try:
#         num1 = int(input("Enter the first number: "))
#         num2 = int(input("Enter the second number: "))

#         result = num1/num2  # ZeroDivisionError
#         print("%0.3f"%result)

#     except (ZeroDivisionError, ValueError):
#         print("Invlaid input\nTry Again")
#         func()
# func()

#     # Example 3
# try:
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))

#     result = num1/num2  # ZeroDivisionError
#     print("%0.3f"%result)

# except: 
#     print("Invalid input")

# finally:
#     print("BYEE!!!!!!!!!!!!!!!!!!")


