import math
def hypotenuse():
    a = float(input("Enter the length of the first leg:"))
    b = float(input("Enter the length of the second leg:"))
    c = math.hypot(a,b)
    print(f'The length of the hypotenuse is {c}')
hypotenuse()
