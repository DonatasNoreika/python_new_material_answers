# version 1:

sentence = input("Enter sentence: ")

sent_info = {}

for char in sentence:
    char_number = sentence.count(char)
    # print(char, char_number)
    sent_info[char] = char_number

print(sent_info)

# version 2:

from collections import Counter

sentence = input("Enter sentence: ")

print(dict(Counter(sentence)))

# version 3:

sentence1 = input("Enter sentence: ")
sentence2 = input("Enter sentence: ")
sentence3 = input("Enter sentence: ")

full_sentence = sentence1 + sentence2 + sentence3

sent_info = {}

for char in full_sentence:
    char_number = full_sentence.count(char)
    # print(char, char_number)
    sent_info[char] = char_number

print(sent_info)

# version 4:

full_sentence = ""

for x in range(3):
    sentence = input("Enter sentence: ")
    full_sentence += sentence

sent_info = {}

for char in full_sentence:
    char_number = full_sentence.count(char)
    # print(char, char_number)
    sent_info[char] = char_number

print(sent_info)
