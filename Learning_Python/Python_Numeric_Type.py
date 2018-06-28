# Chapter 5
# Numeric Types

# Mixed types are converted up
print(40 + 3.14)        # Integer to float, float math/result
print(int(3.1415))      # Truncates float to integer
print(float(3))         # Converts integer to float

a = 3                   # Name created: not declared ahead of time
b = 4
print(a+1, a-1)         # Addition (3 + 1), subtraction (3 − 1)
print(b*3, b/2)         # Multiplication (4 * 3), division (4 / 2)
print(a%2, b**2)        # Modulus (remainder), power (4 ** 2)
print(2+4.0, 2.0**b)    # Mixed-type conversions

print(b/2+a)            # Same as ((4 / 2) + 3) [use 2.0 in 2.X]
print(b/(2.0+a))        # Same as (4 / (2.0 + 3)) [use print before 2.7]

# Numeric Display Formats
num = 1/3.0
print(num)              # Auto-echoes
print('%e' % num)       # String formatting expression
print('%4.2f' % num)    # Alternative floating-point format
print('{0:4.2f}'.format(num))   # String formatting method: Python 2.6, 3.0, and later

# str and repr Display Formats
print(repr('spam'))     # Used by echoes: as-code form
print(str('spam'))      # Used by print: user-friendly form

# Comparisons: Normal and Chained
print(1 < 2)    # Less than
print(2.0 > 1)  # Greater than or equal: mixed-type 1 converted to 1.0
print(2.0 == 2.0)   # Equal value
print(2.0 != 2.0)   # Not equal value

X = 2
Y = 4
Z = 6
print(X<Y<Z)    # Chained comparisons: range tests
print(X<Y and Y<Z)

print(X<Y>Z)
print(X < Y and Y > Z)
print(1 < 2 < 3.0 < 4)
print(1 > 2 > 3.0 > 4)

print(1 == 2 < 3)       # Same as: 1 == 2 and 2 < 3
                        # Not same as: False < 3 (which means 0 < 3, which is true!)
print(1.1 + 2.2 == 3.3)        # Shouldn't this be True?...
print(1.1 + 2.2)         # Close to 3.3, but not exactly: limited precision
print(int(1.1+2.2) == int(3.3))         # OK if convert: see also round, floor, trunc ahead
                                        # Decimals and fractions (ahead) may help here too





