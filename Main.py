from random import randint

def Main(debug):

    scoreCard = {'Aces': 'Empty',
                 'Twos': 'Empty',
                 'Threes': 'Empty',
                 'Fours': 'Empty',
                 'Fives': 'Empty',
                 'Sixes': 'Empty',
                 '3-of-a-Kind': 'Empty',
                 '4-of-a-Kind': 'Empty',
                 'Total Score': 0,
                 'Bonus': 0,
                 'Total': 0,
                 'Full House': 'Empty',
                 'Small Straight': 'Empty',
                 'Large Straight': 'Empty',
                 'Yahtzee': 'Empty',
                 'Chance': 'Empty',
                 'Yahtzee Bonus': 0,
                 'Total of lower section': 0,
                 'Total of upper section': 0,
                 'Grand Total': 0
                 }
    if debug.capitalize() == 'T':
        #TODO create dictionary to parse through
        scoreCard = changeScoreCard(scoreCard, '3-of-a-Kind', [3, 5, 5, 2, 5])
        scoreCard = changeScoreCard(scoreCard, '4-of-a-Kind', [3, 5, 5, 5, 5])
        printScorecard(scoreCard)
    else:
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
        elif slot == 'Yahtzee Bonus' and scoreCard['Yahtzee Bonus'] < 300:
            return True
        else:
            return False
    except KeyError:
        return False


def changeScoreCard(scoreCard, slot, rolls):

    if slot == '3-of-a-Kind':
        newScore = score3OAK(rolls)
        scoreCard['3-of-a-Kind'] = newScore
    elif slot == '4-of-a-Kind':
        newScore = score4OAK(rolls)
        scoreCard['4-of-a-Kind'] = newScore
    elif slot == 'Full House':
        newScore = scoreFullHouse(rolls)
        scoreCard['Full House'] = newScore
    else:
        whichOne = {'Aces' : 1, 'Twos' : 2, 'Threes' : 3, 'Fours' : 4, 'Fives' : 5, 'Sixes' : 6}
        mySlot = whichOne[slot]
        holder = 0
        for roll in rolls:
            if roll == mySlot:
                holder += roll
        scoreCard[slot] = holder
    totalScore = 0

    counter = 0

    for score in scoreCard.values():
        if score != 'Empty' and counter < 6:
            totalScore += int(score)
        counter += 1

    scoreCard['Total Score'] = totalScore
    if totalScore >= 63:
        scoreCard['Bonus'] = 35

    scoreCard['Total'] = scoreCard['Bonus'] + totalScore

    return scoreCard

def printScorecard(scoreCard):
    print()
    for key, value in scoreCard.items():
        print(str(key) + '\t' + str(value))

def score3OAK(roll):

    valid = False

    for num in roll:
        if roll.count(num) == 3:
            valid = True

    score = 0
    if valid:
        for num in roll:
            score += int(num)
        return score
    else:
        return False

def score4OAK(roll):
    valid = False

    for num in roll:
        if roll.count(num) == 4:
            valid = True

    score = 0
    if valid:
        for num in roll:
            score += int(num)
        return score
    else:
        return False

def scoreFullHouse(roll):

    setroll = set(roll)




if __name__  == '__main__':
    debug = input("Enter T to test program: ")
    Main(debug)