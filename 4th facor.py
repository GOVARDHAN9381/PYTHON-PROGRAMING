x=int(input('enter the number'))
y=[]
print('the factors are')
for i in range(1,x):
    if x%i==0:
        y.append(i)
print(y)
print('number of factors',len(y))
n=int(input('enter the n value'))
if n>len(y):
    print('invalid')
else:
    print(n,'th factor is',y[n-1])