from libs.primelib import Prime
import time

# Question?
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

NUMBER = 600851475143

def main():
    print('script started ...')
    start = time.clock()
    number = NUMBER
    prime = Prime()
    primeIndex = 0
    while number != 1:
        while number % prime.getByIndex(primeIndex) == 0:
            number = number / prime.getByIndex(primeIndex)
            if number == 1:
                highestPrime = prime.getByIndex(primeIndex)
                break
        primeIndex += 1
    end = time.clock()
    print('asnwer: ' + str(highestPrime))
    print('time: ' + str(end - start))
    
if __name__ == '__main__':
    main()
