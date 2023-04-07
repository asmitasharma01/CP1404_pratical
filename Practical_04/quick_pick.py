import random

MINIMUM = 1
MAXIMUM = 45
NUMBERS_PER_LINE = 6
NUMBER_OF_LINES = int(input("How many quick picks? "))

for i in range(NUMBER_OF_LINES):
    numbers = []
    while len(numbers) < NUMBERS_PER_LINE:
        number = random.randint(MINIMUM, MAXIMUM)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()
    print(" ".join("{:2}".format(number) for number in numbers))
