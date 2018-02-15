from libs.primelib import Prime
import time

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def main():
    # Philosophy: Why would you let your PC crunch numbers if you can think for yourself.
    # The smallest positve number that is evenly divisivle a range of numbers ...
    # is a multiplication of all its prime numbers 
    print('script started ...')
    start = time.clock()
    prime = Prime()
    index = 2
    number = 1
    while index <= 20:
        # loop from 2 to 20 with index (1 is redudent)
        tryNumber = number
        primeIndex = 0
        while tryNumber % index!= 0:
            # Check if number is divisible by the current index with a natural result
            # loop through prime's to see which lowest prime will result in a division with a natural result
            tryNumber = number * prime.getByIndex(primeIndex)
            primeIndex += 1
        # Set number to a succesfull find of multiplication of new lowest prime that makes a natural division
        number = tryNumber
        index += 1
    end = time.clock()
    print('answer: ' + str(number))
    print('time: ' + str(end - start))    

def oldInefficient():
    # Philosophy: Why think if your PC can just crunch numbers.
    print('script started ...')
    start = time.clock()
    number = 0
    evenlyDivisible = False
    while evenlyDivisible == False:
        number += 1
        for x in range(1,21):
            # Check number if it can be devided for all the numbers from 1 to 20 with a natural result
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