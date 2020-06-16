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

---
elif statements

Remember that at most only one of the clauses will be executed, and for elif statements, the order matters!

---
“If you ran the following program:
print('Hello')
print('World')
the output would look like this:
Hello
World
The two strings appear on separate lines because the print() function automatically adds a newline character to the end of the string it is passed. However, you can set the end keyword argument to change this to a different string. For example, if the program were this:
print('Hello', end='')
print('World')
the output would look like this:
HelloWorld”

---
“>>> print('cats', 'dogs', 'mice', sep=',')
cats,dogs,mice”

---
“Parameters and variables that are assigned in a called function are said to exist in that function’s local scope. Variables that are assigned outside all functions are said to exist in the global scope. A variable that exists in a local scope is called a local variable, while a variable that exists in the global scope is called a global variable. A variable must be one or the other; it cannot be both local and global.”

---
“Think of a scope as a container for variables. When a scope is destroyed, all the values stored in the scope’s variables are forgotten. There is only one global scope, and it is created when your program begins. When your program terminates, the global scope is destroyed, and all its variables are forgotten. Otherwise, the next time you ran your program, the variables would remember their values from the last time you ran it.”


---

“Scopes matter for several reasons:
Code in the global scope cannot use any local variables.
However, a local scope can access global variables.
Code in a function’s local scope cannot use variables in any other local scope.
You can use the same name for different variables if they are in different scopes. That is, there can be a local variable named spam and a global variable also named spam.”
---

“The reason Python has different scopes instead of just making everything a global variable is so that when variables are modified by the code in a particular call to a function, the function interacts with the rest of the program only through its parameters and the return value. This narrows down the list code lines that may be causing a bug.”

---
“While using global variables in small programs is fine, it is a bad habit to rely on global variables as your programs get larger and larger.”

---
“The global Statement
If you need to modify a global variable from within a function, use the global statement. If you have a line such as global eggs at the top of a function, it tells Python, “In this function, eggs refers to the global variable, so don’t create a local variable with this name.” For example, type the following code into the file editor and save it as sameName2.py:
  def spam():
➊    global eggs
➋    eggs = 'spam'

  eggs = 'global'
  spam()
  print(eggs)
When you run this program, the final print() call will output this:
spam”

---
“There are four rules to tell whether a variable is in a local scope or global scope:
If a variable is being used in the global scope (that is, outside of all functions), then it is always a global variable.
If there is a global statement for that variable in a function, it is a global variable.
Otherwise, if the variable is used in an assignment statement in the function, it is a local variable.
But if the variable is not used in an assignment statement, it is a global variable.”

---
“Errors can be handled with try and except statements. The code that could potentially have an error is put in a try clause. The program execution moves to the start of a following except clause if an error happens.”

---
“def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
When code in a try clause causes an error, the program execution immediately moves to the code in the except clause. After running that code, the execution continues as normal. The output of the previous program is as follows:
21.0
3.5
Error: Invalid argument.
None
42.0
Note that any errors that occur in function calls in a try block will also be caught. Consider the following program, which instead has the spam() calls in the try block:
def spam(divideBy):
    return 42 / divideBy

try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error: Invalid argument.')
When this program is run, the output looks like this:
21.0
3.5
Error: Invalid argument.
The reason print(spam(1)) is never executed is because once the execution jumps to the code in the except clause, it does not return to the try clause. Instead, it just continues moving down as normal.”

---
“Lists can also contain other list values. The values in these lists of lists can be accessed using multiple indexes,
like so:
>>> spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
>>> spam[0]
['cat', 'bat']
>>> spam[0][1]
'bat'
>>> spam[1][4]
50”

---
“The Multiple Assignment Trick
The multiple assignment trick is a shortcut that lets you assign multiple variables with the values in a list
in one line of code. So instead of doing this:
>>> cat = ['fat', 'black', 'loud']
>>> size = cat[0]
>>> color = cat[1]
>>> disposition = cat[2]

you could type this line of code:
>>> cat = ['fat', 'black', 'loud']
>>> size, color, disposition = cat”

---
remove vs del:

>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam.remove('bat')

>>> spam = ['cat', 'bat', 'elephant']
>>> del spam[2]

“If the value appears multiple times in the list, only the first instance of the value will be removed. ”

 ---
 reverse:

>>> spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
>>> spam.sort(reverse=True)
>>> spam
['elephants', 'dogs', 'cats', 'badgers', 'ants']

---
Third, sort() uses “ASCIIbetical order” rather than actual alphabetical order for sorting strings.
This means uppercase letters come before lowercase letters. Therefore, the lowercase a is sorted so
that it comes after the uppercase Z. For an example, enter the following into the interactive shell:

>>> spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
>>> spam.sort()
>>> spam
['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']

If you need to sort the values in regular alphabetical order, pass str. lower for the key keyword argument
in the sort() method call.

>>> spam = ['a', 'z', 'A', 'Z']
>>> spam.sort(key=str.lower)
>>> spam
['a', 'A', 'z', 'Z']

This causes the sort() function to treat all the items in the list as if they were lowercase without
actually changing the values in the list.
