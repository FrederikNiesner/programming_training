# Practicing Object Oriented Programming

class Person(object):
    def __init__(self, age, height, mass) -> None:
        """a class describing persons and some of there (metric) characterisitcs

        Args:
            age (int): person's age in age
            height (_type_): person's heigth in meters
            mass (_type_): person's weight in kg
        """
        self.age = age
        self.height = height
        self.mass = mass
    
    def calculate_BMI(self):
        bmi = self.mass / (self.height ** self.height)
        return bmi

me = Person(30, 1.84, 74)

print(me.height)
print(me.age)
print("Answer: The BMI = ", me.calculate_BMI())
