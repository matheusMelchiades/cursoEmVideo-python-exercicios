#CREATE SCRIPT THAT READ THE HEIGHT AND WIDTH OF A WALL IN METERS, AND CALCULATE YOUR AREA
#AND QUANTITY OF INK NECESSERY TO PINT THE WALL
#CONSIDER: 2m² = 1liter

height = float(input('type height: '))
width = float(input('type width: '))

print(f'Total Ink: {int(height * width)}')