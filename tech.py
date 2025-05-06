n = int(input('Enter the number: '))
x = n  
num_str = str(n)
length = len(num_str)

if length % 2 == 0:
    half = length // 2
    first_half = int(num_str[:half])
    second_half = int(num_str[half:])
    if (first_half + second_half) ** 2 == x:
        print(x, 'is a tech number')
    else:
        print(x, 'is not a tech number')
else:
    print(x, 'is not a tech number')  