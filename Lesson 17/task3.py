class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def get_title(self):
        return f"Pavadinimas: {self.name}"

    def get_author(self):
        return f"Autorius: {self.author}"


pride_and_prejudice = Book("Pride and Prejudice", "Jane Austen")
hamlet = Book("Hamletas", "Viljamas Šekspyras")
war_and_peace = Book("Karas ir taika", "Levas Tolstojus")
harry_potter = Book("Haris Poteris", "J. K. Rowling")

print(hamlet.get_title())
print(hamlet.get_author())
