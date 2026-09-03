FILENAME = "books.csv"

def load_books():
    books = []
    try:
        with open(FILENAME, "r") as f:
            for line in f:
                book_id, title, author, status = line.strip().split(",")
                books.append([book_id, title, author, status])
    except FileNotFoundError:
        pass
    return books

def save_books(books):
    with open(FILENAME, "w") as f:
        for b in books:
            f.write(",".join(b) + "\n")

def add_book(books, book_id, title, author):
    books.append([book_id, title, author, "Available"])
    save_books(books)
    print("Book added")

def search_book(books, book_id):
    for b in books:
        if b[0] == book_id:
            print(b)
            return b
    print("Book not found")
    return None

def issue_book(books, book_id):
    for b in books:
        if b[0] == book_id and b[3] == "Available":
            b[3] = "Issued"
            save_books(books)
            print("Book issued")
            return
    print("Book not available")

def return_book(books, book_id):
    for b in books:
        if b[0] == book_id and b[3] == "Issued":
            b[3] = "Available"
            save_books(books)
            print("Book returned")
            return
    print("Book was not issued")

def display_available(books):
    print("Available books:")
    for b in books:
        if b[3] == "Available":
            print(b)


books = load_books()
add_book(books, "B1", "Python Basics", "John Doe")
add_book(books, "B2", "Data Structures", "Jane Roe")
search_book(books, "B1")
issue_book(books, "B1")
display_available(books)
return_book(books, "B1")
display_available(books)
