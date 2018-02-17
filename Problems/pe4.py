import time

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

LIMIT = [100, 999]


def main():
    start = time.clock()
    answer = 0
    data = []
    # Check all multiplications from 999 to 100 (3 digits)
    for x in range(LIMIT[0], LIMIT[1]):
        for y in range(LIMIT[0], LIMIT[1]):
            multiplication = x * y
            if checkPalindrome(multiplication):
                if multiplication > answer:
                    answer = multiplication
                    data = [x, y]
    end = time.clock()
    print(
        'answer: ' + str(answer) + ' = ' + str(data[0]) + ' x ' + str(data[1]))
    print('time: ' + str(end - start))


def checkPalindrome(number):
    # Convert to string, reverse, compare.
    if str(number) == str(number)[::-1]:
        return True
    else:
        return False


if __name__ == '__main__':
    main()