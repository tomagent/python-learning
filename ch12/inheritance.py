from dog import Dog

class ServiceDog(Dog):
    def __init__(self, name, age, weight, handler):
        Dog.__init__(self, name, age, weight)
        self.handler = handler
        self.is_working = False # Define attribute (not necessary it needs to mirror the parameter)

    def walk(self):
        print(f"{self.name} is helping its handler {self.handler} walk")

    def bark(self):
        if self.is_working:
            print(f"{self.name} says I can't bark I'm working")
        else: 
            Dog.bark(self)

class Frisbee:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return f"I'm a {self.color} frisbee"

class FrisbeeDog(Dog):
    def __init__(self, name, age, weight):
        Dog.__init__(self, name, age, weight)
        self.frisbee = None

    def bark(self):
        if self.frisbee != None:
            print(f"{self.name} says I can't bark, I have a frisbee in my mouth")
        else:
            Dog.bark(self)

    def catch(self, frisbee):
        self.frisbee = frisbee
        print(f"{self.name} caught a {frisbee.color} frisbee")

    def give(self):
        if self.frisbee != None:
            frisbee = self.frisbee
            self.frisbee = None
            print(f"{self.name} gives back {frisbee.color} frisbee")
            return frisbee
        else:
            print(f"{self.name} doesn't have a frisbee")
            return None

    def __str__(self):
        str = f"I'm a dog named {self.name}"
        if self.frisbee != None:
            str = f"{str} and I have a frisbee"
        return str

class Hotel:
    def __init__(self, name):
        self.name = name
        self.kennel_names = []
        self.kennel_dogs = []

    def check_in(self, dog):
        if isinstance(dog, Dog):
            self.kennel_names.append(dog.name)
            self.kennel_dogs.append(dog)
            print(f"{dog.name} is checked into {self.name}")
        else:
            print(f"Sorry only Dogs are allowed in {self.name}")

    def check_out(self, name):
        for i in range(0, len(self.kennel_names)):
            if name == self.kennel_names[i]:
                dog = self.kennel_dogs[i]
                del self.kennel_names[i]
                del self.kennel_dogs[i]
                print(f"{dog.name} is checked out of {self.name}")
                return dog
        print(f"Sorry {name} is not boarding at {self.name}")
        return None

class Cat():
    def __init__(self, name):
        self.name = name

    def meow(self):
        print(f"{self.name} says Meow")

def test_code():
    codie = Dog("Codie", 12, 38)
    jackson = Dog("Jackson", 9, 12)
    sparky = Dog("Sparly", 2, 14)
    rody = ServiceDog("Rody", 8, 38, "Joseph")
    dude = FrisbeeDog("Dude", 5, 20)
    kitty = Cat("Kitty")

    hotel = Hotel("Doggie Hotel")
    hotel.check_in(codie)
    hotel.check_in(jackson)
    hotel.check_in(rody)
    hotel.check_in(dude)
    hotel.check_in(kitty)

    dog = hotel.check_out(codie.name)
    print(f"Checked out {dog.name} who is {dog.age} and {dog.weight} lbs")
    dog = hotel.check_out(jackson.name)
    print(f"Checked out {dog.name} who is {dog.age} and {dog.weight} lbs")
    dog = hotel.check_out(rody.name)
    print(f"Checked out {dog.name} who is {dog.age} and {dog.weight} lbs")
    dog = hotel.check_out(dude.name)
    print(f"Checked out {dog.name} who is {dog.age} and {dog.weight} lbs")
    dog = hotel.check_out(sparky.name)

if __name__ == "__main__":
    test_code()
    # rody = ServiceDog("Rody", 8, 38, "Joseph")
    # print(f"This dog's named is {rody.name}")
    # print(f"This dog's handler is {rody.handler}")
    # print(rody)
    # rody.bark()
    # rody.is_working = True
    # rody.bark()
    # rody.walk()
