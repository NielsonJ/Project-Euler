def main():
    square = int(input("Calculate square root of: "))
    print("square root of " + str(square) + " is " +
          str(binsquareroot(square)))


def binsquareroot(square):
    if square < 1:
        return "an imaginair number"
    if square == 1:
        return 1
    left = 1
    right = square
    mid = right
    while (left + 1 < right):
        mid = int(left + (right - left) / 2)
        root = mid * mid
        if root == square:
            return mid
        elif root > square:
            right = mid
        else:  # root < square
            left = mid
    return "not a flat root"


if __name__ == '__main__':
    main()
