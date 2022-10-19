# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

class User:
    # Constructor
    def  __init__(self, name:str, age:int, email:str):
        self.name = name
        self.email = email
        self.age = age
    
    def greeting(self):
        return f"I am {self.name} and {self.age} years old"

    def has_birthday(self):
        return self.age


samuel = User("samuel", 23, "asare@gmail.com")


print(type(samuel))
print(samuel.greeting())
print(samuel.has_birthday())



class Customer(User):
    def  __init__(self, name:str, age:int, email:str):
        self.name = name
        self.email = email
        self.age = age
        self.balance: 0
    
    def set_ballance(self, balance:float):
        self.balance = balance

    def greeting(self):
        return f"I am {self.name} and {self.age} years old. My balance is {self.balance}"



louis = Customer("Kwaku louis", 23, "louis@xitroo.com")

louis.set_ballance(500)

print(louis.greeting())
print(louis.has_birthday())

