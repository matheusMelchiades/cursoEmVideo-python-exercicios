#CREATE SCRIPT THAT READ THE SALARY OF A FUNCTIONARY AND SHOW 
# YOUR NEW SALARY WITH 15% INCREASE 

salary = float(input('Type you salary: '))

print(f'New Salary: {(salary + (salary * 0.15))}')