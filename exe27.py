# CODE SCRIPT THAT READ FULL NAME OF A PERSON AND SHOW
# YOUR FIRST NAME AND LAST NAME

name = input('Type your name: ').strip()

name = name.split(' ')
size = len(name)
print('FIRST NAME: {0}'.format(name[0]))
print('LAST NAME: {0}'.format(name[size - 1]))
