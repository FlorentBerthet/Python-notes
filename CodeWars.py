```Python

# codewars.com

# Highest and Lowest (7kyu)

# Incorrect solution. 
# For some reason, gives '(ValueError: min() arg is an empty sequence)' even though it works on Sublime Text
  
def high_and_low(numbers):
    numbers = numbers.split(' ')
    numbers = map(int, numbers)
    numbers = max(numbers), min(numbers)
    numbers = str(numbers).replace("(", '"').replace(")",'"').replace(", "," ")
    print numbers

high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")

# Correct solution:

def high_and_low(numbers):
    numbers = numbers.split(' ')
    numbers = sorted(numbers, key=int)
    return numbers[-1] + ' ' + numbers[0]


# Replace With Alphabet Position

from string import ascii_lowercase

IndexedLetters = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start = 1)}

def alphabet_position(text):
    text=text.lower()
    Numbers = [IndexedLetters[character] for character in text if character in IndexedLetters]
    return ' '.join(Numbers)

# Solution 2

from string import ascii_uppercase

def alphabet_position(text):
    return " ".join(str(ascii_uppercase.index(i) + 1) for i in text.upper() if i in ascii_uppercase)

# Take a Ten Minute Walk

def is_valid_walk(walk):

    if len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('w') == walk.count('e'):
    	return True
    else:
        return False

# Solution 2

def isValidWalk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')

# Find the odd int

def find_it(seq):
    for i in seq:
    	if seq.count(i) %2 != 0:
    		return i

# Exes and Ohs

	# Check to see if a string has the same amount of 'x's and 'o's.
	# The method must return a boolean and be case insensitive. The string can contain any char.
def xo(s):
	if s.count('x')+s.count('X') == s.count('o')+s.count('O'):
        # if the sum of x's and X's is equal to the sum of o's and O's
		return True
	else:
		return False

# Solution 2

def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')

# Sum of odd numbers

"""
Given the triangle of consecutive odd numbers:
             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:

row_sum_odd_numbers(1); # 1
row_sum_odd_numbers(2); # 3 + 5 = 8
"""

def row_sum_odd_numbers(n):
    # We can solve this with these 2 steps:
        # first_number_in_row = n**2 - (n-1)
        # sum_odd=first_number_in_row * n + (n-1) * n
            # first_number * n multiplies the first number in the row by the number of items in the row
            # (n-1) * n represents the sum of the differences between the subsequent numbers and the first number
    # Merging these two gives us the solution below.

sum_odd=(n**2 - (n-1))*n + (n-1)*n

   return sum_odd

# Solution 2

def row_sum_odd_numbers(n):
    return n ** 3

# Create Phone Number

    # Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
    # Example:
        # create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

def create_phone_number(n):
    phone_number='('
    for i, num in enumerate(n):
        if i<2:
            phone_number += str(num)
        elif i==2:
            phone_number += str(num)+') '
        elif i<5:
            phone_number += str(num)
        elif i==5:
            phone_number += str(num)+'-'
        elif i<9:
            phone_number += str(num)
        elif i==9:
            phone_number += str(num)
    return(phone_number)

# Solution 2

def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

# Is a number prime?

def is_prime(n):

    if (n <= 1):
        return False
    if (n <= 3):
        return True

    if (n % 2 == 0 or n % 3 == 0):
        return False

    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6

    return True

# Solution 2

def is_prime(num):
    import math

    # There's only one even prime: 2
    if num < 2    : return False
    if num == 2   : return True
    if num %2 == 0: return False

    
    """
    Property:
        Every number n that is not prime has at least one prime divisor p
        such 1 < p < square_root(n)
    """
    root = int(math.sqrt(num))
    
    # We know there's only one even prime, so with that in mind 
    # we're going to iterate only over the odd numbers plus using the above property
    # the performance will be improved
    for i in xrange(3, root+1, 2):
        if num % i == 0: return False

    return True

# Solution 3

from math import sqrt

def is_prime(n):
  return n > 1 and all(n % d for d in xrange(2, int(sqrt(n)) + 1))

# Convert string to camel case

'''
Complete the method/function so that it converts dash/underscore delimited words into camel casing.
The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case,
also often referred to as Pascal case).

Examples

to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"

'''

from string import ascii_letters

def to_camel_case(text):
    
    # Creating a dictionary with each possible part to replace and their replacement
    xdic={}

    for i in ascii_letters:
        xdic['_'+i]=i.upper()
        xdic['-'+i]=i.upper()

    for key in xdic:
        text=text.replace(key, xdic[key])

    return(text)

# Solution 2

def to_camel_case(s):
    return s[0] + s.title().translate(None, "-_")[1:] if s else s
   
# Solution 3

def to_camel_case(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')

#Pete the baker

'''
Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths.
Can you help him to find out, how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object)
and returns the maximum number of cakes Pete can bake (integer).
For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200).
Ingredients that are not present in the objects, can be considered as 0.

Examples:

# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})
'''
def cakes(recipe, available):
    cakes_per_item={}
    for item in recipe:
        if item in available:
            cakes_per_item.update({item: available[item]//recipe[item]})
        else:
            cakes_per_item[item] = 0
    max_cakes=min(cakes_per_item.values())
    return(max_cakes)
    
# Solution 2

def cakes(recipe, available):
    return min(available.get(k, 0)/recipe[k] for k in recipe)
  

# Bit Counting

'''
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

'''

def countBits(n):
    binary = '{0:b}'.format(n)
    ones = binary.count('1')
    return ones

# Solution 2

def countBits(n):
    return bin(n).count("1")


# Scramblies

'''
Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

Notes:

Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered

Examples
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
'''

def scramble(s1, s2):
    for char in s2:
        if char not in s1:
            return False
    s1_char_count = {}
    for char in s1:
        if char in s1_char_count:
            s1_char_count[char] += 1
        else:
            s1_char_count[char] = 1
    s2_char_count = {}
    for char in s2:
        if char in s2_char_count:
            s2_char_count[char] += 1
        else:
            s2_char_count[char] = 1
    for char, count in s2_char_count.items():
        if char in s2_char_count and s1_char_count[char] < s2_char_count[char]:
            return False
    return True    

# Solution 2

def scramble(s1,s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True

# Solution 3

from collections import Counter
def scramble(s1,s2):
    # Counter basically creates a dictionary of counts and letters
    # Using set subtraction, we know that if anything is left over,
    # something exists in s2 that doesn't exist in s1
    return len(Counter(s2)- Counter(s1)) == 0

# Detect Pangram
'''
 A pangram is a sentence that contains every single letter of the alphabet at least once.
 For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
 because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
'''

def is_pangram(s):
    letters_in_s=""
    for letter in s:
        if letter.isalpha():
            letters_in_s="".join([letters_in_s, letter.lower()])
    if len(set(letters_in_s))<26:
        return False
    else:
        return True

#  Solution 2

import string

def is_pangram(s):
    return set(string.lowercase) <= set(s.lower())

#  Solution 3
import string

def is_pangram(s):
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True

# Solution 4

import string

def is_pangram(s):
    return set(string.ascii_lowercase).issubset(s.lower())