print(123 + 222)  # Integer addition
print(1.5 * 4)  # Floating-point multiplication
print(2 ** 100)  # 2 to the power 100, again

print(len(str(2 ** 1000000)))  # How many digits in a really BIG number?

print(3.1415 * 2)  # repr: as code (Pythons < 2.7 and 3.1) & str: user-friendly

# Using inbuilt math module
import math

print(math.pi)
print(math.sqrt(85))

# Using inbuilt random module
import random

print(random.random())  # Print random values
print(random.choice([1, 2, 3, 4]))  # Print random values from list

# String Operations
S = 'spam'  # Make a 4-character string, and assign it to a name
print(len(S))  # Length

print(S[0])  # The first item in S, indexing by zero-based position
print(S[1])  # The second item from the left

print(S[-1])  # The last item from the end in S
print(S[-2])  # The second-to-last item from the end

print(S[len(S) - 1])  # Negative indexing, the hard way

# Slicing in Strings
print(S)  # A 4-character string

print(S[1:3])  # Slice of S from offsets 1 through 2 (not 3). offsets 1 through 2 (that is, 1 through 3 – 1)

print(S[1:])  # Everything past the first (1:len(S))
print(S[0:3])  # Everything but the last
print(S[:3])  # Same as S[0:3]
print(S[:-1])  # Everything but the last again, but simpler (0:-1)
print(S[:])  # All of S as a top-level copy (0:len(S))

# Concatenation in Strings
print(S + 'xyz')  # Concatenation
print(S * 8)  # Repetition

# Immutability [Numbers, Strings and tupples are immutables where as list and dictionaries isn't
# S[0] = 'z'  # Immutable objects cannot be changed
T = 'hello'
T = 'z' + T[1:]  # But we can run expressions to make new objects
print(T)

# Lists Operations
U = 'shrubbery'
L = list(U)  # Expand to a list: [...]
print(L)
L[1] = 'c'  # Change it in place
print(''.join(L))  # Join with empty delimiter

B = bytearray(b'sunnys.thakur')  # A bytes/list hybrid (ahead)
B.extend(b'@gmail.com')  # 'b' needed in 3.X, not 2.X
print(B)  # B[i] = ord(c) works here too
print(B.decode())  # Translate to normal string

# Type Specific Methods
S = 'Welcome'
print(S.find('come'))
print(S.replace('come', 'done'))

# Type Specific Methods 2
line = 'aaa,bbb,ccccc,dd'
print(line.split(','))  # Split on a delimiter into a list of substrings

S = 'python'
print(S.upper())  # Upper- and lowercase conversions
print(S.isalpha())  # Content tests: isalpha, isdigit, etc.

line = 'xxx,yyy,zzzzz,oo\n'
print(line.rstrip())  # Remove whitespace characters on the right side

print(line.rstrip().split(','))  # Combine two operations

# String Formatting
print('%s, eggs, and %s' % ('spam', 'SPAM!'))  # Formatting expression (all)
print('{0}, eggs, and {1}'.format('spam', 'SPAM!'))  # Formatting method (2.6+, 3.0+)
print('{}, eggs, and {}'.format('spam', 'SPAM!'))  # Numbers optional (2.7+, 3.1+)

print('{:,.2f}'.format(296999.2567))  # Separators, decimal digits
print('%.2f|%+05d' % (3.14159, -42))  # Digits, padding, signs

# Getting Help
print(dir())
print(dir(S))

# double underscores
print(S + 'IN!')
print(S.__add__('IN!'))

# Help function
print(help(S.replace))

# Other Ways to Code Strings
S = 'A\nB\tC'  # \n is end-of-line, \t is tab
print(len(S))  # Each stands for just one character
print(ord('\n'))  # \n is a byte with the binary value 10 in ASCII

Y = 'A\0B\0C'  # \0, a binary zero byte, does not terminate string.
print(len(Y))

