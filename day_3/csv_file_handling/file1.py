#     # CSV File Handling: Comma Seperated Values
import csv

# # Reading data from csv files 
# f = open("source.csv", "r")
# data = list(csv.reader(f))
# print(data)
# print("-----NAMES-----\n", *data[0])

# for person in data:
#     print(person[0])
# print("-----PHONES-----")
# for person in data:
#     print(person[1])
# print("-----PLACES-----")
# for person in data:
#     print(person[2])
# f.close()

    # Writing data into csv files
f = open("source.csv", "w", newline="")
obj = csv.writer(f)

obj.writerow(["sam", "sam@email.com"])
obj.writerow(["john", "john@email.com"])
f.close()