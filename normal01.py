'''
task01
'''

a = int(input('Enter the integer number from 1 to 9:'))
while a<0 or a>=10:
    print('Your input is invalid. Try again.')
    a = int(input('Enter the integer number from 1 to 9:'))
print('Square of the entered number is: ', a ** 2)
print('Finish')


'''
task02
'''

a = int(input('Enter first integer number:'))
b = int(input('Enter second integer number:'))
a = a + b
b = a - b
a = a - b
print('Numbers have been swiched')
print('First number is: ', a)
print('Second number is: ', b)
print('Finish')