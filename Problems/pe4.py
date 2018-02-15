import time

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def main():
    start = time.clock()
    answer = 0
    data = []
    for x in range(100,999):
        for y in range(100,999):
            multiplication = x * y
            if checkPalindrome(multiplication):
                if multiplication > answer:
                    answer = multiplication
                    data = [x, y]
    end = time.clock()
    print('answer: ' + str(answer) + ' = ' + str(data[0]) + ' x ' + str(data[1]))
    print('time: ' + str(end - start))

def checkPalindrome(number):
    if str(number) == str(number)[::1]:
        return True
    else:
        return False

if __name__ == '__main__':
    main()