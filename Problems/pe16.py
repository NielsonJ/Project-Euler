import time


def main():
    print('script started ...')
    start = time.perf_counter()
    answer = function(1000)
    end = time.perf_counter()
    print('answer: ' + str(answer))
    print('time: ' + str(end - start))


def function(power):
    digits = str(2**power)
    sum = 0
    for x in digits:
        sum += int(x)
    return sum


if __name__ == '__main__':
    main()