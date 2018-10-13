import time

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

words = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    101: "hundredand",
    1000: "thousand"
}


def main():
    print('script started ...')
    start = time.perf_counter()
    answer = function(1, 1000)
    end = time.perf_counter()
    print('answer: ' + str(answer))
    print('time: ' + str(end - start))


def function(lowerlimit, upperlimit):
    sum = 0
    for number in range(lowerlimit, upperlimit + 1):
        hecta = int(number / 100)
        deca = int((number % 100) / 10)
        ones = int(number % 10)
        wordstring = ""
        print("number:            " + str(hecta) + str(deca) + str(ones))
        if hecta < 1:
            if number < 21:
                wordstring += words[deca * 10 + ones]
            else:
                wordstring += words[deca * 10] + words[ones]
        if hecta >= 1 and hecta <= 9:
            if deca == 0 and ones == 0:
                wordstring += words[hecta] + words[100]
            else:
                wordstring += words[hecta] + words[101]
            if (deca * 10 + ones) < 21:
                wordstring += words[deca * 10 + ones]
            else:
                wordstring += words[deca * 10] + words[ones]
        if hecta > 9:
            wordstring += words[1] + words[1000]
        print("in letters:        " + wordstring)
        print("number of letters: " + str(len(wordstring)))
        sum += len(wordstring)
        print()
    return sum


if __name__ == '__main__':
    main()