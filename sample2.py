def isEven(i):
    if type(i) != int:
        return False
    if i % 2 == 0:
        return True
    else:
        return False
    
data = [76, 56, 20, 77, 42]
even = map(isEven, data)
saved = list(even)
print(saved)
print(saved)