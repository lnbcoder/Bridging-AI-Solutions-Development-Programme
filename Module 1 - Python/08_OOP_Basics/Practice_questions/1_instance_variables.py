# Create a class Book with:
# - title
# - author
# Add a method describe() that prints:
# "<title> by <author>"
# 👉 Create two different books and call describe() on both.

class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        print(f"{self.title} by {self.author}")

book1 = Book("The mountain is you", "Brianna Wiest")
book2 = Book("Atomic Habits", "James Clear")

book1.describe()
book2.describe()