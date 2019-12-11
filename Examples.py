
num = int(input('Enter the number to divide :'))

listRange = list(range(1, num+1))

divisorList = []

for number in listRange:
    if num % number == 0:
        divisorList.append(number)

print(divisorList)


a = [1, 2, 3, 4, 5, 6,]
b = [6, 5, 4, 3, 1 ]

c = []

for i in b:
    if i in b:
        c.append(i)

print(c)

import random

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = [num for num in a if num % 2 == 0]

print(even)

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd = [num for num in b if num % 1 == 1]

print(b)


import random

number = random.randint(1, 9)
Guess = 0
Count = 0

while Guess != number and Count != 'Exit':
    Guess = input('Guess The Number:')
    if Guess == 'exit':
        break

    Guess = int(Guess)
    Count += 1

    if Guess < Count:
        print('Too Low')

        if Guess > Count:
            print('Too High')

        else:
            print('You Got It')
            print('And It Only Took You ', Count, 'Tries !')




import random
a = random.sample(range(1, 30),12)
b = random.sample(range(1, 30),16)

result = [i for i in a if i in b]
print(result)



