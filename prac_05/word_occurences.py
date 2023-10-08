"""
Word Occurrences
Estimate: 60 minutes
Actual:
"""

phrase = input("Enter a string: ").split()

words = []
for word in phrase:
    if word in phrase and word not in words:
        words.append(word)

max_width = max([len(word) for word in words])

counts = [0 for i in range(len(words))]
word_to_count = dict(zip(sorted(words), counts))

for word in phrase:
    if word in word_to_count:
        word_to_count[word] += 1

for word in word_to_count:
    print(f"{word:{max_width}}: {word_to_count[word]}")
