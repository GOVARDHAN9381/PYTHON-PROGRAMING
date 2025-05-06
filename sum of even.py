a = int(input("Enter the number of numbers: "))
b = list(map(int, input("Enter the numbers separated by space: ").split()))
even = 0
odd = 0
for i in range(0, a):
    if b[i] % 2 == 0:
        even += b[i] 
    else:
        odd += b[i]   
print("Sum of even numbers:", even)
print("Sum of odd numbers:", odd)
