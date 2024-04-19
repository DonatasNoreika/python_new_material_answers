def add_string(strings: list[str]) -> list[str]:
    new_strings = []
    for string in strings:
        new_strings.append(string + "_string")
    return new_strings


my_strings = ["Programming", "School", "Code", "Academy"]

print(add_string(my_strings))
