# Import dog class
from dog import Dog

# Create a servicedog class inherited from "Dog"
class ServiceDog(Dog):
    # ServiceDog constructor
    def __init__(self, name, age, weight, handler):
        # Dog constructor
        Dog.__init__(self, name, age, weight)
        # Define servicedog attributes
        self.handler = handler
        self.is_working = False # Define attribute (not necessary it needs to mirror the parameter)

    # Walk
    def walk(self):
        print(f"{self.name} is helping its handler {self.handler} walk")

    # Bark
    def bark(self):
        # Override bark method
        if self.is_working:
            print(f"{self.name} says I can't bark I'm working")
        else: 
            # Call dog bark method
            Dog.bark(self)

# Create frisbee class
class Frisbee:
    # Constructor and define attributes
    def __init__(self, color):
        self.color = color

    # Object itself as string
    def __str__(self):
        return f"I'm a {self.color} frisbee"

# Create frisbeedog inherited with dog
class FrisbeeDog(Dog):
    # FrisbeeDog constructor
    def __init__(self, name, age, weight):
        # Dog constructor
        Dog.__init__(self, name, age, weight)
        # Define other attributes
        self.frisbee = None

    # Bark
    def bark(self):
        # If the dog has a frisbee
        if self.frisbee != None:
            print(f"{self.name} says I can't bark, I have a frisbee in my mouth")
        else:
            Dog.bark(self)

    # Catch
    def catch(self, frisbee):
        self.frisbee = frisbee
        print(f"{self.name} caught a {frisbee.color} frisbee")

    def give(self):
        # If the dog has a frisbee
        if self.frisbee != None:
            # Temp frisbee
            frisbee = self.frisbee
            # Set frisbee to none
            self.frisbee = None
            # Gibve back
            print(f"{self.name} gives back {frisbee.color} frisbee")
            return frisbee
        else:
            print(f"{self.name} doesn't have a frisbee")
            return None

    # Object as string
    def __str__(self):
        str = f"I'm a dog named {self.name}"
        # If it has a frisbee
        if self.frisbee != None:
            str = f"{str} and I have a frisbee"
        return str

# Hotel object
class Hotel:
    def __init__(self, name):
        self.name = name
        # Dictionary
        self.kennel = {}

    # Check in only dogs
    def check_in(self, dog):
        if isinstance(dog, Dog):
            self.kennel[dog.name] = dog
            print(f"{dog.name} is checked into {self.name}")
        else:
            print(f"Sorry only Dogs are allowed in {self.name}")

    # Check out dogs already checked in
    def check_out(self, name):
        if name in self.kennel:
            dog = self.kennel[name]
            print(f"{dog.name} is checked out of {self.name}")
            del self.kennel[dog.name]
            return dog
        else:
            print(f"Sorry {name} is not boarding at {self.name}")
            return 
            
# Cat object
class Cat():
    def __init__(self, name):
        self.name = name

    def meow(self):
        print(f"{self.name} says Meow")

# Testing :)
def test_code():
    codie = Dog("Codie", 12, 38)
    jackson = Dog("Jackson", 9, 12)
    sparky = Dog("Sparky", 2, 14)
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