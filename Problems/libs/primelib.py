# if __name__ == "__main__":
#     print("This is a library module, do not run as script.")

class Prime:
    def __init__(self):
        self.__primeList = [2]

    def getByIndex(self, n):
        number = self.__primeList[-1]
        while n > len(self.__primeList) - 1:
            number += 1
            primeConfirmed = True
            for prime in self.__primeList:
                if number % prime == 0:
                    primeConfirmed = False
                    break
            if primeConfirmed == True:
                self.__primeList.append(number)
        return self.__primeList[n]

    def getCalcedList(self):
        return self.__primeList

    def getFirst(self, number):
        if number > len(self.__primeList):
            self.getByIndex(number - 1)
        return self.__primeList[:number]

if __name__ == '__main__':
    print('This is a class library for prime handling')
    print('Writen by Nielson Janné')