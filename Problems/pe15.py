import time
import math

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
    answer = function(20)
    end = time.perf_counter()
    print('answer: ' + str(answer))
    print('time: ' + str(end - start))


def function(gridsize):
    gridsize += 1  # add one to gridsize to represent each node.
    oldgrid = [1]
    for x in range(0, gridsize):
        newgrid = [1]
        for y in range(0, x):
            if ((y + 1) == x):
                newgrid.append(newgrid[y] * 2)
            else:
                newgrid.append(newgrid[y] + oldgrid[y + 1])
        # print(newgrid)
        oldgrid = newgrid
    return oldgrid[-1]  # return last element in oldgrid's list.


if __name__ == '__main__':
    main()