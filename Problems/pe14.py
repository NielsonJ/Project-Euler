import time


def main():
    print('script started ...')
    start = time.clock()

    answer = getAnswer()

    end = time.clock()
    print('answer: ' + str(answer))
    print('time: ' + str(end - start))


def getAnswer():
    answer = 0
    answer_chain = 0
    for a in range(1, 1000000):
        n = a
        chain = 1
        while n != 1:
            if n % 2 == 0:
                n = n / 2
            else:
                n = 3 * n + 1
            chain += 1
        if chain > answer_chain:
            answer = a
            answer_chain = chain
        print("[ " + str(a) + " ]  answer: " + str(answer) +
              "\t answer-chain: " + str(answer_chain))
    return answer


if __name__ == '__main__':
    main()
