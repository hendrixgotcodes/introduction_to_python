# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods
name = "Samuel"
age = 23

print("Hello my name is " + name)

# String Formatting

# Arguments by position
print("My name is {name} and I am {age} years old".format(name=name, age=age))

# F-Strings
print(f"Hello my name is {name} and I am {age}")

# String Methods
S = "hEllo world"

# capitalize 
print(S.swapcase())
print(S.capitalize())
print(S.upper())
print(S.lower())

print(S.replace("world", "everyone"))