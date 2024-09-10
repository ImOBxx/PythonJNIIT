def reverse_words(string):
    words = string.split()
    print(words)
    reversed_words = ' '.join(reversed(words))
    print(reversed_words )
    return reversed_words


input_string = "A CAT RAN"
reversed_string = reverse_words(input_string)
print(reversed_string)