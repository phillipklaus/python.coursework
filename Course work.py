class Book:
    def __init__(self,title,author,isbn,available = True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def get_info (self):
        return f"{self.title} by {self.author}. ISBN: {self.isbn}. Availability: {self.available}"
    def check_out(self):
        if self.available:
            self.available = False
            return True
        return False
    
class Fiction(Book):
    def __init__(self,title,author,isbn,genre,available = True):
        super().__init__(title,author,isbn,available)
        self.genre = genre
# bringing the get_ifo in this class is polymorphism
    def get_info(self):
        return f"{super().get_info()} GENRE: {self.genre}"
    
class NonFiction(Book):
    def __init__(self, title, author, isbn,subject, available=True):
        super().__init__(title,author,isbn,available)
        self.subject = subject

    def get_info(self):
        return f"{super().get_info()}. Subject: {self.subject}"
    
class Library:
    def __init__(self):
        self.books = []

    def add_book(self,book):
        self.books.append(book)

    def remove_book(self,book):
        self.books.remove(book)

    def search_by_title(self,title):
        matching_books = [book for book in self.books if book.title == title]
        return matching_books
    
    def search_by_author(self,author):
        matching_books = [book for book in self.books if book.author == author]
        return matching_books
    
    def search_by_isbn(self,isbn):
        matching_books = [book for book in self.books if book.isbn ==isbn]
        return matching_books
    
    def search_by_genre(self,genre):
        matching_books = [book for book in self.books if book.genre ==genre]
        return matching_books
    
    def display_book(self):
        for book in self.books:
            print(book.get_info())


book1 = Fiction("Superman", "BY: O.T BACKHOUSE", "0316769487","Fantasy")
book2 = NonFiction("Introduction to I.T", "BY: BASHIR", "0192860925","Information to Technology")
book3 = Fiction("The Lords of the Rings", "BY: MAHLET", "0446310786", "Adventure")


lib = Library()
lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)

#lib.display_book()
# book2.check_out()

matching_books = lib.search_by_title("Superman")
print([book.get_info() for book in matching_books])


        