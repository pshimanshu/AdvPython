# GUI -> tkinter module
from tkinter import *
import csv
import time
import smtplib
from email.mime.multipart import MIMEMultipart


root = Tk()

root.title("Ticketing Software")
root.geometry("400x400")


# Label -> to write something
# Entry -> to take the input from the user
# Button -> to create a button on the root window

Label(root, text="Ticket Dispenser").grid(column=1, row=0)

Label(root, text="Name: ").grid(column=0, row=1)
Label(root, text="Age: ").grid(column=0, row=2)
Label(root, text="Email: ").grid(column=0, row=3)

n = Entry(root)
n.grid(column=1, row=1)
a = Entry(root)
a.grid(column=1, row=2)
e = Entry(root)
e.grid(column=1, row=3)


Label(root, text="From: ").grid(column=2, row=1)
Label(root, text="To: ").grid(column=2, row=2)

# def show():
#     label.config(text = clicked.get())
cities = ["None", "Delhi", "Pune", "Hyderabad", "Bangalore", "Goa", "Chennai", "Lucknow"]
from_city = StringVar()
from_city.set("None")
origin_om = OptionMenu(root, from_city, *cities).grid(column=4,row=1)

to_city = StringVar()
to_city.set("None")
dest_om = OptionMenu(root, to_city, *cities).grid(column=4, row=2)

# Label(root, textvariable=from_city).grid(column=3,row=12)
# Label(root, textvariable=to_city).grid(column=3,row=13)


def createTicket():
    name = n.get()
    age = a.get()
    email = e.get()
    origin = from_city.get()
    destination = to_city.get()

    f = open("ticket.csv", "w", newline="")
    obj = csv.writer(f)
    data = []
    data.append(["Name:", name])
    data.append(["Age", age])
    data.append(["Email", email])
    data.append(["From", origin])
    data.append(["To", destination])
    ct = time.ctime()
    ct = ct[4:10]+ct[20:]
    data.append(["Date of Booking", ct])
    obj.writerows(data)
    f.close()
Button(root, text="Store Data", command = createTicket).grid(column=1, row=9)

def sendTicket():
    pass
    # name = n.get()
    # age = a.get()
    # email = e.get()
    # origin = from_city.get()
    # destination = to_city.get()
    
    # message = MIMEMultipart()
    # message["Subject"] = "Ticket Booking Recipt!!"
    # message["From"] = "Universal Ticket Dispensary"
    # uname = "pshimanshu@gmail.com"
    # pwd = "Uma1devi"
    # sender = uname 
    # receiver = input("Enter the receiver's email id: ") + "@gmail.com"


Button(root, text="Send Ticket", command = sendTicket).grid(column=4,row=9)




root.mainloop()