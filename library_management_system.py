# Initial book catalog using dictionaries
book_catalog = [
    {'title': 'Python Crash Course', 'author': 'Eric Matthes', 'genre': 'Programming', 'availability': True},
    {'title': '1984', 'author': 'George Orwell', 'genre': 'Dystopian Fiction', 'availability': False},
    # Add more book entries as needed...
]
lending_records = [
    {'book': '1984', 'user': 'Alice', 'due_date': '2023-12-25'},
    # Add more lending records as needed...
]


# Function to add a new book to the catalog
def add_book():
    print("\n--- Add a New Book ---")
    title = input("Enter title: ")
    author = input("Enter author: ")
    genre = input("Enter genre: ")
    availability = input("Is the book available? (True/False): ").capitalize()
    if availability not in ['True', 'False']:
        print("Invalid input for availability. Please enter True or False.")
        return
    new_book = {'title': title, 'author': author, 'genre': genre, 'availability': availability == 'True'}
    book_catalog.append(new_book)
    print(f"Book '{title}' added to the catalog.")


# Function to edit book details based on title
def edit_book():
    print("\n--- Edit Book Details ---")
    title = input("Enter the title of the book to edit: ")
    new_title = input("Enter new title (leave blank to keep current): ")
    new_author = input("Enter new author (leave blank to keep current): ")
    new_genre = input("Enter new genre (leave blank to keep current): ")
    new_availability = input("Enter new availability (True/False, leave blank to keep current): ").capitalize()

    if new_availability and new_availability not in ['True', 'False']:
        print("Invalid input for availability. Please enter True or False.")
        return

    edit_book = any([new_title, new_author, new_genre, new_availability])
    if not edit_book:
        print("No changes made.")
        return

    for book in book_catalog:
        if book['title'].lower() == title.lower():
            if new_title:
                book['title'] = new_title
            if new_author:
                book['author'] = new_author
            if new_genre:
                book['genre'] = new_genre
            if new_availability:
                book['availability'] = new_availability == 'True'
            print(f"Book '{title}' details updated.")
            return
    print(f"Book '{title}' not found in the catalog.")


# Function to delete a book from the catalog based on title
def delete_book():
    print("\n--- Delete a Book ---")
    title = input("Enter the title of the book to delete: ")
    for book in book_catalog:
        if book['title'].lower() == title.lower():
            book_catalog.remove(book)
            print(f"Book '{title}' deleted from the catalog.")
            return
    print(f"Book '{title}' not found in the catalog.")


# Function to search books by title, author, or genre
def search_books(query):
    search_results = []
    for book in book_catalog:
        if query.lower() in book['title'].lower() or query.lower() in book['author'].lower() or query.lower() in book[
            'genre'].lower():
            search_results.append(book)

    if not search_results:
        print("No matching books found.")

    return search_results


# Function to sort books alphabetically by title
def sort_books_by_title():
    sorted_books = sorted(book_catalog, key=lambda x: x['title'].lower())
    return sorted_books


# Function to sort books by genre
def sort_books_by_genre():
    sorted_books = sorted(book_catalog, key=lambda x: x['genre'].lower())
    return sorted_books


def check_out_book(title, user, due_date):
    for book in book_catalog:
        if book['title'].lower() == title.lower() and book['availability']:
            book['availability'] = False
            lending_records.append({'book': title, 'user': user, 'due_date': due_date})
            print(f"Book '{title}' checked out by {user} until {due_date}.")
            return
    print(f"Book '{title}' is either unavailable or not found.")


# Function to return a book
def return_book(title):
    for book in book_catalog:
        if book['title'].lower() == title.lower() and not book['availability']:
            book['availability'] = True
            for record in lending_records:
                if record['book'].lower() == title.lower():
                    lending_records.remove(record)
            print(f"Book '{title}' returned successfully.")
            return
    print(f"Book '{title}' cannot be returned.")


