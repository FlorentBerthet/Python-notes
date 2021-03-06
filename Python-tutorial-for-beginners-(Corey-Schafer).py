
# Python Tutorial for beginners (Corey Schafer)

# 2. Strings - Working with Textual data
	# https://www.youtube.com/watch?v=k9TUPpGqYTo&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=2

message = 'Hello World'

print (message[10])
	-> d

print (message[:5])
	-> Hello

print (message.upper())
	-> HELLO WORLD

print (message.count('l'))
	-> 3

print (message.find ('World'))
	-> 6  (it starts at the 6th index)

message.replace ('World', 'Universe')

print (message)
	-> Hello Universe
-
greeting = 'Hello'
name = 'Michael'
message = greeting + ', ' + name

print(message)
	-> Hello, Michael

message = '{}, {}. Welcome!'.format(greeting, name)

print(message)
	-> Hello, Michael. Welcome!



# 3: Integers and Floats - Working with Numeric Data
	# https://www.youtube.com/watch?v=khKv-8q7YmY&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=3

num = 3.14

print(type(num))
	-> <class 'float'>
-
print (3 // 2)
	->  1
	'''This is a floor division = division without the modulus'''
-
print (3 ** 2)
	-> 9 (exponent)
-
print(10 % 7)
	-> 3 (modulus)
-
num = 2
num *= 3

print(num)
	-> 6
-
print(round(3.75,1))
	-> 3.8
-
num_1 = 2
num_2 = 3

print(num_1 == num_2)
	-> False
-
num_1 = '100'
num_1 = int(num_1)
	'''Transforms into an integer'''


# 4: Lists, Tuples, and Sets
	# https://www.youtube.com/watch?v=W8KRzm-HUcc&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=4

# Lists:

courses = ['History', 'Math', 'Physics', 'CompSci']
nums = [1, 5, 2, 4, 3]

print(len(courses))
	-> 4

print(courses[0])
	-> ['History']

print(courses[0:2])
	-> ['History', 'Math']
	'''The last index is excluded'''

print(courses[-1])
	-> ['CompSci']

print(courses[2:])
	-> ['Physics', 'CompSci']

courses.append('Art')
	'''Adds 'Art' at the end of the list'''

courses.insert(0, 'Art')
	'''Adds 'Art' at the beginning of the list'''

courses_2 = ['Art', 'Education']
courses.extend(courses_2)
	'''Adds 'Art' and 'Education' at the end of the list'''

courses.remove('Math')
	'''Removes 'Math' from the list'''

courses.pop()
	'''Removes the last value of the list'''

popped = courses.pop()

print(popped)
	-> 'CompSci'

courses.reverse()
	'''Reverses the values of the list'''

courses.sort()
	'''Sorts by alphabetical order or ascending order'''

courses.sort(reverse=True)
	'''Sorts by reversed alphabetical order or descending order'''

sorted_courses = sorted(courses)
	'''Creates a variable with sorted values'''

print(min(nums))
	-> 1

print(sum(nums))
	-> 15

print(courses.index('CompSci'))
	-> 3
	'''Prints the index of a value'''

print('Biology' in courses)
	-> False  (checks if value is in list)

for course in courses:
	print(course)
	'''Prints each item of the variable'''

for index, course in enumerate(courses):
	print(index, course)
	-> 0 History
	-> 1 Math
	-> 2 Physics
	-> 3 CompSci

for index, course in enumerate(courses, start=1):
	print(index, course)
	-> 1 History
	-> 2 Math
	-> 3 Physics
	-> 4 CompSci

course_str = ', '.join(courses)
print(course_str)
	-> History, Math, Physics, CompSci

course_str = ', '.join(courses)
new_list = course_str.split (', ')
	-> ['History', 'Math', 'Physics', 'CompSci']

'''
Tuples:
	We can't mutate/change the values in the tuple
	Format: Tuple_1 = ('Math', 'History')

Sets:
	Sets are values that are unordered and have no duplicates
	Format: Set_1 = {'Math', 'History'}
'''

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses.intersection(art_courses))
	-> ('History', 'Math')

print(cs_courses.difference(art_courses))
	-> ('Physics', 'CompSci')

print(cs_courses.union(art_courses))
	-> ('Art', 'CompSci', 'Math', 'Design', 'History', 'Physics')
-
empty_list = []
	'''Creates an empty list'''
empty_tuple = ()
	'''Creates an empty tuple'''
empty_set = set{}
	'''Creates an empty set'''
empty_dict = {}
	'''Creates en empty dictionary'''


# 5: Dictionaries - Working with Key-Value Pairs
	# https://www.youtube.com/watch?v=daefaLgNkw0&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=5

student = {'name': 'John', 'age': 25, 'courses':['Math', 'CompSci']}

print(student['name'])
	-> John

print(student.get('phone', 'Not Found'))
	-> Not Found

