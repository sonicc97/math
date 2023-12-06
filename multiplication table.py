def checking_the_multiplication_table(number_of_attempts):
    first = int(input("Enter the first number:"))
    second = int(input("Enter the second number"))
    for i in range(number_of_attempts):
        number1 = first
        number2 = second
        result = number1 * number1

        answer = int(input(f'How much is it {number1} x {number2}? '))

        if answer == result:
            print("Correct")
        else:
            print("Incorrectly")


checking_the_multiplication_table(1)
