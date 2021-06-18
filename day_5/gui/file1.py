# GUI -> tkinter module
from tkinter import *

root = Tk()

root.title("Small Calculator")
root.geometry("300x300")


# Label -> to write something
# Entry -> to take the input from the user
# Button -> to create a button on the root window

Label(root, text="My first app").grid(column=0, row=0)

num1 = Entry(root)
num1.grid(column=0, row=1)

num2 = Entry(root)
num2.grid(column=1, row=1)

def addNum():
    if num1.get()=="":
        a = 0
    else:
        a = int(num1.get())
    if num2.get()=="":
        b = 0
    else:
        b = int(num2.get())
    result = a+b
    Label(root, text=str(result)).grid(column=1,row=2)

Button(root, text="ADD", command = addNum).grid(column=0, row=2)




root.mainloop()