
def load_text(text):
    word_frequency = {}
    words = text.split()
    for word in words:
        word = word.lower()
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    return word_frequency


def sorted_word_frequencies(word_frequency):
    return sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)


def words_occurred_more_than_once(word_frequency):
    return [word for word, frequency in word_frequency.items() if frequency > 1]


text = "This is a sample text. This text contains sample words for demonstration purposes. This text will be used to test the program."


word_frequency = load_text(text)


sorted_words_with_frequencies = sorted_word_frequencies(word_frequency)

words_more_than_once = words_occurred_more_than_once(word_frequency)


print("Sorted list of words with their frequencies:")
for word, frequency in sorted_words_with_frequencies:
    print(f"{word}: {frequency}")

print("\nList of words which have occurred more than once:")
print(words_more_than_once)
