class Mamal:
    def walk(self):
        print("walk")

class Dog(Mamal):
    def bark(self):
        print("Bark")

class Cat(Mamal):
    def meow(self):
        print("Meow")

newDog = Dog()
newCat = Cat()

newDog.walk()
newDog.bark()

newCat.walk()
newCat.meow()
