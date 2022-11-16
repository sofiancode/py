# A Set is an unordered collection data type that is iterable, mutable and has no duplicate elements.

mySet = {1, 2, 3, 4, 5, 5}  # dublicate values will be exterminated

print(len(mySet))

# use methods
mySet.add(0)
mySet.remove(5)

print(mySet)

# indexing and slicing does NOT work
# use the type conversion to get one item from the set by index

print(list(mySet)[1])

# coparison operators

boxOne = {1, 2, 3, 4, 5, 5}
boxTwo = {4, 5, 6, 7}

print(boxOne.union(boxTwo))  # mergin these two box of items
print(boxOne.intersection(boxTwo))  # finds shared values
print(boxOne.difference(boxTwo))  # finds diffferences
