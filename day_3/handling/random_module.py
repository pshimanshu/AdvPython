# Random module
import random

#1. random() - prints a float between 0 and 1
# print("%0.4f"%(random.random()))

#2. uniform() - specify a lower and an upper limit, returns a float
# print("%0.4f"%(random.uniform(4,789)))

#3. randint() - specify a lower and an upper limit, returns an int
# print("%i"%(random.randint(100,12293)))

#4. sample() - returns an array with values in given range and given size without duplicates
# print(*random.sample(range(1,11),6))

#5. shuffle()
list1 = ["club", "diamond", "spade", "heart"]
random.shuffle(list1)
print(list1)

#6. choice() - to select 1 element randomly
var = random.choice(list1)
print(var)

print(random.sample(list1,3))