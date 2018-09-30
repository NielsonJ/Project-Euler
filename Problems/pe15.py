import time
import math

# +-+-+-+
# +-+-+-+
# +-+-+-+
# +-+-+-+


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
    return oldgrid[-1]


if __name__ == '__main__':
    main()