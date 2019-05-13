# CODE SCRIPT SORT A NUMBER AND USER SHOULD
# ASSERT A NUMBER 
from random import randint

SORTED = randint(0, 5)
choose = int(input('Choose a number between 1 and 5:  '))

if SORTED == choose: 
    print('Congrats you are winner!!')
else: 
    print('HMMM! TRY AGAIN!')