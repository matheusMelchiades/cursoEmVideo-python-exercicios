# CODE SCRIPT THAT READ A PHRASE AND SHOW:
# - how mutch times does it appear the letter A
# - which position does it appear the first time
# - which position does it appear the last time

phrase = input('Type something: ').lower().strip()

size = len(phrase)
print('HOW MUTCH TIMES: {0}'.format(phrase.count('a')))
print('FIRST POSITION: {0}'.format(phrase.find('a')))
print('LAST POSITION: {0}'.format(phrase.rfind('a')))
