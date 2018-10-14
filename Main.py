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

        scoreCard = changeScoreCard(scoreCard, slot, dice)
        printScorecard(scoreCard)

    return

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

    for key, value in scoreCard.items():
        print(str(key) + '\t' + str(value))



if __name__  == '__main__':
    Main()