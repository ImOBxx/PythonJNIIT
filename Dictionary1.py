myFile = open("mytestFile.txt", "r")
textData = myFile.read()
textData = textData.replace(",", "")
textData = textData.replace(".", "")
words = textData.split(" ")
print()
print(words)
print()
wordsDictionary = {}
for word in words:
    wordsDictionary[word] = words.count(word)

print(wordsDictionary)

