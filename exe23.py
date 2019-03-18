# CODE SCRIPT THAT READ A NUMBER BETWEEN 0 AND 9999 AND SHOW
# EACH ONE OF THEM

number = input('Type a number').strip()
size = len(number)

print(f'UNITY: {number[size - 1:size]}')
print(f'TEN: {number[size - 2:size - 1 ]}')
print(f'HUNDRED: {number[size - 3:size - 2]}')
print(f'THOUSAND: {number[size - 4:size -3]}')
