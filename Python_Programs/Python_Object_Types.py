print(123 + 222)    # Integer addition
print(1.5*4)        # Floating-point multiplication
print(2**100)       # 2 to the power 100, again

print(len(str(2**1000000)))     # How many digits in a really BIG number?

print(3.1415*2)     # repr: as code (Pythons < 2.7 and 3.1) & str: user-friendly

#Using inbuilt math module
import math
print(math.pi)
print(math.sqrt(85))

#Using inbuilt random module
import random
print(random.random())              #Print random values
print(random.choice([1, 2, 3, 4]))  #Print random values from list

#String Operations
S = 'spam'          # Make a 4-character string, and assign it to a name
print(len(S))       # Length

print(S[0])         # The first item in S, indexing by zero-based position
print(S[1])         # The second item from the left

print(S[-1])        # The last item from the end in S
print(S[-2])        # The second-to-last item from the end

print(S[len(S)-1])  # Negative indexing, the hard way

#Slicing in Strings
print(S)            # A 4-character string

print(S[1:3])       # Slice of S from offsets 1 through 2 (not 3). offsets 1 through 2 (that is, 1 through 3 – 1)

print(S[1:])        # Everything past the first (1:len(S))
print(S[0:3])       # Everything but the last
print(S[:3])        # Same as S[0:3]
print(S[:-1])       # Everything but the last again, but simpler (0:-1)
print(S[:])          # All of S as a top-level copy (0:len(S))













