from dataclasses import dataclass
from library import Library


@dataclass
class AuthorIterator:

    _library: Library
    _index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._library.books):
            book = self._library.books[self._index]
            self._index += 1
            return book.author
