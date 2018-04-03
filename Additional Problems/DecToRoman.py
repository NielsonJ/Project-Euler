def main():
    print("\nDecimal to Roman numeral converter")
    numbers = input("Number to convert: ")
    numerals = {
        0 : "I", # 1
        1 : "V", # 5
        2 : "X", # 10
        3 : "L", # 50
        4 : "C", # 100
        5 : "D", # 500
        6 : "M"  # 1000
    }
    answer = ""
    numeralpointer = 0
    for number in reversed(numbers):
        if int(number) < 4:
            answer = (int(number) * numerals[numeralpointer]) + answer
        elif int(number) == 4:
            answer = numerals[numeralpointer] + numerals[numeralpointer + 1] + answer
        elif int(number) > 4 and int(number) < 9:
            answer = numerals[numeralpointer + 1] + (int(number) - 5) * numerals[numeralpointer] + answer
        elif int(number) == 9:
            answer = numerals[numeralpointer] + numerals[numeralpointer + 2] + answer
        else:
            print("something went wrong")
        numeralpointer += 2
    print(answer)

if __name__ == '__main__':
    main()