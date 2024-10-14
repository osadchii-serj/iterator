from dataclasses import dataclass

from author_iterator import AuthorIterator
from library_iterator import LibraryIterator
from genre_iterator import GenreIterator

from interface import ILibrary


@dataclass
class Library(ILibrary):

    books = []

    def add_book(self, book: str):
        self.books.append(book)

    def get_author_iterator(self):
        return AuthorIterator(self)

    def get_genre_iterator(self):
        return GenreIterator(self)

    def __iter__(self):
        return LibraryIterator(self)
