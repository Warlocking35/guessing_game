import random


def get_integer(prompt):
    """
    Get an integer from Standard input (stdin).

    The function will continue looping, and prompting
    the user, until a valid `int` is entered.

    :param prompt: The String the user will see, when
    they're prompted to enter the value.
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        elif temp.isalpha():
            print("'{0}' is not a number".format(temp))


highest = 1000
answer = random.randint(1, highest)
guess = 0  # initialise to any number that doesn't equal the answer
# I did this code to just mess around with making a random number
# Instead of a fixed one on answer
print("Please guess number between 1 and {}: ".format(highest))


while guess != answer:
    guess = get_integer(": ")

    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess == 0:
            print("GoodBye")
            break
        if guess < answer:
            print("Please guess higher")
        else:   # guess must be greater than answer
            print("Please guess lower")
