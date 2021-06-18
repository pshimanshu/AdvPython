# Email sending application

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


# create an object of MIMEMultipart
message = MIMEMultipart()
message["Subject"] = "Summer Sale"
# message["Cc"] = "cc@gmail.com"
# message["Bcc"] = "bcc@gmail.com"
message["From"] = "Amazon Company"



# username and password
uname = "pshimanshu@gmail.com"  #input("Enter your email id: ") + "@gmail.com"
pwd = "Uma1devi"    #input("Enter your password: ")

# sender and recevier
sender = uname 
receiver = input("Enter the receiver's email id: ") + "@gmail.com"

# Mail Body
t = '''
<h1> !! SUMMER SALE !! </h1>
<h2> Buy 3 Get 2 FREE!! </h2>
<p> Last 2 days !! Grab  the offer soon!! </p>
<h2> !! Happy Shopping !! </h2>
'''
text = MIMEText(t, "html")  # plain -> if simple string
message.attach(text)

# attaching an image
i = open("img.jpg", "rb")
img = MIMEImage(i.read())
message.attach(img)


# Sending an email

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(uname, pwd)
print("Login successful")

server.sendmail(sender, receiver, message.as_string())
