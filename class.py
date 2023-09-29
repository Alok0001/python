class Person:
    def __init__(self,name,age): #constructor
        self.name = name
        self.age = age

    def greet(self):
            print(f"hello, my name is {self.name} and im {self.age} years old.")

# creating an object
person1 = Person("alice",25)
person2 = Person("Bob",30)

#calling menthods
person1.greet()
person2.greet()
