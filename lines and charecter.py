
text = input("Enter a string: ")
num_characters = len(text)
words = text.split()
num_words = len(words)
num_lines = text.count('\n')+1
print("Number of characters:", num_characters)
print("Number of words:", num_words)
print("Number of lines:", num_lines)
