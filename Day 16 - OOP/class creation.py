class Dog:
    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots

    def bark(self):
        print(f'WOOF! My name is {self.name}')

    