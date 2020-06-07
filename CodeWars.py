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


# Catching Car Mileage Numbers (4 kyu)

'''
"7777...8?!??!", exclaimed Bob, "I missed it again! Argh!" Every time there's an interesting number coming up, he notices and then promptly forgets. Who doesn't like catching those one-off interesting mileage numbers?

Let's make it so Bob never misses another interesting number. We've hacked into his car's computer, and we have a box hooked up that reads mileage numbers. We've got a box glued to his dash that lights up yellow or green depending on whether it receives a 1 or a 2 (respectively).

It's up to you, intrepid warrior, to glue the parts together. Write the function that parses the mileage number input, and returns a 2 if the number is "interesting" (see below), a 1 if an interesting number occurs within the next two miles, or a 0 if the number is not interesting.

Note: In Haskell, we use No, Almost and Yes instead of 0, 1 and 2.

"Interesting" Numbers
Interesting numbers are 3-or-more digit numbers that meet one or more of the following criteria:

Any digit followed by all zeros: 100, 90000
Every digit is the same number: 1111
The digits are sequential, incementing†: 1234
The digits are sequential, decrementing‡: 4321
The digits are a palindrome: 1221 or 73837
The digits match one of the values in the awesome_phrases array
† For incrementing sequences, 0 should come after 9, and not before 1, as in 7890. ‡ For decrementing sequences, 0 should come after 1, and not before 9, as in 3210.
'''

def is_interesting(number, awesome_phrases):

    if number < 98:
        return 0

    elif number == 98 or number == 99:
        return 1

# For inputs that must evaluate to 2

    # Any digit followed by all zeros: 100, 90000
    elif all(i == '0' for i in str(number)[1:]):
        return 2


    # Every digit is the same number: 1111
    elif len(set(str(number))) == 1:
        return 2


    # The digits are sequential, incementing: 1234 (0 should come after 9, and not before 1, as in 7890)
    elif str(number) in '1234567890':
        return 2


    # The digits are sequential, decrementing: 4321 (0 should come after 1, and not before 9, as in 3210)
    elif str(number) in '9876543210':
        return 2


    # The digits are a palindrome: 1221 or 73837
    elif number == int(''.join(reversed(str(number)))):
        return 2


    # The digits match one of the values in the awesome_phrases array
    elif number in awesome_phrases:
        return 2


# For inputs that must evaluate to 1

    # Any digit followed by all zeros: 100, 90000
    elif all(i == str(number + 1)[1] for i in str(number + 1)[1:]):
        return 1

    elif all(i == str(number + 2)[1] for i in str(number + 2)[1:]):
        return 1


    # Every digit is the same number: 1111
    elif len(set(str(number + 1))) == 1:
        return 1

    elif len(set(str(number + 2))) == 1:
        return 1


    # The digits are sequential, incementing: 1234 (0 should come after 9, and not before 1, as in 7890)
    elif str(number + 1) in '1234567890':
        return 1

    elif str(number + 2) in '1234567890':
        return 1


    # The digits are sequential, decrementing: 4321 (0 should come after 1, and not before 9, as in 3210)
    elif str(number + 1) in '9876543210':
        return 1

    elif str(number + 2) in '9876543210':
        return 1


    # The digits are a palindrome: 1221 or 73837
    elif number + 1 == int(''.join(reversed(str(number + 1)))):
        return 1

    elif number + 2 == int(''.join(reversed(str(number + 2)))):
        return 1


    # The digits match one of the values in the awesome_phrases array
    elif number + 1 in awesome_phrases:
        return 1

    elif number + 2 in awesome_phrases:
        return 1

    else:
        return 0


#  Solution 2

def is_incrementing(number): return str(number) in '1234567890'
def is_decrementing(number): return str(number) in '9876543210'
def is_palindrome(number):   return str(number) == str(number)[::-1]
def is_round(number):        return set(str(number)[1:]) == set('0')

def is_interesting(number, awesome_phrases):
    tests = (is_round, is_incrementing, is_decrementing,
             is_palindrome, awesome_phrases.__contains__)
       
    for num, color in zip(range(number, number+3), (2, 1, 1)):
        if num >= 100 and any(test(num) for test in tests):
            return color
    return 0


#  Solution 3

def is_interesting(number, awesome_phrases):
    for i in [number, number+1, number+2]:
        if i<100 :
            continue
        j=str(i)
        if any([
            i in awesome_phrases,
            all([j[x]=='0' for x in range(1,len(j))]),
            all([j[x]==j[0] for x in range(1,len(j))]),
            j == j[::-1],
            j in '1234567890',
            j in '9876543210'
                ]):
            return 2-bool(number-i)
    return 0

#  Solution 4

def is_interesting(number, awesome_phrases):
    for r, num in zip((2, 1, 1), range(number, number + 3)):
        num_str = str(num)
        if num in awesome_phrases or num > 99 and (int(num_str[1:]) == 0 or num_str[::-1] == num_str or num_str in '1234567890' or num_str in '9876543210'):
            return r
    return 0




# Number of trailing zeros of N!

'''
Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 * 2 * 3 * ... * N

Be careful 1000! has 2568 digits...

For more info, see: http://mathworld.wolfram.com/Factorial.html

Examples
zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros
Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros.
'''

def zeros(n):
    divisors=[]
    div = 5
    result = 0
    if n >= 5:
        while (div <= n):
            divisors.append(div)
            div = div*5
        for i in divisors:
            result = result + n//i
    return result

# Solution 2

def zeros(n):
  x = n//5
  return x+zeros(x) if x else 0 

# Solution 3

def zeros(n):
    zeros = 0
    i = 5
    while n//i > 0:
        zeros += n//i
        i*=5
    return zeros

# Solution 4

def zeros(n):
    result = 0
    while n != 0:
        result += n / 5
        n = n / 5
    return result

# Solution 5
def zeros(n):
    return n/5 + zeros(n/5) if n >= 5 else 0
