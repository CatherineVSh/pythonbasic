print('Welcome to Physical Shape evaluation tool')
name = input('What is your name?')
while bool(name) == False:
    name = input('Nothing has been entered. Please enter you name.')
lastname = input('What is your last name?')
while bool(lastname) == False:
    lastname = input('Nothing has been entered. Please enter you last name.')
print('Hello, ', name, lastname,'. Please provide your data to start evaluation')
age = int(input('How old are you?'))
while bool(age) == False:
    age = input('Nothing has been entered. Please enter you age.')
weight = int(input('How much do you weight?'))
while bool(weight) == False:
    weight = input('Nothing has been entered. Please enter you weight .')
if age <= 30 and (weight >= 50 and weight <= 120):
    print(name, lastname,',', age, 'years old, weight is', weight, 'kg. You are in a good physical shape!')
elif age > 30 and (weight >= 50 and weight <=120):
    print(name, lastname,',', age, 'years old, weight is', weight, 'kg. You need to take care about yourself.')
elif age > 40 and (weight < 50 or weight > 120):
    print(name, lastname,',', age, 'years old, weight is', weight, 'kg. Please schedule doctor appointment')
elif age <= 30 and weight < 50:
    print(name, lastname, ',', age, 'years old, weight is', weight, 'kg. You need to eat well')
elif age <= 30 and weight > 120:
    print(name, lastname, ',', age, 'years old, weight is', weight, 'kg. You need to eat less')
print('Finish')
