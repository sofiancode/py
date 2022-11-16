# Tuple is a collection of objects separated by commas. In some ways, a tuple is similar to a list in terms of indexing, nested objects, and repetition but a tuple is immutable, unlike lists which are mutable.

# Tuple
myTuple = (1, 2, 3, 1.45, 'word', [7, 8, 9, 'word'])
print(myTuple)

# how to pick elements from a tuple list -> Indexing or Slicing
print(myTuple[5])
print(myTuple[5][0])
print(myTuple[-3])
# python assigns each value in a list or tuple an index

# find a word/string 'hello :)'
exerciseList = ['first entry', [123, 456, [0, 'hello :)']], 'by']
soluction = exerciseList[1][2][1]

print(soluction)

# slicing

practiceTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(practiceTuple[0:5:3])

# unpacked

a, b = (10, 5)
print(a)
print(b)
