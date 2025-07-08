#Task 1: Calculate Factorial Using a Function 
from math import factorial

number = int (input("Enter The Number : "))
def factorial (number):
    if number < 2:
        return 1
    else:
        return number * (factorial (number-1))
result = factorial (number)

print(f"Factorial of the {number} is: ", result)
