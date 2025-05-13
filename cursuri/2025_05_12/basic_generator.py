def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4

# Usage
for item in my_generator():
    print(item)