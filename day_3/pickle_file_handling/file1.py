    # Pickle files
'''
Pickle denotes the process of converting a python object heirarchy into a byte string and 
unpickling converts byte stream back to an object heirarchy
'''
import pickle
# dump() and load()

f = open("data.pkl", "wb")   #wb -> write binary
data = ("1","2,3,4", '223', 23,31, "3ie")
pickle.dump(data, f)
f.close()

# reading form pickle file
f = open("data.pkl", "rb")
var = pickle.load(f)
print(type(var))
print(var)
f.close()