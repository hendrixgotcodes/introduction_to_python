# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries
person = {
    "first_name": "Kwaku",
    "last_name": "Yeboah",
    "age": 34
}

person2 =dict(first_name="Sarah", last_name= "unknown")

print(person)
print(person2)

#Get dict keys
print(person.keys())

person2 = person.copy()
print(len(person2))

#List of dictionaries
people = [
    person2,
    person,
]

print(people)