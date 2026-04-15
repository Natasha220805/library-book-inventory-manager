import json
from book import Book

class Library:
  def __init__(self):
    self.books = {} 

  def add_book(self,book):
    self.books[book.title] = book
    self.save_to_file()

  def search_by_title(self,title):
    return self.books.get(title)

  def search_by_author(self,author):
    results = []
    for book in self.books.values():
      if book.author.lower() == author.lower():
        results.append(book)
    return results

  def issue_book(self,title):
    book = self.books.get(title)
    if book and not book.is_issued:
      book.issue()
      print("The book is issued!")
    else:
      print("The book is not available")   

  def return_book(self,title):  
    book = self.books.get(title)
    if book and book.is_issued:
      book.return_book()
      print("Book returned!")

  def report(self):
    total = len(self.books)
    issued = sum(1 for b in self.books.values() if b.is_issued)
    print(f"Total books: {total} ") 
    print(f"Issued books: {issued}")    

  def save_to_file(self):
    with open("data.json" , "w") as f:
      json.dump(
        {title: book.to_dict() for title, book in self.books.items()},
        f,
        indent=4
      )
  
  def load_from_file(self):
    try:
      with open("data,json" , "r") as f:
        data = json.load(f)
        self.books = {
          title: Book.from_dict(book_data)
          for title, book_data in data.items()
        }
    except FileNotFoundError:
      print("No data file found.")    

