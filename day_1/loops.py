
    #Example 1
# size = int(input("Enter number of elements: "))
# nums = []
# for i in range(size):
#     num = int(input("Enter element: "))
#     nums.append(num)
# print("Second largest element is: %i"%(sorted(nums)[-2]))

#     # Example 2    
# size = int(input("Enter number of elements: "))
# evens, odds = [], []
# for i in range(size):
#     num = int(input("Enter element: "))
#     if num%2==0:
#         evens.append(num)
#     else:
#         odds.append(num)
# print("Even list: ", evens)
# print("Odd list: ", odds)

    # Example 4
# low = int(input("Enter the lower range: "))
# up = int(input("Enter the higher range: "))
# lst = []
# for num in range(low, up+1):
#     lst.append((num, num*num))
# print(lst)


    # Example 5
# list1 = [10,20,30,40]
# list2 = [11,22,33,44]

# list3 = []
# for i in range(len(list1)):
#     list3.append(list1[i]*list2[i])
# print(list3)

    # Example 6
# names = ['manjunath', 'akanksha', 'suresh', 'uday']
# vowel_names = []
# for name in names:
#     if name[0] in "aeiouAEIOU":
#         vowel_names.append(name)
# print(vowel_names)

    # Example 7
# for file in files:
#     ext = file[-3:]
#     if ext=="txt":
#         texts.append(file)
#     elif ext=="pdf":
#         pdfs.append(file)
#     else:
#         jpgs.append(file)

# files = ["abc.txt", "pqr.pdf", "xyz.jpg"]
# texts, pdfs, jpgs = [], [], []
# for file in files:
#     if file.startswith(".txt"):
#         texts.append(file)
#     elif file.startswith(".pdf"):
#         pdfs.append(file)
#     else:
#         jpgs.append(file)
# print(texts) 
# print(pdfs)
# print(jpgs)

    # Example 8
lst = [10,20,30,10,40,30,40,50,70,20,10]
new = []
for name in lst:
    if not name in new:
        new.append(name)
print(new)
print(*sorted(list(set(lst))))