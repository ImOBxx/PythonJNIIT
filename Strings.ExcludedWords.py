
excluded_words = {'this', 'and', 'is', 'not', 'etc.'}

sentence = input("Enter a sentence: ")

words = sentence.split()

# Initialize a list to store unique non-excluded words
unique_non_excluded_words = []

# Iterate over each word in the sentence
for word in words:
    # Check if the word is not in the set of excluded words
    if word.lower() not in excluded_words:
        # Check if the word is not already in the list of unique non-excluded words
        if word.lower() not in unique_non_excluded_words:
            # Add the word to the list of unique non-excluded words
            unique_non_excluded_words.append(word.lower())

# Display the unique non-excluded words
print("Unique non-excluded words in the sentence:")
for word in unique_non_excluded_words:
    print(word)
