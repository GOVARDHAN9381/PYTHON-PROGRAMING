sentences = [
    "I love Python",
    "This is a longer sentence than the first",
    "Short one",
    "This is the sentence with the most words in it perhaps"
]
max_words = 0

for sentence in sentences:
    word_count = len(sentence.split())
    if word_count > max_words:
        max_words = word_count
print("Maximum number of words in a sentence:", max_words)
