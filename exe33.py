# CODE SCRIPT READ THREE NUMBER AND PRINT
# THE LESSER NUMBER AND BIGGER NUMBER

n1 = int(input('Type a fist number: '))
n2 = int(input('Type a Second number: '))
n3 = int(input('Type a third number: '))

# LESSER
if n1 < n2 and n1 < n3:
    lesser = n1
if n2 < n1 and n2 < n3:
    lesser = n2
if n3 < n1 and n3 < n2:
    lesser = n3

# BIGGER
if n1 > n2 and n1 > n3:
    bigger = n1
if n2 > n1 and n2 > n3:
    bigger = n2
if n3 > n1 and n3 > n2:
    bigger = n3

print(f'{lesser} is the lesser number')
print(f'{bigger} is the bigger number')
