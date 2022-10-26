numbers = [1,3,10,5,4]

def findLargest():
    largest = 0
    for number in  numbers:
        if number > largest:
            largest = number
    return largest

print(findLargest())