print(
    Y)  # Non-printables are displayed as \xNN hex escapes (not clear). Output differ here and in Python command line ('A\x00B\x00C')

# Output differ here and in Python command line. Output (\naaaaaaaaaaaaa\nbbb\'\'\'bbbbbbbbbb""bbbbbbb\'bbbb\ncccccccccccccc\n')
msg = """                           
aaaaaaaaaaaaa
bbb'''bbbbbbbbbb""bbbbbbb'bbbb
cccccccccccccc
"""
print(msg)

# Unicode Strings
print('sp\xc4m')  # 3.X: normal str strings are Unicode text
print(b'a\x01c')  # bytes strings are byte-based data
print(u'sp\u00c4m')  # The 2.X Unicode literal works in 3.3+: just str)

print(u'sp\xc4m')  # 2.X: Unicode strings are a distinct type
print('a\x01c')  # Normal str strings contain byte-based text/data
print(b'a\x01c')  # The 3.X bytes literal works in 2.6+: just str

print('spam')  # Characters may be 1, 2, or 4 bytes in memory
print('spam'.encode('utf8'))  # Encoded to 4 bytes in UTF-8 in files
print('spam'.encode('utf16'))  # But encoded to 10 bytes in UTF-16

print('\u00A3', '\u00A3'.encode('latin'), b'\xA3'.decode('latin'))

# print(u'x' + b'y')      # Works in 2.X (where b is optional and ignored)
# print(u'x' + 'y')       # Works in 2.X: u'xy'
# print(u'x' + b'y')      # Fails in 3.3 (where u is optional and ignored)
# print(u'x' + 'y')       # Works in 3.3: 'xy'
# print('x' + b'y'.decode())  # Works in 3.X if decode bytes to str: 'xy'
# print('x'.encode() + b'y')  # Works in 3.X if encode str to bytes: b'xy'

# Pattern Matching
import re

match = re.match('Hello[\t]*(.*)world', 'Hello   Python world')
print(match.group(1))

match = re.match('[/:](.*)[/:](.*)[/:](.*)', '/usr/home:lumberjack')
print(match.groups())

print(re.split('[/:]', '/usr/home/lumberjack'))

# Sequence Operations (Lists)
L = [123, 'spam', 1.23]  # A list of three different-type objects
print(len(L))  # Number of items in the list
print(L[0])  # Indexing by position
print(L[:-1])  # Slicing a list returns a new list
print(L + [4, 5, 6])  # Concat/repeat make new lists too
print(L)  # We're not changing the original list

# Type-Specific Operations
L.append('NI')  # Growing: add object at end of list
print(L)

L.pop(2)  # Shrinking: delete an item in the middle
print(L)  # "del L[2]" deletes from a list too

M = ['bb', 'aa', 'cc']
M.sort()
print(M)

M.reverse()
print(M)

# Bounds Checking (Lists)
# print(L)
# print(L[99])

# Nesting
M = [[1, 2, 3],  # A 3 × 3 matrix, as nested lists
     [4, 5, 6],  # Code can span lines if bracketed
     [7, 8, 9]]
print(M)

print(M[1])  # Get row 2
print(M[1][2])  # Get row 2, then get item 3 within the row

# Comprehensions
col2 = [row[2] for row in M]  # Collect the items in column 2
print(col2)
print(M)  # The matrix is unchanged

print([row[1] + 1 for row in M])  # Add 1 to each item in column 2
print([row[1] for row in M if row[1] % 2 == 0])  # Filter out odd items

diag = [M[i][i] for i in [0, 1, 2]]  # Collect a diagonal from matrix
print(diag)

doubles = [c * 2 for c in 'spam']  # Repeat characters in a string
print(doubles)

print(list(range(4)))  # 0..3 (list() required in 3.X)
print(list(range(-6, 9, 2)))  # −6 to +6 by 2 (need list() in 3.X)
print([[x ** 2, x ** 3] for x in range(4)])  # Multiple values, "if" filters

print([[x, x / 2, x * 2] for x in range(-6, 7, 2) if x > 0])

