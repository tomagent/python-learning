from dog import print_dog
from dog import Dog

class ServiceDog(Dog):
    def __init__(self, name, age, weight, handler):
        Dog.__init__(self, name, age, weight)
        self.handler = handler

    def walk(self):
        print(f"{self.name} is helping its handler {self.handler} walk")

if __name__ == "__main__":
    rody = ServiceDog("Rody", 8, 38, "Joseph")
    print(f"This dog's name is {rody.name}")
    print(f"This dog's handler is {rody.handler}")
    print_dog(rody)
    rody.bark()
    rody.walk()