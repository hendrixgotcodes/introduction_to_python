# numbers = [1,3,10,5,4]

# def findLargest():
#     largest = 0
#     for number in  numbers:
#         if number > largest:
#             largest = number
#     return largest

# print(findLargest())

# listMethods


# numbers = [1,2,3,4,5,6,7,8,9]
# numbers.append(20)
# numbers.insert(4, 15)
# numbers.remove(3)
# numbers.pop()

# print(numbers)
# print(numbers.index(15))
# print(6 in numbers)

# numbers.append(12)
# numbers.insert(4, 12)
# print(numbers.count(12))

# numbers.sort()
# print(numbers)

# numbers.reverse()
# print(numbers)

# newNumbers = numbers.copy()
# print(newNumbers)


numbers = [1,2,3,4,5,6,1,5,2,4,1,3]
duplicates = []

for number in numbers:
    if(not number in duplicates):
        duplicates.append(number)

print(duplicates)