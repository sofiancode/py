# name = 'tom'
# age = 30
# greetingString = f'hello {name}, you are {age} years old'
# print(greetingString)

##

name = 'Ron'
hobby = 'reading books'
fString = f'hello my name is {name} \nand my hobby is {hobby}'
print(fString)


age = int(input(f'how old are u ?'))

if age >= 18:
    print(f'you are an adult')
elif age < 0:
    print(f'you havent been born yet')
else:
    print(f'you are a child!')
