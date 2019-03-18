# CODE SCRIPT THAT READ THE NAME OF A CITY
# AND SHOW IF START WITH "SANTO" OR NOT

city = input('Type a name: ')

print('START WITH SANTO: {0}'.format('santo' in city[0:5].lower()))
