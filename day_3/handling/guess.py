
import random

class SmallError(Exception):
    pass
class LargeError(Exception):
    pass

def game():
    players = int(input("Enter the number of players: "))
    names = []
    for player in range(players):
        names.append(input("Enter player%i name: "%(player+1)))
    start = int(input("Enter start point: "))
    stop = int(input("Enter stop point: "))
    print("Picking a random number in between %i and %i"%(start, stop))
    number = random.randint(start, stop)
    print("  **  "*4, "DONE!!")

    attempts = 1
    lucky_player = random.randint(0,len(names)-1)
    name = names[lucky_player]
    print("Hey !! %s"%name)
    guess = int(input("Guess the number-->"))
    while True:
        lucky_player = random.randint(0,len(names)-1)
        name = names[lucky_player]
        print("Hey !! %s"%(name))
        try:
            if guess<number:
                raise SmallError
            elif guess>number:
                raise LargeError
            else:
                break
        except SmallError:
            print("The previous guess is too SMALL!! Please guess a larger number-->")
        except LargeError:
            print("The previous guess is too LARGE!! Please guess a smaller number-->")       
        guess = int(input())
        attempts+=1
    print("Congratulation %s, you have won the game"%name)
    print("The total number of attempts is:",attempts)

while True:
    print("-"*10,"GUESS THE NUMBER","-"*10)
    print("1. Press '1' to START the game\n2. Press '2' to EXIT")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        game()
    elif ch == 2:
        break
    else:
        print("Invalid choice :(, select again")