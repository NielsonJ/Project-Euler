from libs.primelib import Prime
import time

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

LIMIT = 2000000


def main():
    print('script started ...')
    start = time.clock()
    prime = Prime()
    index = 0
    answer = 0
    while prime.getByIndex(index) < LIMIT:
        answer += prime.getByIndex(index)
        index += 1
    end = time.clock()
    print('answer: ' + str(answer))
    print('time: ' + str(end - start))


if __name__ == '__main__':
    main()