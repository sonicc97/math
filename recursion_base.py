def main():

    message(5)
 
def message(times):
    if times > 0:
     print('This is a recursive function!')
     message(times - 1)
 
#Call the main function
main()


#This program has a recursive function.
 
def main():
# By passing the argument 5 to the message function we are telling it to display the message five times
# This program also has print before and after to see the order of recurcive returns
  message(5)
 
def message(times):
    print(f'This is start of the {times}-th instance of the recursive funcion.')
    if times > 0:
        print('This is a recursive function. ')
        message(times - 1)
    print(f'This is end of the {times}-th instance of the recursive funcion.')
 
#Call the main function.

main()


#This program uses recursion to find the GCD of two numbers.
 
def main():
    #Get two numbers.
    num1 = int(input('Enter an integer: '))
    num2 = int(input('Enter another integer: '))
 
    #Display the GCD.
    print(f'The greatest common divisor of ' f'the two numbers is {gcd(num1, num2)}.')
 
    #The gcd function returns the greatest common
    #divisor of two numbers.
def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(x, x % y)
 
#Call the main function.

main()