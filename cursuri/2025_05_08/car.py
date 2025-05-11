class Car:
    acceleration = 10
    def __init__(self, registration_number):
        self.registration_number = registration_number
        self.in_motion = False
        self.speed = 0

    def __str__(self):
        return f'Car with plate {self.registration_number}'

    def drive(self):
        self.in_motion = True

    def accelerate(self):
        self.speed += Car.acceleration

    def stop(self):
        self.in_motion = False
        self.speed = 0


my_old_honda = Car('WGT6914')
print(my_old_honda)
print(str(my_old_honda))

my_old_honda.drive()
my_old_honda.accelerate()

print(my_old_honda.speed)