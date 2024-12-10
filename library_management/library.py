# -*- coding: utf-8 -*-

import json
import os

class Book:
    def __init__(self, id, title, author, year, status="available"):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }

class Library:
    def __init__(self, filename='library_data.json'):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as file:
                return [Book(**data) for data in json.load(file)]
        return []

    def save_books(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False, indent=4)

    def add_book(self, title, author, year):
        book_id = len(self.books) + 1
        new_book = Book(book_id, title, author, year)
        self.books.append(new_book)
        self.save_books()

    def remove_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                self.save_books()
                return
        print("Book with this ID not found.")

    def search_books(self, query):
        results = [book for book in self.books if query.lower() in book.title.lower() or
                   query.lower() in book.author.lower() or
                   query == str(book.year)]
        return results

    def display_books(self):
        for book in self.books:
            print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}")

    def change_status(self, book_id, new_status):
        for book in self.books:
            if book.id == book_id:
                if new_status in ["available", "issued"]:
                    book.status = new_status
                    self.save_books()
                    return
                else:
                    print("Invalid status. Available statuses: 'available', 'issued'.")
                    return
        print("Book with this ID not found.")

def main():
    library = Library()
    while True:
        print("\n1. Add book")
        print("2. Remove book")
        print("3. Search book")
        print("4. Display all books")
        print("5. Change book status")
        print("6. Exit")
        choice = input("Choose an action: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = input("Enter publication year: ")
            library.add_book(title, author, year)
        elif choice == '2':
            book_id = int(input("Enter book ID to remove: "))
            library.remove_book(book_id)
        elif choice == '3':
            query = input("Enter title, author, or year to search: ")
            results = library.search_books(query)
            if results:
                for book in results:
                    print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}")
            else:
                print("No books found.")
        elif choice == '4':
            library.display_books()
        elif choice == '5':
            book_id = int(input("Enter book ID to change status: "))
            new_status = input("Enter new status ('available' or 'issued'): ")
            library.change_status(book_id, new_status)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()