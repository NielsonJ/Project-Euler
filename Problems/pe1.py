import time
from libs.timetablelib import TimesTable

# Question:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

LIMIT = 1000


def methode1():
    # Attempt one, the shitty one
    print('script started ...')
    start = time.clock()
    three = TimesTable(3)
    five = TimesTable(5)
    three.findMultiplicatives(LIMIT)
    five.findMultiplicatives(LIMIT)
    five.excludeMultiplicatives(3)
    total = sum(three.multiplicatives) + sum(five.multiplicatives)
    end = time.clock()
    print('answer: ' + str(total))
    print('time: ' + str(end - start))


def methode2():
    # Attempt two, yes baby.
    print('script started ...')
    total = 0
    start = time.clock()
    for x in range(0, LIMIT):
        if x % 3 == 0 or x % 5 == 0:
            total = total + x
    end = time.clock()
    print('answer: ' + str(total))
    print('time: ' + str(end - start))


if __name__ == '__main__':
    methode1()
    print()
    methode2()
