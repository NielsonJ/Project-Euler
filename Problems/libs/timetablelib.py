'''
class to handle time tables
'''


class TimesTable:
    def __init__(self, number):
        self.number = number
        self.multiplicatives = []

    def findMultiplicatives(self, limit):
        for x in range(1, limit):
            if (x * self.number) >= limit:
                break
            self.multiplicatives.append(x * self.number)
        return self.multiplicatives

    def excludeMultiplicatives(self, number):
        for x in self.multiplicatives:
            if x % number == 0:
                self.multiplicatives.remove(x)
        pass