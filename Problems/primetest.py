from libs.primelib import Prime
import cProfile
import time

# Test variable's
primeindex = 100000
primecheck = 1000000000000


def main():
    prime = Prime()
    print('test 1:')
    start = time.clock()
    value = prime.getByIndex(primeindex)
    end = time.clock()
    print('value: ' + str(value))
    print('time: ' + str(end - start))
    print()

    print('test 2:')
    start = time.clock()
    value = prime.getByIndex(primeindex)
    end = time.clock()
    print('value: ' + str(value))
    print('time: ' + str(end - start))
    print()

    prime1 = Prime()
    prime2 = Prime()

    print('test 4:')
    start = time.clock()
    value = prime1.checkIfPrime(primecheck)
    end = time.clock()
    print('value: ' + str(value))
    print('time: ' + str(end - start))
    print()

    print('test 5:')
    start = time.clock()
    value = prime1.checkIfPrime(primecheck)
    end = time.clock()
    print('value: ' + str(value))
    print('time: ' + str(end - start))
    print()

    print('test 6:')
    start = time.clock()
    value = prime2.checkIfPrime(primecheck)
    end = time.clock()
    print('value: ' + str(value))
    print('time: ' + str(end - start))
    print()

    print('test 7:')
    start = time.clock()
    value = prime2.checkIfPrime(primecheck)
    end = time.clock()
    print('value: ' + str(value))
    print('time: ' + str(end - start))
    print()


if __name__ == '__main__':
    main()
