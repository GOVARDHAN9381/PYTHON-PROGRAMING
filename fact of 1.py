import math
n=int(input('enter the number'))
sum=1
for i in range(1,n+1):
    sum+=1/math.factorial(i)
print()
print(sum)
