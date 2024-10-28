"""
Word Occurrences
Estimate: 30 minutes
Actual:   21 minutes

get text
words = split text
word_count = empty dictionary
for word in words
    if word in word_count
        word_count[word] = word_count[word] + 1
    else
        word_count[word] = 1
max_length = get max length in word_count
for word, count in items of word_count after sorted
    display word, count
"""

text = input("Enter the text: ")
words = text.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
        word_count[word] = 1

# Find the max length word in text
max_length = len(max(word_count.keys()))

for word, count in sorted(word_count.items()):
    print(f"{word:{max_length}} : {count}")
