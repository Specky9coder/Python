
name = input('Enter Your name:')
age = int(input('Enter Your Age:'))

year = str((1998-age)+100)
print(name + 'you will be 100 years old in the year ' + year)





num = str(input('Enter The Number:'))

mod =num % 2

if mod > 0:
    print('The Number Is Odd ')

else:
    print('The Number Is Even')


lst = [1,2,3,4,5,7,8,9,10]

if lst < 5:
    print(lst)

def add(param1 ,param2):
    input('param1:')
    input('Param2:')
    return param1+param2

add()



x = 34 -23
y = 'Hello'
z = 3.45
y = 'Hi'
if z == 3.45 or y == 'Hello':
    x += 1
    y  =  y + ' Hello'
    print(x)
    print(y)
