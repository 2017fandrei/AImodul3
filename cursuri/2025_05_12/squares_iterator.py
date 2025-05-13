import math

class MyIterator:
    def __init__(self, limit):
        self.limit = limit
        self.index = 0
        self.number = -1

    def __iter__(self):
        self.index = 0
        self.number = -1
        return self

    def __next__(self):
        if self.index < self.limit:
            self.number += 1
            square = math.sqrt(self.number)
            while square!=int(square):
                self.number += 1
                square = math.sqrt(self.number)
            self.index += 1
            return self.number
        else:
            raise StopIteration

iter_ = MyIterator(10)
for i in iter_:
    print(i)