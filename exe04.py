# CREATE SCRIPT THAT READ SOMETHING
# AND PRINT YOURS PRIMITIVE TYPE INFOS

x = input('Type it something: ')

print(f'Is numberic: {x.isnumeric()}')
print(f'Is alpha: {x.isalpha()}')
print(f'Is decimal: {x.isdecimal()}')
print(f'Is digit: {x.isdigit()}')