    # Example 1
# WAF to count total words in your text file.
def wordCount():
    f = open("source.txt", "r")
    str1 = f.read()
    f.close()

    print("Total number of words is: ", len(str1.split()))
#wordCount()

def countVowels():
    f = open("source.txt", "r")
    str1 = f.read()
    f.close()
    count = 0
    for let in str1:
        if let in "aeiouAEIOU":
            count+=1
    print("The total number of letters is %i"%count)
#countVowels()

def lineCount():
    f = open("source.txt", "r")
    str1 = f.readlines()
    f.close()
    print("The total number of lines is: {}".format(len(str1)))
#lineCount()

def upperNewFile():
    f = open("source.txt", "r")
    str1 = f.read()
    f.close()
    f = open("upper.txt", "w")
    f.write(str1.upper())
    f.close()
#upperNewFile()