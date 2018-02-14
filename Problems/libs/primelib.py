# if __name__ == "__main__":
#     print("This is a library module, do not run as script.")

class Prime:
    def __init__(self):
        self.primeList = [2]

    def get_prime_by_index(self, n):
        self.primeList.append(n)
        return -1

    def get_prime_list(self):
        return self.primeList

    def add_prime(self, n):
        self.primeList.append(n)
