#CREATE SCRIPT THAT READ THE PRICE OF A PRODUCT AND SHOW
#NEW PRICE WITH 5% OFF

price = float(input('Type a price: '))

print(f'Total: {(price - (price * 0.05)):.4}')