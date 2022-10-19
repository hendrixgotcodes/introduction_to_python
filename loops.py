# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ["John", "Paul", "Sara", "Susan"]

for person in people:
    if person == "Sara":
        break
    print(f"Current person: {person}")

for person in people:
    if person == "Sara":
        continue
    print(f"Current person: {person}")

#range
for i in range(20):
    print(i)

# While loops execute a set of statements as long as a condition is true.
