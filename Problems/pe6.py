from libs.primelib import Prime
import time

# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

LIMIT = 100


def main():
    print('script started ...')
    start = time.clock()
    sumOfSquares = 0
    squaresOfSum = 0
    for x in range(1, LIMIT + 1):
        sumOfSquares += x**2
        squaresOfSum += x
    squaresOfSum = squaresOfSum**2
    answer = squaresOfSum - sumOfSquares
    end = time.clock()
    print('answer: ' + str(answer))
    print('time: ' + str(end - start))


if __name__ == '__main__':
    main()