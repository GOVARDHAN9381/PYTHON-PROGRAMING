import math
x_deg = float(input("Enter the value of x in degrees: "))
n = int(input("Enter number of terms: "))
x = math.radians(x_deg)
cos_x = 0
for i in range(n):
    term = ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)
    cos_x += term
print(f"cos({x_deg}) ≈ {cos_x}")
