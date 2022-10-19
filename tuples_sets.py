# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
fruits = ("Apples", 4, "Watermelon", 2.33)

print(type(fruits))
print(fruits[1])

fruits_set = {"Apples", "Oranges", "Mangoes"}

print("Apples" in fruits_set)

fruits_set.add("Grapes")
print(fruits_set)

fruits_set.remove("Grapes")
print(fruits_set)

fruits_set.clear()
print(fruits_set)
# A Set is a collection which is unordered and unindexed. No duplicate members.
