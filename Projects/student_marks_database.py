import sqlite3
import csv
import smtplib



def addStudent():
    print("-"*8,"Lets add a new student to the database", "-"*8)
    
    roll_no = int(input("Enter roll number: "))
    while roll_no<=0:
        print("Please choose a positive roll number")
        roll_no = int(input("Enter roll number: "))
    name = input("Enter name: ")
    while not name.isalnum():
        print("Please choose a valid name")
        name = input("Enter name: ")
    mth_marks = int(input("Enter Mathematics marks: "))
    while mth_marks<0 or mth_marks>100:
        print("Enter valid marks between 0 to 100.")
        mth_marks = int(input("Enter Mathematics marks: "))
    phy_marks = int(input("Enter Physics marks: "))
    while phy_marks<0 or phy_marks>100:
        print("Enter valid marks between 0 to 100.")
        phy_marks = int(input("Enter Physics marks: "))
    chm_marks = int(input("Entry Chemistry marks: "))
    while chm_marks<0 or chm_marks>100:
        print("Enter valid marks between 0 to 100.")
        chm_marks = int(input("Enter Chemistry marks: "))
    arr = list((roll_no, name, mth_marks, phy_marks, chm_marks))
    students_db.execute("insert into student values (?,?,?,?,?)",arr)
    students_db.commit()
    print("-"*8,"Data Added Successfully", "-"*8)

def calcPercent():
    name = input("Whose percentgae do you want to calculate: ")
    print("-"*8, "Caluclating percentage of three sujects for %s"%name, "-"*8)
    cursor.execute("select * from student where name = ?", [name])
    present_data = cursor.fetchall()
    print(present_data)
    total_marks = present_data[0][2] + present_data[0][3] + present_data[0][4]
    perc = total_marks/3
    print("The percentage is %0.3f"%perc)
    print("-"*45)

def createReport():
    print("-"*8, "Creating report for all studnets currently in database", "-"*8)
    csv_file = open("students_report.csv", "w", newline="")
    obj = csv.writer(csv_file)
    header = ["Roll_No", "Name", "MTH_Marks", "PHY_Marks", "CHM_Marks", "Percentage", "Status"]
    obj.writerow(header)
    cursor.execute("select * from student")
    data = cursor.fetchall()
    #print(data)
    for row in data:
        row_list = list(row)
        row_list.append((row_list[2]+row_list[3]+row_list[4])/3)
        if row_list[2]<35 or row_list[3]<35 or row_list[4]<35:
            row_list.append("FAIL")
        else:
            row_list.append("PASS")
        #print(row_list)
        obj.writerow(row_list)
    csv_file.close()
    print("-"*8, "!csv file created!", "-"*8)
    

def sendReport():
    # SMTP
    # 1 - server address, 2 - port number
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls() # to make secure connection
    print("----- Connected to the server-----")

    # -> login
    username = input("Enter your email address: ")
    password = input("Enter your password: ")
    server.login(username, password)
    print("-"*8, "Login Successful for %s"%username, "-"*8)

    # -> send an email
    sender = username
    print("1. Send ALL!\n2. Choose a particular person")
    ch = int(input("Enter your choice: "))
    if ch==1:
        cursor.execute("select * from student")
        data = cursor.fetchall()
        for person in data:
            msg = str((person[2] + person[3] + person[4])/3)
            print("Sending %s's data"%person[1])
            receiver = input("Enter the receiver's email id: ")+"@gmail.com"
            server.sendmail(sender, receiver, msg)
    else:
        roll_no = int(input("Enter the roll number whose report you want to send: "))
        cursor.execute("select * from student where roll_no = ?", [roll_no])

    print("-"*8, "Mail sent successfully", "-"*8)

students_db = sqlite3.connect("students_db.sqlite")
cursor = students_db.cursor()
try:
    students_db.execute("create table student (roll_no integer, name text, math_marks integer, phy_marks integer, chm_marks integer)")
except:
    pass

while True:
    print("-"*8,"MAIN MENU","-"*8)
    print("1. Add New Student Data\n2. Calculate Percentage\n3. Create Report in csv Format\n4. Send Report\n5. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        addStudent()
    elif ch == 2:
        calcPercent()
    elif ch == 3:
        createReport()
    elif ch == 4:
        sendReport()
    elif ch == 5:
        print("-"*14,"!BYE!","-"*14)
        cursor.close()
        students_db.close()
        break
    else:
        print("-"*8,"Invalid choice :(, please choose again","-"*8)