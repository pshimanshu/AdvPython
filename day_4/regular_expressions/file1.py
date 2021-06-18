    # Regular Expressions
import re

# search()-> returns only first match and findall()-> returns a list of all matching patterns
    # example 1
# match = re.search("hello", "hello world")
# print(match.group()) 

    # example 2
# pat = "hello"
# txt = open("data1.txt", "r").read()
# match = re.search(pat, txt)
# if match:
#     print("Match found:", match.group())
# else:
#     print("Match not found")

# pat = "hello"
# txt = open("data1.txt", "r").read()
# matches = re.findall(pat, txt)
# print(matches)
# #print(type(matches))

'''
    #data2.txt
pat = "\d\d"
pat = "\d+"
txt = open("data2.txt", "r").read()
matches = re.findall(pat, txt)
print(matches)
#print(type(matches))
'''


'''
# data3.txt
#pat = "\d\d\d-\d\d\d-\d\d\d\d"
#pat = "\d{3}-\d{3}-\d{4}"
pat = "\d{3}[-\s*]\d{3}[-\s*]\d{3}"
txt = open("data3.txt", "r").read()
matches = re.findall(pat, txt)
print(matches)
'''


# regular expressionssss
'''
\d -> digits -> 0-9
\D -> not digits -> anything but a digit

\s -> spaces
\S -> not spaces -> anything but spaces

\w -> a-z or A-Z or 0-9

[a-zA-Z] -> only alphabets

. (dot) -> anything
+ (plus) -> one or more
* (star) -> zero or more
? (question mark) -> zero or one

{range} -> {2,7}
[aeiou] -> all elements written 

'''


    # data4.txt
# pat = "\d+\s[a-zA-Z]+"
# txt = open("data4.txt", "r").read()
# matches = re.findall(pat, txt)
# print(matches)


    # data5.txt
#pat = "\.+@[a-zA-Z]+\.[a-z]+"
pat = "\S+@\S+"
txt = open("data5.txt", "r").read()
matches = re.findall(pat, txt)
print(matches)
