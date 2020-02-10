"""Computes sqaures in a cardinal discrete coordinate system.

0 - 0 - 0
|   |   |
0 - 0 - 0
|   |
0 - 0

this should have 5 squares

"""
def how_many_squares(coordinates):
    count = dict()
    answer = 0
    for coord_above in coordinates:
        for coord_below in coordinates:
            if coord_above[1] == coord_below[1] and coord_above[0] < coord_below[0]:
                # this is an vertical line
                # save the vertical line as a pair of integer resprenting the top and bot height
                pair = (coord_above[0], coord_below[0])
                if pair not in count:
                    # if dosnt excist yet, add
                    count[pair] = 0
                else:
                    # else increase pair counter and add squares to result
                    count[pair] += 1
                    answer += count[pair]
    return answer


if __name__ == "__main__":
    coordinates = [
        (0, 0),
        (1, 0),
        (0, 1),
        (1, 1),
        (0, 2),
        (1, 2),
        # (2, 0),
        # (2, 1),
        # (2, 2),
        (0, 3),
        (1, 3),
        (0, 4),
        (1, 4)
    ]
    print(how_many_squares(coordinates))