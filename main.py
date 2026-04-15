from library import Library
from book import Book

def main():
  lib = Library()
  lib.load_from_file()

  while True:
    print("\n 1. Add Book")
    print("2. Search by Title")
    print("3. Search by Author")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Report")
    print("7. Exit")

    choice = input("Choose: ")

    if choice == "1":
      title = input("Title: ")
      author = input("Author: ")
      lib.add_book(Book(title, author))

    elif choice == "2":
      title = input("Title ")
      book = lib.search_by_title(title)
      if book:
        print(f"Found: {book.title} by {book.author}")
      else:
        print("Not found.")

    elif choice == "3":
      author = input("Author: ")
      results = lib.search_by_author(author)
      for b in results:
        print(b.title)

    elif choice == "4":      
      title = input("Title: ")
      lib.issue_book(title)

    elif choice == "5":    
      title = input("Title: ")
      lib.return_book(title)

    elif choice == "6":   
      lib.report()

    elif choice == "7":   
      lib.save_to_file
      break


if __name__ == "__main__":
  main()