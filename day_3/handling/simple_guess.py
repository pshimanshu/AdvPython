# User defined exceptions - raise
    # Example 4
import random

class SmallError(Exception):
    pass
class LargeError(Exception):
    pass

number = 72

while True:
    guess = int(input("Guess the number: "))
    try:
        if guess<number:
            raise SmallError
        elif guess>number:
            raise LargeError
        else:
            break
    except SmallError:
        print("Your guess is too small\nPlease guess a larger number")
    except LargeError:
        print("Your gues is too large\nPlease guess a smaller number")
    



print("Congratulations!!! You have won the game")
