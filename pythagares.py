x=int(input('enter the number'))
for a in range(1,x+1):
    for b in range(1,x+1):
        for c in range(1,x+1):
            if a*a+b*b==c*c:
                print(f'the numbers are {a},{b},{c}')