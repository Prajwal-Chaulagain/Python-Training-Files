import json
import streamlit as st

FILENAME = "books.json"

def load_books():
    """Loads books from the JSON file."""
    try:
        with open(FILENAME, "r") as file:
            books = json.load(file)
            if isinstance(books, list):
                return books
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_books(books):
    """Saves the books list to the JSON file."""
    with open(FILENAME, "w") as file:
        json.dump(books, file, indent=4)

def main():
    st.title("📚 Library Management System")
    books = load_books()
    
    menu = ["Display Books", "Add Book", "Remove Book"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Display Books":
        st.subheader("Available Books")
        if not books:
            st.write("No books available in the library.")
        else:
            for index, book in enumerate(books, start=1):
                st.write(f"{index}. **{book['name']}** by {book['author']}")

    elif choice == "Add Book":
        st.subheader("Add a New Book")
        book_name = st.text_input("Enter book name")
        author_name = st.text_input("Enter author name")
        if st.button("Add Book"):
            books.append({"name": book_name, "author": author_name})
            save_books(books)
            st.success(f"Book '{book_name}' by {author_name} added successfully!")
            st.rerun()

    elif choice == "Remove Book":
        st.subheader("Remove a Book")
        if not books:
            st.write("No books available to remove.")
        else:
            book_list = [f"{book['name']} by {book['author']}" for book in books]
            book_to_remove = st.selectbox("Select a book to remove", book_list)
            if st.button("Remove Book"):
                books = [book for book in books if f"{book['name']} by {book['author']}" != book_to_remove]
                save_books(books)
                st.success("Book removed successfully!")
                st.rerun()

if __name__ == "__main__":
    main()