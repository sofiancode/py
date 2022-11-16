# variables

# calculationToHours = 24
# nameOfUnit = 'hours'

#  function


# def daysToHours(numOfDays, customMessage):
#     print(f'{numOfDays} days are {numOfDays * calculationToHours} {nameOfUnit} ')
#     print(customMessage)

# invoke function


# daysToHours(30, 'goody')
# daysToHours(60, 'great')
# daysToHours(90, 'excellent')

# function


# def scopeCheck(numOfDays):
#     myVariable = 'variable inside function'
#     print(nameOfUnit)
#     print(numOfDays)
#     print(myVariable)


# scopeCheck(20)

# user input

# \n -- represent - new line

# userInput = input('hey user, please type your name\n')
# print(userInput)

# function with return values

# first = 2 * 2
# second = 3 * 3


# def calcNumb():
#     return f'{first} + {second} '


# finalResult = calcNumb()
# print(finalResult)

# conditionals (if / else) and
# boolean data type

# ---------------------------

# age = 17


# def allowedToDrive(age):
#     if age < 18:
#         return 'good to go'
#     else:
#         return 'next time buddy'


# userInput = input('your age\n')
# userInputNumber = int(userInput)

# calcValue = allowedToDrive(userInputNumber)
# print(calcValue)

# age = int(input(f'enter your age:\n'))

# if age >= 18:
#     print('you are signed up')
# else:
#     print('u must be 18teen to sign up')


# string methods

name = 'sofian'

print(len(name))

print(name.find('a'))

print(name.capitalize())

print(name.upper())
