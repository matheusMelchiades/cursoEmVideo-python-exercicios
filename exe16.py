#CREATE SCRIPT THAT READ ANY REAL NUMBER AND SHOW YOUR ENTIR    ES PORTION
from math import floor

real = float(input('Type a real number: '))

print(f'The real number {real} has a portion entire of {floor(real)}')