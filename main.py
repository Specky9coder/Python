
from math import *

phrase = '_SPECKY_CODER_'
print(phrase.index(''))

my_num = 3.142848935
print(floor(my_num))


Color = input('Enter the Color :')
Think  = input('Enter the name :')
Object = input('Enter the Object name :')
Person = input('Enter the Person name :')
My_love = input('Enter the name of my Love :')




print('Clouds are  '+ Color)
print(Think +' thinking of mine is right')
print('Make your '+ Object +' in contact to mine ')
print('Listen to me '+  Person)
print('I love you '+ My_love)

numbers = [9,11,1998]
friends = ['Karen', 'Mitchlle', 'Logan']
print(friends)
friends.extend(numbers)
friends.pop(4)
friends.insert(3,'Purva '+'Desai')
print(friends)



def say_hi(name, age ):
    print('Hello ' + name+ 'Your Age Is ' + str(age))

say_hi('Keyur ', 21)
say_hi('Purva ', 21)

print('hi\n')

say_hi()

def Cube(number):
    return number*number*number

cube = Cube(14)
cube2 = Cube(9)
print(cube)
print(cube2)


Is_male = False
Is_female = False



if Is_male and Is_female:
    print('You are a handsome male ')

elif Is_male and not(Is_female):
    print('You are a female' )
elif not(Is_male) and Is_female:
    print('You are not a male or but are female')

else:
    print('You are not a male or  not female')


def Max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(Max_num(9, 11, 14))


def Max_num(num1, num2, num3):
    if num1 != num2 and num1 != num3:
        return num1
    elif num2 != num1 and num2 != num3:
        return num2
    else:
        return num3

print(Max_num(9,14, 11))

def Max_num(num1, num2, num3):
    if num1 == num2 and num1 == num3:
        return num3
    elif num2 == num1 and num2 == num3:
        return num2
    else:
        return num3

print(Max_num(9, 11, 14))

def Max_num(num1, num2, num3):
    if num1 <= num2 and num1 <= num3:
        return num1
    elif num2 <= num1 and num2 <= num3:
        return num2
    else:
        return num3

print(Max_num(9, 11, 14))




num1 = float(input('Enter the Value : '))
operator = input('Enter The Value: ')
num2 = float(input('Enter The Value: '))

if operator == '+':
    print(num1 + num2)

elif operator == '-':
    print(num1 - num2)

elif operator == '*':
    print(num1 * num2)

elif operator == '/':
    print(num1 / num2)
else:
    print('Does not Calculate ')




monhtConversions = {
    'Jan': 'January',
    'Feb':  'February',
    'Mar':  'March',
    'Apr': 'April',
    'May': 'May',
    'Jun': 'June',
    'Jul': 'July',
    'Aug': 'August',
    'Sep': 'September',
    'Oct': 'October',
    'Nov': 'November',
    'Dec': 'December'
}

print(monhtConversions.get('Jan' ,'Not a valid key'))



i = 1
while i <= 10:

    print(i)
    i += 1


print('Done')

Forbid_Word = 'Specky'
Forbid_Word2 = 'Purva'
Predict = ''
Prediction = 0
Predicted = 3
Fuck_Off = False

while Predict != Forbid_Word and not(Fuck_Off):
    if Prediction < Predicted:
        Predict = input('Forbid_Word : ')
        Prediction += 1

    elif Prediction < Predicted:
        Predict = input('Forbid_Word2 : ')
        Prediction += 1

    else:
        Fuck_Off = True

if Fuck_Off:
    print('Get The Fuck Off')

else:
    print('Gotchha')

Amigos = ['Chris', 'Vamos','Vienna', 'Vanice']

for Index in range(5):
    if Index ==0:
        print('First Iteration')

    else:
        print('Not First')


def Raise_to_Power(Base,Power):
    Res = 1
    for index in range(Power):
        Res = Res * Base
    return Res

print(Raise_to_Power())

Number_Grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]


for row in Number_Grid:
    #print(row)

    for column in row :
        print(column)



