import math


def square_generator(limit):
    index = 0
    number = -1
    while index < limit:
        number += 1
        square = math.sqrt(number)
        while square != int(square):
            number += 1
            square = math.sqrt(number)
        index += 1
        yield number



# Usage
gen = square_generator(50)
for elem in gen:
    print(elem)

#     def __next__(self):
#         if index < self.limit:
#             self.number += 1
#             square = math.sqrt(self.number)
#             while square!=int(square):
#                 self.number += 1
#                 square = math.sqrt(self.number)
#             self.index += 1
#             return self.number
#         else:
#             raise StopIteration
#
# iter_ = MyIterator(10)
# for i in iter_:
#     print(i)