student['phone'] = '555-5555'
print(student.get('phone', 'Not Found')
	-> 555-5555

student['name'] = 'Jane'
	''' Changes the name'''

student.update({'name': 'Jane', 'age':26, 'phone': '555-5555'})
	''' Updates or adds several keys '''

del student['age']
	''' Deletes a key '''

age = student.pop('age')
	''' Pops a key '''

prints(student.items())
	-> dict_items([('name', 'John'), ('age', 25), ('courses', ['Math', 'CompSci'])])

for key in student.items()
	print (key, value)
	-> name John
	-> age 25
	-> courses ['Math', 'CompSci']


# 6: Conditionals and Booleans - If, Else, and Elif Statements
	# https://www.youtube.com/watch?v=DZwmZ8Usvnk&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=6

language = 'Java'

if language == 'Python':
	print('Language is Python')
elif language == 'Java'
	print('Language is Java')
elif language == 'JavaScript'
	print('Language is JavaScript')
else:
	print('No match')
	-> No match
-
user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
	print ('Admin Page')
else:
	print ('Bad Creds')
-
'''
Values that evaluate to False:
	False
	None
	Zero of any numeric type
	Any empty sequence or mapping, for example: '', (), [], {}
'''

condition = ''

if condition:
	print('Evaluated to True')
else:
	print('Evaluated to False')
	-> Evaluated to False

# 7: Loops and Iterations - For/While Loops
	# https://www.youtube.com/watch?v=6iF8Xb7Z3wQ&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=7

nums = [1,2,3,4,5]

for num in nums:
	if num == 3
		print('Found!')
		break
	print(num)
	-> 1
	-> 2
	-> Found!

for num in nums:
	if num == 3
		print('Found!')
		continue
	print(num)
	-> 1
	-> 2
	-> Found!
	-> 3
	-> 4
'''The 'continue' makes the function go to the next value (so it doesn't print the '3')'''

for num in nums:
	for letter in 'abc':
		print(num, letter)
	-> 1 a
	-> 1 b
	-> 1 c
	-> 2 a
	-> ...
-
for i in range(1,5):
	print(i)
	-> 1
	-> 2
	-> 3
	-> 4
-
x = 0

while x < 3:
	print(x)
	x += 1
	-> 0
	-> 1
	-> 2

while True:
	if x == 5
		break
	print(x)
	x += 1
	-> 0
	-> 1
	-> 2
	-> 3
	-> 4

# 8: Functions
	# https://www.youtube.com/watch?v=9Os0o3wzS_I&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=8

def hello_func():
	print('Hello Function.')

hello_func()
	-> Hello Function.
-
def hello_func():
	return('Hello Function.')
print(hello_func())
	-> Hello Function.
-
def hello_func(greeting):
	return '{} Function'.format(greeting)
print(hello_func('Hi'))
	-> Hi Function
-
def hello_func(greeting, name = 'You'):
	return '{}, {}'.format(greeting)
print(hello_func('Hi'))
	-> Hi, You
-
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('math', 'bio', name='John', age=22)
	-> ('math', 'bio')
	-> {'name': 'John', 'age': 22}
-
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

course = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(*courses, **info)
	-> ('math', 'bio')
	-> {'name': 'John', 'age': 22}

-
# Example: Return number of days in that month in that year

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
	'''return true for leap years'''
	return year % 4 == 0 and (year %100 != 0 or year %400 == 0)

def days_in_month (year, month):
	'''Return number of days in that month in that year'''
	if not 1 <= month <=12:
		return 'Invalid month'
	if month == 2 and is_leap(year):
			return 29
	return month_days[month]

print(is_leap(2020))
print(days_in_month(2019, 2))
	-> True
	-> 28


# 9: Import Modules and Exploring The Standard Library
	# https://www.youtube.com/watch?v=CqvZ3vGoGs0&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=9

# To import a module

	# in module_A (both modules have to be in the same directory):

import module_B
'''We can also shorten the name of the module by writing: import module_B as bla'''

courses = ['History', 'Math', 'Physics', 'CompSci']

index = module_B.find_index(courses, 'Math')
print(index)

# in module_B:

# To find the index of a value in a sequence

def find_index(to_search, target):
	for i, value in enumerate(to_search):
		if value == target:
			return i
	return -1
-
# To import a function from a module

from module_B import find_index
	'''We can then use the 'find_index' function simply by typing its name'''

# To import several functions or variables from a module

from module_B import find_index, variable_A

# To add a directory to the Python path environment variable (on a Mac)

	# Open Terminal
	# Type:
	# 	$ nano ~/.bash_profile
	# 	export PYTHONPATH="/Users/user_name/Desktop/My-modules"
	# Save by: control-x, y, enter
	# Restart Terminal

# Using library modules

	# Random

import random

courses = ['History', 'Math', 'Physics', 'CompSci']
random_course = random.choice(courses)
print(random_course)

	# Math

		# Example with radians:
import math
rads = math.radians(90)
print(rads)
	-> 1.57079632679

	# datetime

import datetime
today = datetime.date.today()

	# calendar

import calendar
print(calendar.isleap(2017))
	-> False

	# os

		# To show current working directory
import os
print(os.getcwd())

		# To show the location of a file (example with the os file):
import os
print(os.__file__) '''these are double underscores'''
 
      
