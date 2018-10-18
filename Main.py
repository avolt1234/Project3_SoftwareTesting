from random import randint

def Main():

    scoreCard = {'Aces': 'Empty', 'Twos': 'Empty', 'Threes': 'Empty', 'Fours': 'Empty', 'Fives': 'Empty',
                 'Sixes': 'Empty'}

    while True:
        rollD = input("\nPress Y to roll dice, press Q to quit: ")
        if rollD.upper() == 'Y':
            dice = rollDice()

        breaker = True
        while breaker:
            slot = input("Which slot did you want to use? ").title()
            valid = validator(scoreCard, slot)
            if valid:
                breaker = False
            else:
                print("The " + slot + " slot is already in use")

        scoreCard = changeScoreCard(scoreCard, slot, dice)
        printScorecard(scoreCard)

    return

def MainDebug(scoreCard, diceRolls):

    printScorecard(scoreCard)

    print("\nDice roll is " + str(diceRolls))

    breaker = True
    while breaker:
        slot = input("Which slot did you want to use? ").title()
        valid = validator(scoreCard, slot)
        if valid:
            breaker = False
        else:
            print("The " + slot + " slot is already in use")

    scoreCard = changeScoreCard(scoreCard, slot, diceRolls)
    printScorecard(scoreCard)

def rollDice():

    # Rolls 5 dice and returns a list of the dice rolls
    rollList = []
    for i in range(5):
        rollList.append(randint(1, 6))

    print(rollList)
    return rollList



def validator(scoreCard, slot):
    '''
    :param scoreCard: the Scorecard
    :param slot: the slot where you want to input the score
    :return: True or False
    '''
    try:
        if scoreCard[slot.title()] == 'Empty':
            return True
        else:
            return False
    except KeyError:
        return False


def changeScoreCard(scoreCard, slot, rolls):

    whichOne = {'Aces' : 1, 'Twos' : 2, 'Threes' : 3, 'Fours' : 4, 'Fives' : 5, 'Sixes' : 6}

    mySlot = whichOne[slot]

    holder = 0

    for roll in rolls:
        if roll == mySlot:
            holder += roll

    scoreCard[slot] = holder

    return scoreCard

def printScorecard(scoreCard):
    print()
    for key, value in scoreCard.items():
        print(str(key) + '\t' + str(value))

if __name__  == '__main__':
    debug = input("Enter debug to test program: ")

    if debug.title() == 'Debug':

        scoreCard = {'Aces': 'Empty', 'Twos': 'Empty', 'Threes': 'Empty', 'Fours': 'Empty', 'Fives': 'Empty',
                     'Sixes': 'Empty'}

        whichSlot = input("Enter the slot: ")
        slotValue = input("Enter the value, leave blank if empty: ")

        if slotValue:
            scoreCard[whichSlot] = slotValue

        roller = input("Enter 5 dice rolls, each separated by a comma (1, 2, 3, 4, 5): ")

        diceRoll = [1, 2, 3, 4, 5]

        finalRoll = []

        for char in roller:
            if char != ',' and char != ' ':
                finalRoll.append(int(char))
        if finalRoll:
            diceRoll = finalRoll
        MainDebug(scoreCard, diceRoll)
    else:
        Main()