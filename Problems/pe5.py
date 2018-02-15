from libs.primelib import Prime
import time

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def main():
    print('script started ...')
    start = time.clock()
    prime = Prime()
    index = 2
    number = 1
    while index < 21:
        tryNumber = number
        primeIndex = 0
        while tryNumber % index!= 0:
            tryNumber = number * prime.getByIndex(primeIndex)
            primeIndex += 1
        number = tryNumber
        index += 1
    end = time.clock()
    print('answer: ' + str(number))
    print('time: ' + str(end - start))    

def oldInefficient():
    print('script started ...')
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
    print()
    oldInefficient()