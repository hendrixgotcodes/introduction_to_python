# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces


#Create function
def sayHello(name):
    print(f"hello {name}")


def getSum(num1:int, num2:int):
    total = num1 + num2
    return total

sayHello("Samuel")
print(getSum(2,))

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

