#CODE SCRIPT THAT READ FULL NAME OF A PERSON AND SHOW:
# - the name with all letters uppercase
# - the name with all letters lowercase
# - how mutch letters contains full name 
# - how mutch letters contains first name

name = input('Type you full name: ').strip()

print(f'UPPERCASE: {name.upper()}')
print(f'LOWERCASE: {name.lower()}')
print(f'LENGTH FULL NAME: {len(name)}')
print('LENGTH FIRST NAME: {0}'.format(len(name.split(' ')[0])))
