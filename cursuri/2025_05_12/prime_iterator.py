import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):# alt+enter deschide sugestiile pentru repararea erorilor
        if n % i == 0:
            return False
    return True

class PrimeIterator:
    def __init__(self, n):
        self.n = n
        self.generated_numbers = 0
        self.number = 1


    def __iter__(self):
        self.number = 1
        return self

    def __next__(self):
        self.number += 1
        if self.generated_numbers >= self.n:
            raise StopIteration
        elif is_prime(self.number):
            self.generated_numbers += 1
            return self.number
        return self.__next__()

# Usage
iter_ = PrimeIterator(3)
# print(next(iter_))
# print(next(iter_))
# print(next(iter_))
# print(next(iter_))
# print(next(iter_))
# print(next(iter_))

for elem in iter_:
    print(elem)
# for elem in iter_:
#     print(elem)

# a_list = [n for n in iter_]
#
# a_list = []
# for n in iter_:
#     a_list.append(n)
