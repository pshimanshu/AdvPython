import csv
import matplotlib.pyplot as plt

def addData():
    f = open("corono.csv", "a", newline="")
    obj = csv.writer(f)
    list1 = []
    list1.append(input("Enter country name: "))
    list1.append(input("Enter total positive cases: "))
    list1.append(input("Enter recovered cases: "))
    list1.append(input("Enter total deaths: "))

    obj.writerow(list1)
    f.close()
    print("Data added successfully for country %s"%list1[0])

def showData():
    f = open("corono.csv")
    data = list(csv.reader(f))
    f.close()

    for country_data in data:
        print(country_data)
    print("-"*30)
    
def plotData():
    f = open("corono.csv")
    data = list(csv.reader(f))
    
    country_name = []
    positive_cases = []
    recovered_cases = []
    num_deaths = []

    for cntry in data:
        country_name.append(cntry[0])
        positive_cases.append(int(cntry[1]))
        recovered_cases.append(int(cntry[2]))
        num_deaths.append(int(cntry[3]))

    plt.title("CORONA DATABASE")
    plt.xlabel("Country Name")
    while True:
        print("1. Positive Cases\n2. Recovered Cases\n3. Number of Deaths\n4. Exit")
        ch = int(input("Enter for which dat you want to plot the data: "))
        if ch==1:
            plt.plot(country_name, positive_cases)
            plt.ylabel("Number of Positive Cases")
            plt.show()
        elif ch==2:
            plt.plot(country_name, recovered_cases, "-.", linewidth=8)
            plt.ylabel("Number of Recovered Cases")
            plt.show()
        elif ch==3: 
            plt.bar(country_name, num_deaths)
            plt.ylabel("Number of Deaths")
            plt.show()
        else:
            break 
    

while True:
    print("1. Add Data\n2. Show Data\n3. Plot Data\n4. Exit")
    choice = int(input("Enter your choice: ")) 
    if choice==1:
        addData()
    elif choice==2:
        showData()
    elif choice==3:
        plotData()
    elif choice==4:
        break
    else:
        print("Invlaid choice\n Please select again.")