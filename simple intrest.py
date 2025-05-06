p=int(input('enter the principal amount '))
y=int(input('enter the years'))
c=input('enter is customer senoir{Y/N}')
g=input('enter {M/F}')
if c=='Y' and g=='M':
    si=p*y*12/100
    print(si)
elif c=='n' and g=='f':
    si=p*y*15/100
    print(si)
else:
    si=p*y*10/100
    print(si)