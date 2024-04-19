sentence = "Hello john.doe@example.com $%gfgdf55@@@@fds2424 This is a test jane.doe@example.com Goodbye test.email@example.org"


def extract_email_addresses(text: str) -> list[str]:
    addresses = []
    splited_text = text.split()
    for word in splited_text:
        if "@" in word:
            addresses.append(word)
    return addresses


print(extract_email_addresses(sentence))

# Alternative with RegEx:
import re

test_string = "Hello john.doe@example.com $%gfgdf55@@@@fds2424 This is a test jane.doe@example.com Goodbye test.email@example.org"


def extract_email_addresses(string):
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(email_regex, string)


print(extract_email_addresses(test_string))
