
### An iterable is any Python object capable of returning its members one at a time, permitting it to be iterated over 
in a for-loop.
Familiar examples of iterables include lists, tuples, and strings - any such sequence can be iterated over in a for-loop.


### Use the elif condition is used to include multiple conditional expressions between if and else.

if x==1:
    print('X is 1')
elif x==5:
    print('X is 5')
elif x==10:
    print('X is 10')
else:
    print('X is something else')


### Frequency of each character in String

'''
Using collections.Counter()
The most suggested method that could be used to find all occurrences is this method,
this actually gets all element frequency and could also be used to print single element frequency if required.
'''

from collections import Counter 

test_str = "GeeksforGeeks"
res = Counter(test_str)

# Output:
Counter({'e': 4, 's': 2, 'k': 2, 'G': 2, 'o': 1, 'r': 1, 'f': 1})

'''
Using dict.get()

get() method is used to check the previously occurring character in string, 
if its new, it assigns 0 as initial and appends 1 to it, 
else appends 1 to previously holded value of that element in dictionary.
'''

test_str = "GeeksforGeeks"
res = {} 
for keys in test_str: 
    res[keys] = res.get(keys, 0) + 1
 
### Classes

class Student:
	def __init__(self, age, nom, prenom):
		self.age = age
		self.nom = nom
		self.prenom = prenom
	def __repr__(self):
		return str(self.prenom) + " " + str(self.nom) + " (" + str(self.age) + " ans)"
	def __str__(self):
		return str(self.prenom) + " " + str(self.nom) + " (" + str(self.age) + " ans)"


def AddStudent( cont, item ):
	cont[ item.prenom ] = item


students = dict()
AddStudent( students, Student(25, 'berthet', 'jerome'))
AddStudent( students, Student(20, 'berthet', 'florent'))
AddStudent( students, Student(20, 'berthet', 'nadia'))
print students


