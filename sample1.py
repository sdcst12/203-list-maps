def isEven(i):
    if type(i) != int:
        return False
    if i % 2 == 0:
        return True
    else:
        return False
    
data = [76, 56, 20, 77, 57, 96, 24, 83, 16, 39, 25, 0, 86, 64, 65, 25, 15, 99, 77, 79, 31, 95, 25, 13, 9, 84, 42, 38, 9, 42]
even = map(isEven, data)
print(list(even))
print(list(even))  # This will print an empty list since the iterator is exhausted
    