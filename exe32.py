# CODE SCRIPT THAT READ A YEAR
# AND PRINT IF HER IS BISSEXTILE

year = int(input('Type a year:  '))

if (year % 100 != 0) and (year % 4 == 0) or (year % 400 == 0):
    print('This year is bissextile!')
else:
    print("This year isn't bissextile")
