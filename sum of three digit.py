num=int(input('Enter the number:'))
Sum=0

while num>0:
    digit=num%10
    Sum+=digit
    num=num//10
print('Sum of Digits:', Sum)