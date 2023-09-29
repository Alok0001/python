#base class
class Animal:
    def __init__(self,name):
        self.name = name;

    def speak(self):
        pass

#derived class
class Dog(Animal):
    def speak(self):
        return "woof!"

class Cat(Animal):
    def speak(self):
        return "meow"

# creating object
dog = Dog("Buddy")
cat = Cat("kity")

print(f"{dog.name} says: {dog.speak()} ")
print(f"{cat.name} says: {cat.speak()} ")
