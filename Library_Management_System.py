class Library:
    def __init__(self):
        self.file_name = "books.txt"
        self.file = open(self.file_name, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.read().splitlines()
        if not books:
            print("There is not any books in the list.")
        else:
            print("Books:")
            for book in books:
                title, author, release_date, pages = book.strip().split(',')
                print(f"Title = {title}, Author =  {author}")

    def add_book(self):
        title = input("Enter the title: ")
        author = input("Enter the author: ")
        release_date = input("Enter the release year: ")
        page_number = input("Enter the number of pages: ")
        info = f"{title},{author},{release_date},{page_number}\n"
        self.file.write(info)
        print("Book adding complete.")

    def remove_book(self):
        title = input("Please enter the title of the book for remove: ")
        self.file.seek(0)
        books = self.file.readlines()
        found = False
        new_books = []
        for book in books:
            if title in book:
                found = True
                continue
            new_books.append(book)
        if found:
            self.file.seek(0)
            self.file.truncate()
            self.file.writelines(new_books)
            print(f"Book '{title}' is removed.")
        else:
            print(f"Book '{title}' is not in the library system already.")

library1 = Library()

while True:

    print("Welcome to the library management system.")
    print("**********************************************")
    print("1-List Books")
    print("2-Add Book")
    print("3-Remove Book")
    print("4-Quit")
    print("**********************************************")
    num = input("Enter a number:")

    if num == '1':
        library1.list_books()
    elif num == '2':
        library1.add_book()
    elif num == '3':
        library1.remove_book()
    elif num == '4':
        break
    else:
        print("Wrong enter. Please enter a number between 1-4")