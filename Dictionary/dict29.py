books = {1: "Python Basics", 2: "Data Structures", 3: "Operating Systems"}
books[4] = "Computer Networks"
search_id29 = 2
if search_id29 in books:
    print("Book found:", books[search_id29])
books.pop(3)
print("All books:", books)
print("Total books:", len(books))