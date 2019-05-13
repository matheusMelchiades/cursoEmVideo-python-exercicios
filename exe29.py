# CODE A SCRIPT THAT SHOULD READ A VELOCITY IN KM
# AND PRINT , IF OVERCOME 80 KM, QUANTITY TOTAL OF TRAFFIC TICKET
# $ 7.00 FOR EACH KM

velocity = float(input('Type the velocity: '))
LIMIT =  80

if (velocity > LIMIT): 
    print('VELOCITY OVERCOME!')
    print(f'TRAFFIC TICKET: R$ {(velocity - LIMIT) * 7.00}')
else : 
    print('Velocity are inside limit')

