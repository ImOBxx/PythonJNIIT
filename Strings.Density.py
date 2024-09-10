
excluded_words = {'this', 'and', 'is', 'not', 'etc.'}

sentence = input("Enter a long sentence: ")

words = sentence.split()


filtered_words = [word.lower() for word in words if word.lower() not in excluded_words]

total_words = len(filtered_words)


word_frequency = {}

for word in filtered_words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

print("Density of each word in the sentence:")
for word, frequency in word_frequency.items():
    density = frequency / total_words
    print(f"{word}: {round(density)}")
