import time


def main():
    print('script started ...')
    start = time.perf_counter()
    answer = function(1)
    end = time.perf_counter()
    print('answer: ' + str(answer))
    print('time: ' + str(end - start))


def function(power):

    return 0


if __name__ == '__main__':
    main()