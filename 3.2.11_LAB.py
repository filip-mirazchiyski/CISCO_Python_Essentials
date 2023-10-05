word = input()
word = word.upper()
word_without_vowels = ""

for letter in word:
    if letter == "A" or letter == "E" or letter == "O" or letter == "U" or letter == "I":
        continue
    else:
        word_without_vowels += letter
print(word_without_vowels)
