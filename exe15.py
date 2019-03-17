#CODE SCRIPT THAT READ THE QUANTITY OF KM PERCURRED FOR ONE 
#RENTED CAR AND THE QUANTITY OF DAYS THAT RENTED, 
#CALCULATE TOTAL PRICE.
#CONSIDER R$60 FOR DAY AND R$0.15 FOR KM

km = int(input('Type km percurred: '))
days = int(input('Type days to be rented: '))

print(f'Total a pay: R${float((km * 60) + (days * 0.15)):2}')
