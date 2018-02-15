from libs.primelib import Prime
import time

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?

def main():
    print('script started ...')
    start = time.clock()
    prime = Prime()
    # In primelib the first prime starts at index 0 (2)
    answer = prime.getByIndex(10001 - 1)
    end = time.clock()
    print('answer: ' + str(answer))
    print('time: ' + str(end - start))    

if __name__ == '__main__':
    main()