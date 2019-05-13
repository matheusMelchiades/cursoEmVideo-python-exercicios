# CODE SCRIPT THAT READ A DISTANCE IN KM 
# AND RETURN THE PRICE WITH YOUR TAXES
# - R$ 0.50 by KM <= 200 km
# - R$ 0.45 by KM > 200 KM

distance = float(input('Type a distance: '))

if distance <= 200:  
    price = distance * 0.50
else:   
    price = distance * 0.45

print (f'Price total: R${price}')