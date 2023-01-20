### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. 
## Follow the instructions to create and call a function to add a book, based off of the previous dictionaries 
## for our library, to the .txt file properly formatted with commas as separators.




def add_book():

    title = input("What is the name of the title you would like to add?  ")
    author = input("What is the name of the author of the book you would like to add?  ")
    try:
        year = int(input("What is the year that this book was published?  "))
    except:
        year = int(input("Please type a number for the year.  "))
    try:
        rating = float(input("What rating out of 5 would you give this book?  "))
    except:
        rating = float(input("Please type a number followed by a period and another number for your rating.  "))
    try:
        pages = int(input("How many pages are in this book?  "))
    except:
        pages = int(input("Please type a number for the pages.  "))
    
    with open("library.txt", "a") as f:
        f.write(f"{title}, {author}, {year}, {rating}, {pages}\n")

    # add_book()

### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, 
## but gets the info from a list, and make it work by reading the information in your home library's 
## .txt document. This will take some new logic, but you can do it.

def book_library():

    with open("library.txt", 'r') as f:
        file = f.readlines()

        for line in file:
            title, author, year, rating, pages = line.split(", ")

        print(f'\nTitle: {title}, Author: {author}, Year: {year}, Rating: {rating}, Pages: {pages}')

# book_library()



### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally 
## run if this file is imported as a module elsewhere.

def main_menu(library):

    menu_loop = True
    
    while menu_loop:
        
        opt = int(input("Enter a 1 to add a new book, 2 to access all of the books, 3 for none of the above  "))
        if opt == 1:
            add_book()
        elif opt == 2:
            book_library()
        elif opt == 3:
            print("You have finished looking for books")
            menu_loop = False
        else:
         print("Enter a number 1-3")

if __name__ == "__main__:":
    main_menu()     
# Code this at the bottom of the script


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. 
## Great job getting your first Python application finished!
books = []

def add_book():

    title = input("What is the name of the title you would like to add?  ")
    author = input("What is the name of the author of the book you would like to add?  ")
    try:
        year = int(input("What is the year that this book was published?  "))
    except:
        year = int(input("Please type a number for the year.  "))
    try:
        rating = float(input("What rating out of 5 would you give this book?  "))
    except:
        rating = float(input("Please type a number followed by a period and another number for your rating.  "))
    try:
        pages = int(input("How many pages are in this book?  "))
    except:
        pages = int(input("Please type a number for the pages.  "))
    
    with open("library.txt", "a") as f:
        f.write(f"{title}, {author}, {year}, {rating}, {pages}\n")


def book_library():

    with open("library.txt", 'r') as f:
        file = f.readlines()
        for line in file:
            title, author, year, rating, pages = line.split(", ")
            books.append({
                "title": title,
                "author": author,
                "year": int(year),
                "rating": float(rating),
                "pages": int(pages)
            })
    return books

book_library('library.txt')







def main_menu(library):

    menu_loop = True
    
    while menu_loop:
        
        opt = int(input("Enter a 1 to add a new book, 2 to access all of the books, 3 for none of the above  "))
        if opt == 1:
            add_book()
        elif opt == 2:
            book_library()
        elif opt == 3:
            print("You have finished looking for books")
            menu_loop = False
        else:
         print("Enter a number 1-3")

if __name__ == "__main__:":
    main_menu("library.txt")   