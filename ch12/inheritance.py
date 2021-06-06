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

if __name__ == "__main__":
    rody = ServiceDog("Rody", 8, 38, "Joseph")
    print(f"This dog's named is {rody.name}")
    print(f"This dog's handler is {rody.handler}")
    print(rody)
    rody.bark()
    rody.is_working = True
    rody.bark()
    rody.walk()
