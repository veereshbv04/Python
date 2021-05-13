class vehicle:
    def general_usage(self):
        print("general usage: used for commuting")

class Car(vehicle):
    def __init__(self):
        print("I am car here")
        self.wheel=4
        self.roof=True

    def specific_usage(self):
        print("specific use is ,used for vaction with families")
        self.general_usage()


class Motorbike(vehicle):
    def __init__(self):
        print(" I am motorbike here")
        self.wheel=2
        self.roof=False
    def specific_usage(self):
        print("Specific usage is,used for road trip and racing")
        self.general_usage()



car =Car()
car.specific_usage()
print(car.wheel)

motor=Motorbike()
motor.specific_usage()

