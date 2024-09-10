def count_word_occurrences(string, word):
    string = ''.join(char for char in string if char.isalnum() or char.isspace()).lower()
    print(string)
    words = string.split()
    print(words)
    

    count = 0
    for w in words:
        if w == word:
            count += 1
    
    return count

input_string = "This is a test. This test is only a test."
input_word = "test"
print(f"The word '{input_word}' occurred {count_word_occurrences(input_string, input_word)} times in the string.")
