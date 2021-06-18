# regexp project
# Supermarket database management

# 1. extract data -> regex
# 2. put it in a csv file
# 3. plot  a graph

import re
import csv

txt = open("june1.txt").read()

patp = "Product:\s+(\w+)"
products = re.findall(patp, txt)

patq = "Quantity:\s+(\d+)"
quantities = [int(x) for x in re.findall(patq, txt)]

patcp = "CP:\s+(\d+)"
cps = [int(x) for x in re.findall(patcp, txt)]

patsp = "SP:\s(\d+)"
sps = [int(x) for x in re.findall(patsp, txt)]

data = [[products[i],quantities[i],cps[i],sps[i]] for i in range(len(products))]
total = 0
for i in range(len(data)):
    pf = (data[i][3]-data[i][2])*data[i][1]
    total+=pf
    data[i].append(pf)

f = open("supermarket.csv", "w", newline="")
obj = csv.writer(f)
headers = ["Product", "Quantity", "Cost_Price", "Selling_Price", "Profit"]
obj.writerow(headers)
obj.writerows(data)
obj.writerow(["","","","Total profit",total])
f.close()
print("-"*8,"Report generated successfully", "-"*8)

