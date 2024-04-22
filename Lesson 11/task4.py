def starts_with_vowel(*args: str):
    vowels_list = []
    vowels = ('a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', "Y")
    for word in args:
        if word.startswith(vowels):
            vowels_list.append(word)

    return vowels_list


print(starts_with_vowel("Code", "Exception", "Loops", "Academy", "Python", "IF", "Indentation"))
