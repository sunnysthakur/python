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


