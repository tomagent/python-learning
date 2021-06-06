class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        if self.weight > 29:
            print(self.name, 'says "WOOF WOOF"')
        else:
            print(self.name, 'says "woof woof"')

    def human_years(self):
        human_age = self.age * 7
        return human_age

    def __str__(self):
        return f"I'm a dog name {self.name}"

if __name__ == "__main__":
    codie = Dog("Codie", 12, 38)
    jackson = Dog("Jackson", 9, 12)
    print(f"{jackson.name}'s age in human years is {jackson.human_years()}") # String interpolation
    print(f"{codie.name}'s age in human years is {codie.human_years()}")