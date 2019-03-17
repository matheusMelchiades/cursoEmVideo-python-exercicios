#CREATE SCRIPT THAT READ A VALUE IN METERS AND PRINT IN CENTIMETERS AND MM

value = float(input('Type it the meters: '))

print(f'METERS: {value}')
print(f'CENTIMETERS: {value * 100}')
print(f'MM: {value * 1000}')