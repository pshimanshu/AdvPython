import string
import random

# alpha = string.ascii_letters
# print(type(alpha), alpha)

# lowercase = string.ascii_lowercase
# print(type(lowercase), lowercase)
# uppercase = string.ascii_uppercase
# print(type(uppercase), uppercase)

# digs = string.digits
# print(type(digs), digs)

# puncs = string.punctuation
# print(type(puncs), puncs)

    # Example OTP or Product KEY
for i in range(16):
    print(random.choice(string.digits+string.ascii_letters+string.punctuation), end='')