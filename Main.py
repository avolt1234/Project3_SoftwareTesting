from random import randint

def Main(debug):

    scoreCard = {'Aces': 'Empty',
                 'Twos': 'Empty',
                 'Threes': 'Empty',
                 'Fours': 'Empty',
                 'Fives': 'Empty',
                 'Sixes': 'Empty',
                 'Total Score': 0,
                 'Bonus': 0,
                 'Total': 0,
                 '3-of-a-Kind': 'Empty',
                 '4-of-a-Kind': 'Empty',
                 'Full-House': 'Empty',
                 'Small-Straight': 'Empty',
                 'Large-Straight': 'Empty',
                 'Yahtzee': 'Empty',
                 'Chance': 'Empty',
                 'Yahtzee Bonus': 0,
                 'Total of lower section': 0,
                 'Total of upper section': 0,
                 'Grand Total': 0
                 }
    if debug.capitalize() == 'T':
        test1 = {1: ['Aces', [1, 2, 3, 4, 5]],
                 2: ['3-of-a-Kind', [2, 3, 2, 4, 2]],
                 3: ['3-of-a-Kind', [4, 2, 6, 4, 4]],
                 4: ['Fours', [4, 2, 6, 4, 4]],
                 5: ['Yahtzee', [6, 6, 6, 6, 6]],
                 6: ['Full-House', [3, 5, 5, 3, 3]],
                 7: ['Fives', [5, 2, 3, 5, 5]],
                 8: ['Chance', [4, 4, 5, 5, 2]],
                 9: ['Twos', [2, 2, 2, 3, 4]],
                 10: ['Fours', [4, 2, 1, 3, 4]],
                 11: ['Small-Straight', [4, 2, 1, 3, 4]],
                 12: ['4-of-a-Kind', [3, 3, 3, 3, 3]],
                 13: ['Large-Straight', [6, 4, 3, 2, 5]],
                 14: ['Sixes', [6, 4, 6, 2, 1]],
                 15: ['Threes', [3, 3, 3, 3, 3]]
                 }

        test2 = {1: ['3-of-a-Kind', [1, 2, 1, 1, 5]],
                 2: ['Twos', [2, 2, 4, 5, 2]],
                 3: ['Small-Straight', [1, 5, 3, 2, 4]],
                 4: ['Full-House', [2, 2, 3, 3, 2]],
                 5: ['Aces', [1, 3, 1, 1, 1]],
                 6: ['Chance', [1, 3, 1, 2, 2]],
                 7: ['Fives', [5, 5, 4, 5, 2]],
                 8: ['4-of-a-Kind', [6, 6, 6, 5, 6]],
                 9: ['Fours', [4, 4, 4, 1, 4]],
                 10: ['Yahtzee', [6, 6, 6, 6, 6]],
                 11: ['Threes', [3, 3, 3, 3, 3]],
                 12: ['Large-Straight', [5, 1, 3, 4, 2]],
                 13: ['Sixes', [6, 4, 3, 6, 5]],
                 }

        tests = [test1, test2]
        #TODO create dictionary to parse through
        for test in tests:
            scoreCard1 = scoreCard.copy()
            for i in range(len(test)):
                scoreCard1 = changeScoreCard(scoreCard1, test[i + 1][0], test[i + 1][1])
                printScorecard(scoreCard1)

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
        if scoreCard[slot] == 'Empty' or slot == 'Yahtzee Bonus':
            return True
        else:
            return False
    except KeyError:
        return False


