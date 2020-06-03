'''
Expressions consist of values (such as 2) and operators (such as +), and they can always evaluate (that is, reduce) 
down to a single value. That means you can use expressions anywhere in Python code that you could also use a value.

Assignment: variable = value
An assignment statement consists of a variable name, an equal sign (called the assignment operator), and the value
to be stored. If you enter the assignment statement spam = 42, then a variable named spam will have the integer 
value 42 stored in it.
---
Variable names can't begin with a number

---
print('Hello world!')
print('What is your name?')    # ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')    # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')

---
print() # prints a blank line

input() # waits for the user to type some text on the keyboard and press ENTER

You can't concatenate an integer and a string, e.g.: print('I am ' + 29 + ' years old.')
You can use the str() function as a solution: print('I am ' + str(29) + ' years old.')

The input() function always returns a string, even if the user enters a number

>>> int(7.7)
7
>>> int(7.7) + 1
8

Excerpt From: Sweigart, Albert. “Automate the Boring Stuff with Python: Practical Programming for Total Beginners”. Apple Books. 
Excerpt From: Sweigart, Albert. “Automate the Boring Stuff with Python: Practical Programming for Total Beginners”. Apple Books. 
