###########################
##      Simple Game     ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--##
###########################


# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!


import random


def random_num():
    """
    generate list with 3 str items, each items is a random number
    """
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    return digits[:3]


def win_condition(list_result, input_str):
    """
    input_str: user input str of 3 digits number
    list_result: list with 3 str items, each items is a random number

    True if every position of input_str match with list_result
    """
    match = True

    for i in range(len(list_result)):
        if list_result[i] != input_str[i]:
            match = False

    return match


def nope(list_result, input_str):
    """
    input_str: user input str of 3 digits number
    list_result: list with 3 str items, each items is a random number

    True if none of position of input_str match with list_result
    """
    nope = True

    for digit in input_str:
        if digit in list_result:
            nope = False

    return nope


def close(list_result, input_str):
    """
    input_str: user input str of 3 digits number
    list_result: list with 3 str items, each items is a random number

    True if atleast 1 of position of input_str is in list_result
    """
    close = False

    if nope(list_result, input_str):
        return False
    else:
        for i in range(len(list_result)):
            if input_str[i] != list_result[i]:
                close = True

    return close


def match(list_result, input_str):
    """
    input_str: user input str of 3 digits number
    list_result: list with 3 str items, each items is a random number

    True if atleast 1 of position of input_str match in list_result of the same position
    """
    match = False

    if nope(list_result, input_str):
        return False
    else:
        for i in range(len(list_result)):
            if input_str[i] == list_result[i]:
                match = True

    return match


def play_guessing():
    """
    play game function.
    Generate random number, you have to guess that number to break the loop
    """
    result = random_num()
    print(result)

    while True:
        guess = input("What is your guess? ")

        if match(result, guess):
            print("Match")

        elif close(result, guess):
            print("Close")

        elif nope(result, guess):
            print("Nope")

        if win_condition(result, guess):
            print("You Win!")
            break


play_guessing()
