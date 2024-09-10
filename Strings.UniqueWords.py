sentence = input("Enter a sentence: ")
words = sentence.split()
unique_words = set(words)
print("Unique words in the sentence:")
for word in unique_words:
    print(word)
