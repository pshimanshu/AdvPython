import json

f = open("file.txt", "w")
dict1 = {101: {"name":"sam", "salary":30000}, 102: {"name":"john", "salary":35000}}
json.dump(dict1, f, indent=4)
f.close()

f2 = open("file.txt", "r")
dat = json.load(f2)
print(dat)
f2.close()