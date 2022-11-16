# variable = a container for a value. Behaves as the value that it contains.


# string -- store a series of characters
# integer -- store a whole number
# float -- store a floating point number
# boolean -- true or false

# *****************************
# string

from operator import truediv


firstname = 'Nolan'
lastName = 'Sofian'
fullName = f'{firstname} {lastName}'

print(f'Hello {fullName}')

# *****************************
# int = integer (a whole number)


age = 21
age = age + 1
age += 1

# print(age)
# print(type(age))


# *****************************
# float = floating point number (a decimal number)

height = 250.5

# print(height)
# print(f'your height is: {height} cm')
# print(type(height))

# *****************************
# boolean (true or false)

human = True

# print(human)
# print(type(human))

# print('are u a human: '+str(human))
# print(f'are u a human: {human}')

# *****************************
# multiple assignment = allows us to assign multiple variables at the same time in one line of code

# name = 'Nolan'
# age = 21
# attractive = True


name, age, attractive = 'Nolan', 21, True

# print(name)
# print(age)
# print(attractive)


# Sam = 30
# Dean = 30
# Michael = 30

Sam = Dean = Michael = 30

# print(Sam)
# print(Dean)
# print(Michael)
