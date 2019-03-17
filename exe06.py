# CREATE SCRIPT THAT READ A NUMBER AND PRINT THE DOUBLE, THE TRIPLE AND SQUARE ROOT
from math import sqrt

number = int(input('Type it a number: '))

print(f'DOUBLE: {number * 2}')
print(f'TRIPLE: {number * 3}')
print(f'SQUARE ROOT: {sqrt(number):.3}')
