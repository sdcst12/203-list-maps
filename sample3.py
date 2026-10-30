import time, random


def f(i):
    # this is used by the listmap
    return i**2

print("This is going to take a few seconds...")

data = []
start = time.time()
for i in range(10000000):
    data.append(random.randrange(-10,10))
end = time.time()
elapsed = end - start
print(f"This took {elapsed} seconds to generate 10 million random numbers" )

start = time.time()
dataMap1 = []
for i in data:
    dataMap1.append(f(i))
end = time.time()
print(f"This took {end-start} seconds to do list with a for loop")


start = time.time()
dataMap2 = [f(i) for i in data]
end = time.time()
print(f"This took {end-start} seconds to do list comprehension")

start = time.time()
dataMap3 = map(f,data)
end = time.time()
print(f"This took {end-start} seconds to do a list map")