def Translate(Phrase):
    Translation = ''
    for letters in Phrase:
        if letters.lower() in 'aeiou':
            if letters.isupper():
                Translation = Translation + 'S'
        else:
            Translation = Translation + 's'

    return Translation
print(Translate(input('Enter The Phrase:')))



try:
    #vale = 10/0
    number = int(input('Hi:'))
    print(number)
except ZeroDivisionError as error:
    print(error)
except ValueError as error:
    print(error)


Intents_file = open('intents.jason1.txt', 'a')
Intents_file.write('Specky_Coder')
print()
Intents_file.close()

import Useful_Tools

print(Useful_Tools.Roll_Dice(10))

# An Object is Instance Of a Class.
# Create a Student Name With The Following Attributes.


from Students import Student

from Students import Students_female

from Students import Students_Mobile

from Students import Students_female_Mobile
from Students import intelligent_Student
from Students import Students_with_Laptops

Students1 = Student('Specky\n', 'Computer Science\n', 4.0, False)

Students_female = Students_female('Illusionnist\n', 'Information Technology\n', 3.0, True)

print(Students1.name, Students1.major, Students1.gpa, Students1.is_on_probation)

print(Students_female.name, Students_female.major, Students_female.gpa, Students_female.is_intern_or_not)

Students_Mobile = Students_Mobile('Note 7s\n', 'Pie 9\n', 10000, False)
Students_female_Mobile = Students_female_Mobile('Iphone 6s\n', 'IOS 11\n', 50000, True)

print(Students_Mobile.Model, Students_Mobile.Operating_system, Students_Mobile.A_version, Students_Mobile.is_Costly_or_not)

print(Students_female_Mobile.Model, Students_female_Mobile.Operating_system, Students_female_Mobile.A_version, Students_female_Mobile.is_Costly_or_not)

Students = intelligent_Student(True, 'Average Student\n', 'Not\n', True)

print(intelligent_Student.intelligent , intelligent_Student.A_student, intelligent_Student.Ab_a_stuedent, intelligent_Student.is_intelligent_or_not)

Students_with_laptops = Students_with_Laptops('User Seriese \n', 'Windows 10', '60000', )
print(Students_with_Laptops.L_type, Students_with_Laptops.Operating_system, Students_with_Laptops.Price)





from Question import Question

question_prompts = [
    'What Color Are Apples ? \n(a) Red/Green\n(b) Purple\n(c) Orange\n\n',
    'What Color Are Banana ? \n(a) White\n(b) Yellow/Green\n(c)Pink\n\n',
    'What Color Are Strawberries ?\n(a) Magenta\n(b) Red\n(c) Black\n\n'

]

questions = [
    Question(question_prompts[0], 'a'),
    Question(question_prompts[1], 'b'),
    Question(question_prompts[2], 'b'),
]

def run_test(questions):
    score = 0
    correct = 3
    for question in questions:
        answer = input(question.prompt)
    if answer == question.answer:
        score += 1
    if answer < question.answer :
        print('Your Result is  good' )
    elif:
        print('Your Result is Poor')

    else:
     print('Awsome ' + str(score) + '/' + str(len(questions)))

run_test(questions)




from Student import Student

Student1 = Student('Specky', 'Computer Science', 4.5)
Student2 = Student('Purva', 'Information Technology', 3.5)

print(Student2.on_honor_roll())

print(Student1.is_in_criteria())



from Chef import Chef
from ItaliyanChef import ItaliyanChef
from FrenchChef import FrenchChef
from PersianChef import PersianChef
myItaliyanChef = ItaliyanChef()

myItaliyanChef.make_Rissoto()
myFrenchChef = FrenchChef()

myFrenchChef.make_Creambrulle()
myChef = Chef()
myFrenchChef.make_Special_dish()

myFrenchChef.make_salad()
myFrenchChef.make_chicken()

myPersianChef = PersianChef()
myPersianChef.make_Special_Dish()
myPersianChef.make_chicken()
myPersianChef.make_salad()
