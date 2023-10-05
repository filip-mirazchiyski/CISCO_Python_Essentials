word = input()
word = word.upper()

for letter in word:
    if letter == "A" or letter == "E" or letter == "O" or letter == "U" or letter == "I":
        continue
    else:
        print(letter)
