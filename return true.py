def is_palindrome_integer(x):
    if not isinstance(x, int):
        return False
    if x < 0:
        return False
    x_str = str(x)
    return x_str == x_str[::-1]
test_inputs = [121, -121, 10, "abc", 0]
for value in test_inputs:
    result = is_palindrome_integer(value)
    print(f"Input: {value} → Output: {result}")
