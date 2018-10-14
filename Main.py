from random import randint

def Main():
    dice = rollDice()
    return

def rollDice():

    # Rolls 5 dice and returns a list of the dice rolls
    rollList = []
    for i in range(5):
        rollList.append(randint(1,6))
    return rollList


if __name__  == '__main__':
    Main()