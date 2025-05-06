# Get input using list data type
inputs = list(map(int, input("Enter M, N, K separated by spaces: ").split()))
M, N, K = inputs[0], inputs[1], inputs[2]
if M <= N:
    for num in range(M, N + 1, K + 1):
        print(num, end=", ")
