"""
Word Occurences
Estimate: 60 minutes
Actual:
"""

phrase = input("Enter a string: ").split()
words = []
for word in phrase:
    if word in phrase and word not in words:
       words.append(word)

