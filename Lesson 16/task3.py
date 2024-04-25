import random_word

words = random_word.Wordnik()
random_words = words.get_random_words(limit=5)
result = sorted(word.title() for word in random_words)
print(result)
