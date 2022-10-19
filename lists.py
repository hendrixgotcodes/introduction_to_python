# A List is a collection which is ordered and changeable. Allows duplicate members.
numbers = [1,2,3,4,5,6,7,8,9]

#use constractor
numbers2 = list((1,2,3,4,5,6,7,8,9))

fruits = ["oranges", "apples", "banana"]

print(numbers, numbers2)

print(len(fruits))

fruits.append("mangoes")
print(fruits)

fruits.remove("oranges")
print(fruits)

fruits.insert(3,"strawberries")
print(fruits)

fruits.pop(2)
print(fruits)

fruits.reverse()
print(fruits)

fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)