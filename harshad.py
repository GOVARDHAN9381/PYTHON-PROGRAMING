a = int(input('Enter the number: '))
x = a 
sum = 0

while x > 0:
    digit = x % 10
    sum += digit
    x = x // 10

if a % sum == 0:
    print('It is a Harshad number')
else:
    print('It is not a Harshad number')