# Function to check for overdue books
def check_overdue_books():
    import datetime
    today = datetime.date.today()
    overdue_books = []
    for record in lending_records:
        due_date = datetime.datetime.strptime(record['due_date'], "%Y-%m-%d").date()
        if due_date < today:
            overdue_books.append(record)
    return overdue_books


# Function to generate a summary of the library's status
def generate_summary():
    total_books = len(book_catalog)
    available_books = sum(1 for book in book_catalog if book['availability'])
    lent_out_books = total_books - available_books

    genres = [book['genre'] for book in book_catalog]
    popular_genres = max(set(genres), key=genres.count)

    print("\n--- Library Summary ---")
    print(f"Total Books: {total_books}")
    print(f"Available Books: {available_books}")
    print(f"Books Lent Out: {lent_out_books}")
    print(f"Most Popular Genre: {popular_genres}")


# Bonus Feature: Basic recommendation system based on book genres
def recommend_books_by_genre(genre):
    recommended_books = [book for book in book_catalog if book['genre'].lower() == genre.lower()]
    return recommended_books


# User interface (updated with organized options)
while True:
    print("\n--- Library Management System ---")
    print("1. Display Book Catalog")
    print("2. Borrowed")
    print("3. Generate Library Summary")
    print("4. Recommend Books by Genre")
    print("5. Exit")

    first_choice = input("Enter your choice (1-5): ")

    if first_choice == '1':
        # Display Book Catalog section
        print("\n--- Book Catalog ---")
        for index, book in enumerate(book_catalog, start=1):
            availability_status = "Available" if book['availability'] else "Not Available"
            print(
                f"{index}. Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}, Availability: {availability_status}")

        print("\nOptions:")
        print("1. Add a Book")
        print("2. Edit a Book")
        print("3. Delete a Book")
        print("4. Sort Books")
        print("5. Search the Book")
        print("6. Back to Main Menu")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            edit_book()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            while True:
                print("\n--- Sort Books ---")
                print("1. Sort by Title")
                print("2. Sort by Genre")
                print("3. Back to Book Catalog")
                second_choice = input("Enter your choice (1-3): ")

                if second_choice == '1':
                    sort_books_by_title()
                elif second_choice == '2':
                    sort_books_by_genre()
                elif second_choice == '3':
                    break
                else:
                    print("Invalid choice. Please enter a valid option.")

        elif choice == '5':
            user_search = input("Enter book title: ")
            search_books(user_search)
        elif choice == '6':
            pass
        else:
            print("Invalid choice. Please enter a valid option.")

    elif first_choice == '2':
        print("\n--- Borrowed ---")
        print("1. Check Out a Book")
        print("2. Return a Book")
        print("3. Check Overdue Books")
        borrow_choice = input("Enter your choice (1-3): ")
        if borrow_choice == '1':
            title = input("Enter the title of the book to check out: ")
            user = input("Enter your name: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            check_out_book(title, user, due_date)
        elif borrow_choice == '2':
            title = input("Enter the title of the book to return: ")
            return_book(title)
        elif borrow_choice == '3':
            overdue_books = check_overdue_books()
            if overdue_books:
                print("\n--- Overdue Books ---")
                for index, book in enumerate(overdue_books, start=1):
                    print(f"{index}. Book: {book['book']}, User: {book['user']}, Due Date: {book['due_date']}")
            else:
                print("No overdue books.")
        else:
            print("Invalid choice. Please enter a valid option (1-3).")
    elif first_choice == '3':
        generate_summary()
    elif first_choice == '4':
        genre = input("Enter the genre to recommend books: ")
        recommended_books = recommend_books_by_genre(genre)
        if recommended_books:
            print("\n--- Recommended Books ---")
            for index, book in enumerate(recommended_books, start=1):
                print(f"{index}. Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}")
        else:
            print("No recommended books found for this genre.")
    elif first_choice == '5':
        print("Exiting the Library Management System. Thank you!")
        break
    else:
        print("Invalid choice. Please enter a valid option (1-8).")
