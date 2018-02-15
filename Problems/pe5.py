from libs.primelib import Prime
import time

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def main():
    start = time.clock()
    number = 0
    evenlyDivisible = False
    while evenlyDivisible == False:
        number += 1
        for x in range(1,21):
            evenlyDivisible = True
            if number % x != 0:
                evenlyDivisible = False
                break
    end = time.clock()
    print('answer: ' + str(number))
    print('time: ' + str(end - start))

if __name__ == '__main__':
    main()
