a=int(input('enter the number'))
original=a
sum=0
while a!=0:
    digit=a%10
    sum+=digit**3
    a=a//10
if sum==original:
    print('it is armstrong number')
else:
    print('it is not a armstrong')