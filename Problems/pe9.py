from libs.primelib import Prime
import time
import math

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def main():
    print('script started ...')
    start = time.clock()
    answer = 0
    for a in range(1, 334):
        for b in range(a + 1, 500):
            c = math.sqrt(a**2 + b**2)
            if a + b + c == 1000:
                answer = a * b * c
                break
        if answer != 0:
            break
    end = time.clock()
    print('answer: ' + str(int(answer)))
    print('time: ' + str(end - start))


if __name__ == '__main__':
    main()
