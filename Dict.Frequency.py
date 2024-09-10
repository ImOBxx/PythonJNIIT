sentence = input ("Enter a sentence: ")
sentence = ''.join(char for char in sentence if char.isalnum() or char.isspace()).lower()
print(sentence)
words = sentence.split()
print(words)
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

sorted_frequency = dict(sorted(frequency.items()))

for word, count in sorted_frequency.items():
    print(f"{word}: {count}")