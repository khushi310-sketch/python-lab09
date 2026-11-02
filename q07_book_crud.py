books = []

while True:
    print("\n1. Add Book")
    print("2. View Books")
    print("3. Update Book")
    print("4. Delete Book")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        books.append(book)
        print("Book added successfully!")

    elif choice == "2":
        print("Books:", books)

    elif choice == "3":
        old_book = input("Enter old book name: ")
        if old_book in books:
            new_book = input("Enter new book name: ")
            index = books.index(old_book)
            books[index] = new_book
            print("Book updated!")
        else:
            print("Book not found!")

    elif choice == "4":
        book = input("Enter book name to delete: ")
        if book in books:
            books.remove(book)
            print("Book deleted!")
        else:
            print("Book not found!")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")