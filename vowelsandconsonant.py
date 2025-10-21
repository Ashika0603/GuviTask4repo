sentence = input("Enter the sentence:")
vowels = "aeiou"
vowel_count = 0
consonant_count =0
for char in sentence.lower():
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
print("vowel count:",vowel_count,"consonant count:",consonant_count)