#CREATE SCRIPT THAT READ THE LENGTH OF THE OPPOSITE CATHETER
#AND THE ADJCENT CATHETER OF A RECTANGLE TRIANGLE, AND CALCULATE THE LENGTH OF HYPOTENUSE
from math import hypot

catOposto = float(input('Type the opposite catheter: '))
catAdjacente = float(input('Type the adjacent catheter: '))

print(f'Total length hypotenuse: {hypot(catOposto, catAdjacente):.3}')