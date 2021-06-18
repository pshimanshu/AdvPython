    # Mini-Project 1

names = []
mobs = []
addrs = []

def addData():
    name = input("Enter the new name: ")
    while not name.isalpha():
        print("Invalid name, please try again")
        name = input("Enter the new name: ")
    while name in names:
        print("Data already exists for %s\nAdd data for new person"%name)
        name = input("Enter the new name: ")
    mob = input("Enter the new mobile number: ")
    while not mob.isnum():
        print("Invalid phone number, please try again")
        mob = input("Enter the new mobile number: ")
    addr = input("Enter the new address")

    names.append(name)
    mobs.append(mob)
    addrs.append(addr)
    print("-"*5,"Data Added Succesfully", "-"*3)

def showData():
    name = input("Whose data do want to retreive? ")
    while not name.isalpha():
        print("Invalid name, please try again")
        name = input("Enter the new name: ")
    if name in names:
        id = names.index(name)
        print("Name: ",names[id])
        print("Phone: ",mobs[id])
        print("Address: ",addrs[id])
    else:
        print("Data not found for %s"%name)
    print("-"*30)

def delData():
    name = input("Whose data do want to delete? ")
    while not name.isalpha():
        print("Invalid name, please try again")
        name = input("Enter the new name: ")
    if name in names:
        id = names.index(name)
        names.pop(id)
        mobs.pop(id)
        addrs.pop(id)
    else:
        print("Data not found for {}".format(name))

while True:
    print("1. Add Data\n2. Show Data\n3. Delete Dat\n4.Exit")
    choice = int(input("Enter your choice: "))

    if choice==1:
        addData()
    elif choice==2:
        showData()
    elif choice==3:
        delData()
    elif choice==4:
        print("Process Done!!")
        break
    else:
        print("Invalid choice, RESELECT!!!")
