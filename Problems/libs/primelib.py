import math

class Prime:
    def __init__(self):
        self.__primeList = [2]

    def getByIndex(self, n):
        number = self.__primeList[-1]
        while n > len(self.__primeList) - 1:
            number += 1
            # primeConfirmed = True
            # for prime in self.__primeList:
            #     if number % prime == 0:
            #         primeConfirmed = False
            #         break
            #     if prime > math.sqrt(number):
            #         break 
            # if primeConfirmed == True:
            if self.checkIfPrime(number) == True:
                self.__primeList.append(number)
        return self.__primeList[n]

    def checkIfPrime(self, number):
        while number > self.__primeList[-1]**2:
            self.getByIndex(len(self.__primeList))
        primeConfirmed = True
        for prime in self.__primeList:
            if number % prime == 0:
                primeConfirmed = False
                break
            if prime > math.sqrt(number):
                break
        return primeConfirmed

    def getCalcedList(self):
        return self.__primeList

    def getFirst(self, number):
        if number > len(self.__primeList):
            self.getByIndex(number - 1)
        return self.__primeList[:number]

if __name__ == '__main__':
    print('This is a class library for prime handling')
    print('Writen by Nielson Janné')