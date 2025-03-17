import json
def display_menu():
    print("\n📚 Welcome to your Personal Library Manager!")
    print("1. Add a book")
    print("2. Remove a book ")
    print("3. Search for a book")
    print("4. Display all books ")
    print("5. Display statistics")
    print("6. Exit")

library=[]


def add_book():
    title=input("Enter the book title: ")
    author=input("Enter the author: ") 
    publication_year=input("Enter the publication year: ")
    genre=input("Enter the genre: ")
    read=input("Have you read this book? (yes/no): ").lower().strip()=="yes"
    
    my_book={
        "title":title,
        "author":author,
        "publication_year":publication_year,
        "genre":genre ,
        "read":read
    }
    library.append(my_book)
    print(f"{title} added successfully ✔.")

def remove_book():
    remove=input("Enter the title of the book to remove: ").strip()
    for book in library:

        if book["title"].lower() ==remove.lower():
            library.remove(book)
            print(f"{book["title"]} removed seccessfully ❌")
            return
        else :
            print("Book not found")

def search_book():
    search_by=input("Enter 1 (title) or 2 (author)? ").strip()
    # if search_by == 1:
    #     querry=input("Enter the title: ")
    #     result=[book for book in library if querry.lower() in book["title"].lower() ]
    # elif search_by == 2:
    #     querry=input("Enter the author: ")
    #     result=[book for book in library if querry.lower() in book["author"].lower() ]
    # else :
    #     print("Invalid choice!")
    #     return
    if search_by == "1":
        query = input("Enter book title: ").strip()
        result = [book for book in library if query.lower() in book["title"].lower()]
    elif search_by == "2":
        query = input("Enter book's author: ").strip()
        result = [book for book in library if query.lower() in book["author"].lower()]
    else:
        print("Invalid choice!")
        return
    if result:
        print("\n📖 Matching Books:")
        for book in result:
            print(f"{book["title"]} by {book["author"]} {book["publication_year"]} - {book["genre"]} - {"Read" if book["read"] else "Unread"}")
    else :
        print("❌ No matching books found.")            



def display_book():
    if not library:
        print("\n📭 Your library is empty")
        return
    
    print("\n📚  Your library")
    
    for i , book in enumerate(library,start=1):
        print(f"\n{i}. {book["title"]} by {book["author"]} ({book["publication_year"]}) - {book["genre"]} - {"Read" if book["read"] else "Unread"}")

def display_statistics():
    total_books=len(library)
    if total_books == 0:
        print("📭 No books in the library.")
        return
    
    read_books = sum(1 for book in library if book["read"])
    read_percent =(read_books / total_books) * 100

    print(f"\n📊 Library Statistics: ")
    print(f"Total Books: {total_books}")
    print(f"Percentage Read: {read_percent:.2f}%")

def save_library():
    with open("library.json","w") as file:
        json.dump(library,file)
        print("\n📁 Library saved successfully!")


def load_library():
    global library
    try:
        with open("library.json","r") as file:
            library = json.load(file)
    except FileNotFoundError:
        library=[] 
    except json.JSONDecodeError:
        print("❌Error decoding JSON. The library file may be corrupted.")
        library=[]                   