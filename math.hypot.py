import math
def hypotenuse():
    a = float(input("Enter the length of the first leg:"))
    b = float(input("Enter the length of the second leg:"))
    c = math.hypot(a,b)
    print(f'The length of the hypotenuse is {c}')
hypotenuse()

#SQUARE ROOT
import math
def root():
    check = float(input('Enter the root:'))
    number_check = math.sqrt(check)
    print(f'The square root of a number {check} is {number_check}')
root()
