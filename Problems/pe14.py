import time


def main():
    print('script started ...')
    start = time.clock()

    answer = (1, 1)
    collatzDict = {1: 1}  # don't recalc
    for startNumber in range(1, 1000000):
        NumberToCalc = startNumber
        chain = 0
        while NumberToCalc not in collatzDict:
            chain += 1
            if NumberToCalc % 2 == 0:
                NumberToCalc = NumberToCalc / 2
            else:
                NumberToCalc = 3 * NumberToCalc + 1
        collatzDict[startNumber] = collatzDict[NumberToCalc] + chain
        print("[ " + str(startNumber) + " ] chain: " +
              str(collatzDict[startNumber]))
        if answer[1] < collatzDict[startNumber]:
            answer = (startNumber, collatzDict[startNumber])

    end = time.clock()
    print('answer: ' + str(answer))
    print('time: ' + str(end - start))


if __name__ == '__main__':
    main()
