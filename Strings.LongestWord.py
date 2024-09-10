sentence = input("Enter a sentence: ")
words = sentence.split()

longest_word = ""
max_length = 0

for word in words:
    if len(word) > max_length:
        max_length = len(word)
        longest_word = word

print("The longest word in the sentence is:", longest_word)

