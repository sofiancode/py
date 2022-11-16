# run some code if a value in the variable is true
x = 0
if x > 5:
    print(f'the if statement was true')
elif x != 0:
    print('the elif statement was correct')
else:
    print('the code that was run if statement was false')


if 1 in [1, 2, 3, 4]:
    print('runner')


moneyAvailable = 100
hungry = True
bored = True

if moneyAvailable >= 80:
    print('eat something fancy')
elif moneyAvailable > 45:
    print('eat something nice')
elif moneyAvailable > 15:
    print('eat something okay')
else:
    print('eat something cheap')

if moneyAvailable > 80 and hungry == True or bored == True:
    print('eat something fancy')
