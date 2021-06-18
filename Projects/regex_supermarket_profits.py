import re
import csv
import os
import matplotlib.pyplot as plt


def createReport(fname):
    txt = open(fname+".txt").read()

    patp = "Product:\s+(\w+)"
    products = re.findall(patp, txt)
    patq = "Quantity:\s+(\d+)"
    quantities = [int(x) for x in re.findall(patq, txt)]
    patcp = "CP:\s+(\d+)"
    cps = [int(x) for x in re.findall(patcp, txt)]
    patsp = "SP:\s(\d+)"
    sps = [int(x) for x in re.findall(patsp, txt)]

    data = [[products[i],quantities[i],cps[i],sps[i]] for i in range(len(products))]
    total_pf = 0
    for i in range(len(data)):
        pf = (data[i][3]-data[i][2])*data[i][1]
        total_pf+=pf
        data[i].append(pf)


    f = open(fname+".csv", "w", newline="")
    obj = csv.writer(f)
    obj.writerow(["","",fname,"",""])
    headers = ["Product", "Quantity", "Cost_Price", "Selling_Price", "Profit"]
    obj.writerow(headers)
    obj.writerows(data)
    obj.writerow(["","","","Total profit",total_pf])
    f.close()
    print("-"*8,"Report generated successfully for", fname, "-"*8)
    return total_pf

path = "D:\\1.Suresh\\Personal\\Himu\\Oracle Trainings\\Adv Python\\day_4\\regular_expressions\\regex_project"
txt_files = [file[:-4] for file in os.listdir(path) if file.endswith(".txt")]
profits = []
for fname in txt_files:
    pf = createReport(fname)
    profits.append(pf)
#print(profits)

plt.title("Weekly Profit Comparision")
plt.xlabel("Dates")
plt.ylabel("Daiily Profit")
plt.bar(txt_files, profits)
plt.show()