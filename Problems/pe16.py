import time

# Each node is accesable by the sum of the previous nodes.
# Example of ways to each node :

# 1 - 1 - 1  - 1
# 1 - 2 - 3  - 4
# 1 - 3 - 6  - 10
# 1 - 4 - 10 - 20

# The outcome is symmetrical over the diagonal line, calculating one side is sufficient


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