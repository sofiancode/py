# Python Lists are just like dynamically sized arrays,
# declared in other languages (vector in C++ and ArrayList in Java).
# In simple language, a list is a collection of things,
# enclosed in [ ] and separated by commas.

myList = [1, 2, 3, 4, 5, 'word']
print(myList)
print(len(myList))  # functions
myList.reverse()  # methods
myList.append(16)  # methods
print(myList)

# how to pick a multiple elements from a list
# [1,2,3,4] -  hpw to get the second and tird element?

testList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(testList[1:2])  # slicing
print(testList[-1:4:-1])

# defaultSlicing = testList[start:end:step]
# start -> first value of the list
# end -> last value in list
# step -> 1
defaultSlicing = testList[::2]
print(defaultSlicing)


practice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
solution = practice[7:0:-2]
print(solution)

practiceTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(practiceTuple[0:5:3])

# unpacked

c, d = [20, 'hello']
print(c)
print(d)