G = (sum(row) for row in M)  # Create a generator of row sums
print(next(G))  # iter(G) not required here
print(next(G))  # iter(G) not required here
print(next(G))  # iter(G) not required here

print(list(map(sum, M)))  # Map sum over items in M
print({sum(row) for row in M})  # Create a set of row sums
print({i: sum(M[i]) for i in range(3)})  # Creates key/value table of row sums

print([ord(x) for x in 'spaam'])  # List of character ordinals
print({ord(x) for x in 'spaam'})  # Sets remove duplicates
print({x: ord(x) for x in 'spaam'})  # Dictionary keys are unique
print((ord(x) for x in 'spaam'))  # Generator of values

# Dictionaries
# Mapping Operations

D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
print(D)
print(D['food'])
D['quantity'] += 1
print(D)

D = {}
D['name'] = 'Bob'
D['job'] = 'dev'
D['age'] = '40'
print(D)
print(D['name'])

bob1 = dict(name='Bob', job='Dev', age=40)
print(bob1)

bob2 = dict(zip(['name', 'job', 'age'], ['bob', 'dev', 40]))  # Zipping
print(bob2)

# Nesting Revisited
rec = {'name': {'first': 'Bob', 'last': 'Smith'},
       'jobs': ['dev', 'mgr'],
       'age': 40.5}
print(rec)

print(rec['name'])                  # 'name' is a nested dictionary

print(rec['name']['last'])          # Index the nested dictionary

print(rec['jobs'])                  # 'jobs' is a nested list

print(rec['jobs'][-1])              # Index the nested list

rec['jobs'].append('janitor')       # Expand Bob's job description in place
print(rec)

rec = 0 # Now the object's space is reclaimed

# Missing Keys: if Tests
D = {'a': 1, 'b': 2, 'c': 3}
print(D)

D['e'] = 99         # Assigning new keys grows dictionaries
print(D)

#D['f'] # Referencing a nonexistent key is an error
#print(D)

print('f' in D)
if not 'f' in D:            # Python's sole selection statement
    print('missing')

if not 'f' in D:
    print('missing')
    print('no, really...')      # Statement blocks are indented

value = D.get('x', 0)           # Index but with a default
print(value)

value = D['x'] if 'x' in D else 0   # if/else expression form
print(value)

# Sorting Keys: for Loops
D = {'a': 1, 'b': 2, 'c': 3}
print(D)

Ks = list(D.keys())         # Unordered keys list
print(Ks)                   # A list in 2.X, "view" in 3.X: use list()
Ks.sort()                   # Sorted keys list
print(Ks)
for key in Ks:                  # Iterate though sorted keys
    print(key, '=>', D[key])    # <== press Enter twice here (3.X print)

for key in sorted(D):           # Sort the keys if not in order
    print(key, '=>', D[key])

for c in 'spam':
    print(c.upper())

# while loop 1
x = 1
while x <= 4:
    print('spam!' * x)
    x += 1

# while loop 2
x = 4
while x > 0:
    print('spam!' * x)
    x -= 1

# Iteration and Optimization
squares1 = [x ** 2 for x in [1, 2, 3, 4, 5]]
print(squares1)

squares2 = []
for x in [1, 2, 3, 4, 5]:           # This is what a list comprehension does
    squares2.append(x ** 2)         # Both run the iteration protocol internally
    print(squares2)

# Tuples
T = (1, 2, 3, 4)        # A 4-item tuple
print(len(T))           # Length

print(T + (5, 6))       # Concatenation

print(T[0])             # Indexing, slicing, and more

print(T.index(4))       # Tuple methods: 4 appears at offset 3
print(T.count(4))          # 4 appears once in tuple list

#T[0] = 2               Tuples are immutable
print((2,)+T[:1])       # Make a new tuple for a new value

T = 'spam', 3.0, [11, 22, 33]
print(T[1])
print(T[2][1])
#print(T.append(4))













