### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.
# def add_book():

#     title = input("What is the name of the title you would like to add?  ")
#     author = input("What is the name of the author of the book you would like to add?  ")
#     year = input("What is the year that this book was published?  ")
#     rating = input("What rating out of 5 would you give this book?  ")
#     pages = input("How many pages are in this book?  ")

#     book_dict = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }

#     return book_dict 
   

# print(add_book())


### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.
# def add_book():

#     title = input("What is the name of the title you would like to add?  ")
#     author = input("What is the name of the author of the book you would like to add?  ")
#     year = int(input("What is the year that this book was published?  "))
#     rating = float(input("What rating out of 5 would you give this book?  "))
#     pages = int(input("How many pages are in this book?  "))

#     book_dict = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }

#     return book_dict 
    
# print(add_book())


### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

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
    

    book_dict = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

    return book_dict 


print(add_book())



### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.
user_library= [{

    "title": "The Hobbit",
    "author": "J.R.R Tolkien",
    "year": 1937,
    "rating": 4.28,
    "pages": 310,
},
    {
    "title": "The Lord of the Rings: The Fellowship of the Ring",
    "author": "J.R.R Tolkien",
    "year": 1954,
    "rating": 4.38,
    "pages": 423,
},
    

{
    "title": "The Lord of the Rings: The Two Towers",
    "author": "J.R.R Tolkien",
    "year": 1954,
    "rating": 4.47,
    "pages": 352,
},

{
    "title": "The Lord of the Rings: The Return of the King",
    "author": "J.R.R Tolkien",
    "year": 1955,
    "rating": 4.55,
    "pages": 416,
}]

# def main_menu():
#     opt = int(input("Enter a 1 to add a new book, 2 to access all of the books, 3 for none of the above"))

#     if opt == 1:
#         add_book()
#         print(user_library)
#     elif opt == 2:
#         book_titles = []
#         for book in user_library:
#             book_titles.append(book["title"])
#         print(book_titles)
#     elif opt == 3:
#         print("You have finished looking for books")
#     else:
#         print("Enter a number 1-3")


 
        
# main_menu()     

### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to 
## exit the program. Call the main menu to ensure it functions properly.

def main_menu():

    menu_loop = True
    
    while menu_loop:
        
        opt = int(input("Enter a 1 to add a new book, 2 to access all of the books, 3 for none of the above  "))
        
        if opt == 1:
            add_book()
            print(user_library)
        elif opt == 2:
            book_titles = []
            for book in user_library:
                book_titles.append(book["title"])
            print(book_titles)
        elif opt == 3:
            print("You have finished looking for books")
            menu_loop = False
        else:
         print("Enter a number 1-3")

        
main_menu()     


