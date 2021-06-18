   # Mini-Project 2
import json



def newAccount():
    with open("records.txt", "r") as file:
        try:
            file = open("records.txt", "r")
            records = json.load(file)
        except json.decoder.JSONDecodeError:
            records = []
    file.close()
    acc = input("Eter the account number: ")
    while acc in records:
        print("An acount already exists for the account number {} and its owner is: {}".format(acc, records[acc]["Name"]))
        print("Choose a different account number")
        acc = input("Enter the account number: ")
    keys = ["Name", "Age", "Address", "Phone", "Amount"]
    values = []
    name = input("Enter your name: ")
    values.append(name)
    age = input("Enter your age: ")
    values.append(age)
    address = input("Enter your address: ")
    values.append(address)
    phone = input("Enter your phone number: ")
    values.append(phone)
    amount = int(input("Enter the inital amount you want to deposit: "))
    values.append(amount)

    records[acc] = dict(zip(keys, values))
    
    file = open("records.txt", "w")
    json.dump(records, file, indent=4)
    file.close()
    print("----New account created----")

def existingCust():
    acc = input("Eter the account number: ")

    file = open("records.txt", "r")
    records = json.load(file)
    file.close()
    if not acc in records:
        print("Data not found for the account number: %s"%acc)
        return 

    print("Data found!")
    while True:
        print("1. Check Balance\n2. Withdrwal\n3. Deposit\n4. Main Menu")
        ch2 = int(input("Enter your choice: "))
        if ch2==1:
            print("Current balance for accout number %s is %i"%(acc, records[acc]["Amount"]))
        elif ch2==2:
            amt = int(input("Enter the maount you want to withdraw: "))
            if records[acc]["Amount"]>=amt:
                records[acc]["Amount"] = records[acc]["Amount"] - amt
                print("You have withdrawn %i money and the current balance is %i for account number %s"%(amt, records[acc]["Amount"], acc))
            else:
                print("Insufficient funds for account number %s!!\n Your current balance is %i"%(acc, records[acc]["Amount"]))
        elif ch2==3:
            amt = int(input("Enter the amount you want to deposit: "))
            records[acc]["Amount"] = records[acc]["Amount"] + amt
            print("Current balance for accout number %s is %i"%(acc, records[acc]["Amount"]))
        else:
            break 
    file = open("records.txt", "w")
    json.dump(records, file, indent=4)
    file.close()
    

while True:
    print("1. Open a New Account\n2. Existing Customer\n3. Exit")
    ch1 = int(input("Enter your choice: "))
    if ch1==1:
        newAccount()
    elif ch1==2:
        existingCust()
    elif ch1==3:
        break
    else: 
        print("Invalid ch1, select again! :(")
