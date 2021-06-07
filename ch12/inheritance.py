from dog import Dog

class ServiceDog(Dog):
    def __init__(self, name, age, weight, handler):
        Dog.__init__(self, name, age, weight)
        self.handler = handler
        self.is_working = False # Define attribute (not necessary mirror the parameter)

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


def test_code():
    dude = FrisbeeDog("Dude", 5, 20)
    blue_frisbee = Frisbee("blue")

    print(dude)
    dude.bark()
    dude.catch(blue_frisbee)
    dude.bark()
    print(dude)
    frisbee = dude.give()
    print(frisbee)
    print(dude)

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
