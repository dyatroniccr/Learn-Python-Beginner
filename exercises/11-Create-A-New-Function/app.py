import random

# your code here
def generate_random():
    number = random.randint(0, 9)
    print("Random number between 0 and 9 is % s" % (number))
    return number

generate_random()

