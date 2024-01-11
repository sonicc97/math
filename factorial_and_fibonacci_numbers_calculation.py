# This program uses recursion to calculate the factorial of number
 
def main():
    # Get a number from the user.
    number = int(input('Enter a nonnegative integer: '))
 
    # Get the factorial of the number.
    fact = factorial(number)
 
    # Display the factorial.
    print(f'The factorial of {number} is {fact}.')
 
# The factorial function uses recursion to calculate the factorial of its argument which is assumed to be nonnegative.
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
 
# Call the main function.
main()




# This program uses recursion to print numbers from the Fibonacci series.
def main():
    end = int(input("Enter the number of element of the Fibonacci series: "))
    print(f'The first {end} numbers in the')
    print('Fibonacci series are:')
 
    for number in range(1, end+1):
        print(fib(number))
 
# The fib function returns the nth number in the Fibonacci series.
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1)  + fib(n - 2)
 
# Call the main function.
main()