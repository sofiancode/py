class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def print_info(self):
        print(f"{self.title} is written by {self.auther}")
