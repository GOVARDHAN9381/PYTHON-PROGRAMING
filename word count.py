
sentence = input("Enter a sentence: ")
words = sentence.lower().split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print("Word occurrences:")
print(f"{word_count}")
