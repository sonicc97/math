def call_name():
    name_1 = str(input('Say your name?'))
    name_2 = str(input('Write your last name?'))
    names = (f'Your first name {name_1}, and your last name {name_2}.')
    print(names)
call_name()
def difference():
    math = int(input('How old are you?'))
    math1 = int(input('How old is your wife?'))
    print(f'You have {math} years and your wife is {math1} years old!')
    difference = math - math1
    print(f'The age difference is {difference}')
difference()
