n=int(input('Enter the number:'))
a=n
while a>=10:
    sum=0
    while a!=0:
        digit=a%10
        sum=digit**2+sum
        a=a//10
    a=sum
if sum==1:
    print('True')
else:
    print('False')