def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = " ".join(reversed_words)
    return reversed_sentence


sentence = "A CAT RAN"
reversed_sentence = reverse_sentence(sentence)
print(reversed_sentence)

