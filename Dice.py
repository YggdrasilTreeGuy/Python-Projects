import random
#class Dice():
    #def __init__(self):
        #pass
counter = 0
def rollthedice(x):
    if x == "4":
        return random.randrange(1,5)
    elif x == "6":
        return random.randrange(1,7)
    elif x == "8":
        return random.randrange(1,9)
    elif x == "10":
        return random.randrange(1,11)
    elif x == "20":
        return random.randrange(1,21)
    elif x == "100":
        return random.randrange(1,101)


def diceselection():
    dice = ["4", "6", "8", "10", "20", "100"]
    dicechoice = input("Which dice would you like to roll? {dice}".format(dice=dice))

    if dicechoice in dice:
        return dicechoice

def numbertoroll():
    num = input("Please select a number of dice to roll 1 - 20. ")
    if num == ' ' or num == '':
        num = numbertoroll()

    if int(num) < 1:
        print("You must roll at least one. ")
        num = numbertoroll()
    return num

while True:
    yeses = ["Yes", "Y", "y", "yes"]
    nos = ["No", "n", "N", "no"]
    new = diceselection()

    if new == None:
        counter += 1
        print("Please select a dice.")
        if counter == 6:
            break
        else:
            continue

    amount = numbertoroll()



    if int(amount) > 20:
        print("You may only roll a maximum of 20 at a time.")
        amount = "20"

    for i in range(int(amount)):
        roll = rollthedice(new)
        if roll == None:
            print("There is no dice to roll.")
        else:
            print(roll)

    delay = input("Would you like to try again? Y/N ")

    if delay in yeses:
        pass
    elif delay in nos:
        break
    elif delay == None:
        continue
    else:
        delay = input("I'm sorry, I didn't quite get that, did you want to try again? Y/N ")
        continue
