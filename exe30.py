#CODE SCRIPT THAT READ A NUMBER AND PRINT IF 
# IS PAR OR IMPAR

number = int(input('Type a number: '))
print(f'Your number is {"PAR" if number % 2 == 0 else "IMPAR"}')