n=5
for i in range(n,0,-1):
    p=65
    for j in range(i):
        print(chr(p),end=" ")
        p+=1
    print()