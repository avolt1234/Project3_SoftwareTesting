from random import randint

def Main():
    dice = rollDice()
    return

def rollDice():
    rollList = []
    for i in range(5):
        rollList.append(randint(1,6))


    return rollList


if __name__  == '__main__':
    Main()