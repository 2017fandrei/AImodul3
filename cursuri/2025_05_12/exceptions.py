class NegativeNumberException(Exception):
    pass

class NotANumberException(Exception):
    pass

def check_positive_number(a):
    if a < 0:
        raise NegativeNumberException

def check_number(a):
    try:
        return int(a)
    except ValueError:
        raise NotANumberException

a = input('Please input a positive number:')
while True:
    try:
        a = check_number(a)
        check_positive_number(a)
        break
    except NegativeNumberException:
        print("This number is negative")
        a = input('Please input a positive number:')
    except NotANumberException:
        print('This is not a number')
        a = input('Please input a positive number:')
print(f'Found positive number {a}')