def changeScoreCard(scoreCard, slot, rolls):

    isVal = validator(scoreCard, slot)

    if isVal:
        if len(set(rolls)) == 1 and scoreCard['Yahtzee'] != 'Empty':
            scoreCard['Yahtzee Bonus'] = scoreCard['Yahtzee Bonus'] + 100

        #Checkers
        if slot == '3-of-a-Kind':
            newScore = score3OAK(rolls)
            scoreCard['3-of-a-Kind'] = newScore
        elif slot == '4-of-a-Kind':
            newScore = score4OAK(rolls)
            scoreCard['4-of-a-Kind'] = newScore
        elif slot == 'Full-House':
            newScore = scoreFullHouse(rolls)
            scoreCard['Full-House'] = newScore
        elif slot == 'Small-Straight':
            newScore = scoreSmallStraight(rolls)
            scoreCard['Small-Straight'] = newScore
        elif slot == 'Large-Straight':
            newScore = scoreLargeStraight(rolls)
            scoreCard['Large-Straight'] = newScore
        elif slot == 'Yahtzee':
            newScore = scoreYahtzee(rolls)
            scoreCard['Yahtzee'] = newScore
        elif slot == 'Chance':
            scoreCard['Chance'] = sum(rolls)
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
        scoreCard['Total of lower section'] = lowTotal(scoreCard)
        scoreCard['Total of upper section'] = scoreCard['Total']

        scoreCard['Grand Total'] = scoreCard['Total of lower section'] + scoreCard['Total of upper section']

        return scoreCard
    else:
        print('\n\nThe slot {0} is already used, please select another one'.format(slot))
        return scoreCard

def lowTotal(scoreCard):
    total = 0
    if scoreCard['3-of-a-Kind'] != 'Empty':
        total += scoreCard['3-of-a-Kind']
    if scoreCard['4-of-a-Kind'] != 'Empty':
        total += scoreCard['4-of-a-Kind']
    if scoreCard['Full-House'] != 'Empty':
        total += scoreCard['Full-House']
    if scoreCard['Small-Straight'] != 'Empty':
        total += scoreCard['Small-Straight']
    if scoreCard['Large-Straight'] != 'Empty':
        total += scoreCard['Large-Straight']
    if scoreCard['Yahtzee'] != 'Empty':
        total += scoreCard['Yahtzee']
    if scoreCard['Chance'] != 'Empty':
        total += scoreCard['Chance']
    if scoreCard['Yahtzee Bonus'] != 'Empty':
        total += scoreCard['Yahtzee Bonus']

    return total

def printScorecard(scoreCard):
    print()
    for key, value in scoreCard.items():
        print(str(key) + '\t' + str(value))

def score3OAK(roll):

    valid = False

    for num in roll:
        if roll.count(num) >= 3:
            valid = True

    score = 0
    if valid:
        for num in roll:
            score += int(num)
        return score
    else:
        return 0

def score4OAK(roll):
    valid = False

    for num in roll:
        if roll.count(num) >= 4:
            valid = True

    score = 0
    if valid:
        for num in roll:
            score += int(num)
        return score
    else:
        return 0

def scoreFullHouse(roll):

    setroll = set(roll)

    valid = False

    if len(setroll) == 2:
        for num in setroll:
            if roll.count(num) == 2 or roll.count(num) == 3:
                valid = True
            else:
                valid = False
    if valid:
        return 25
    return 0

def scoreSmallStraight(roll):

    roll = sorted(roll)
    first = roll[0] + 1
    second = roll[1] + 1

    #check if first num rolled is part of the small straight

    firstCheck = True

    for num in range(1, len(roll) - 1):
        if first != int(roll[num]):
            firstCheck = False
        first += 1

    secondCheck = True

    for num in range(2, len(roll)):
        if second != int(roll[num]):
            secondCheck = False
        second += 1

    if firstCheck or secondCheck:
        return 30
    else:
        return 0

def scoreLargeStraight(roll):
    roll2 = sorted(roll)
    if roll2[0] == 1 and roll2[4] == 5 and len(set(roll2)) == 5:
        return 40
    elif roll2[0] == 2 and roll2[4] == 6 and len(set(roll2)) == 5:
        return 40
    else:
        return 0

def scoreYahtzee(roll):
    if len(set(roll)) == 1:
        return 50
    else:
        return False

if __name__  == '__main__':
    debug = input("Enter T to test program: ")
    Main(debug)