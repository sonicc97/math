#Add the missing flight code 
flights = ['1122', '5788', '8879']
codes_a = ['CAN' + flight for flight in flights]
print(codes_a)

codes_b = []
for flight in flights:
    code = 'BC' + flight
    codes_b.append(code)
    print(codes_b)


#Calculation
prices = [10, 20, 35, 48, 60]

def halve(air):
    no_tax = 3 * air
    return no_tax/2

halved = [halve(price) for price in prices]
print(halved)


#Check how many duplicate letters there are
words = ['apple', 'banana', 'strawberry', 'raspberry', 'pineapple', 'orange']

def has_double_a (word):
    count = word.count('a')
    return count == 1
double_a = [has_double_a(word) for word in words]
print(double_a)

#We check the number if it is greater or less than the desired number
points = [95, 80, 73, 92, 102, 55]

def check_under (number):
    checking = number + 10
    return checking > 100

under_100 = [check_under(number) for number in points]
print(under_100)

#Checking between the desired numbers
checking = [20, 70, 83, 42, 12, 39, 55, 120, 88]

ideal = [number for number in checking if number >= 30 and number <= 50]
print(ideal)
