sentence = input("Enter the sentence:")
words = sentence.split()
words.sort(key=len)
print(" ".join(words))
