from libs.primelib import Prime
import cProfile
import time

# Test variable's
primeindex = 100010
primecheck = 1299841

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

    print('test 3:')
    start = time.clock()
    value = prime.checkIfPrime(primecheck)
    end = time.clock()
    print('value: ' + str(value))
    print('time: ' + str(end - start))
    print()

    print('test 4:')
    start = time.clock()
    value = prime.checkIfPrime(1299841)
    end = time.clock()
    print('value: ' + str(value))
    print('time: ' + str(end - start))
    print()

if __name__ == '__main__':
    main()
