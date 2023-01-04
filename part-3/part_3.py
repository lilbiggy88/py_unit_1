my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374,
}

lotr_list = [{
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
},

{
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374,
}

]

# Follow the instructions in this part of the project. 
# Define and flesh out your function below, which should accept a dictionary as an argument when called, 
# and return a string of the info in that book-dictionary in a user-friendly readable format.

def books(book_dictionary):
    book_string = f"The title of this book is called {book_dictionary['title']}. The author is {book_dictionary['author']}. The book came out in {book_dictionary['year']}. It's rating is {book_dictionary['rating']}. The book has {book_dictionary['pages']} pages. "
    return book_string
print(books(my_book))


# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

def book_title(book_dictionary):
    book_string = f"The title of this book is called {book_dictionary['title']}."
    return book_string
print(book_title(my_book))

def book_author(bd):
    book_string = f"The author of this book is {bd['author']}."
    return book_string
print(book_author(my_book))

def book_year(bd):
    year = f"The year the book was written was {bd['year']}"
    return year
print(book_year(my_book))

def book_rating(bd):
    rating = f"The book rating is {bd['rating']}"
    return rating
print(book_rating(my_book))

def book_pages(bd):
    pages = f"The book is {bd['pages']} pages"
    return pages
print(book_pages(my_book))


# Finally, create at least three new functions that might be useful as we expand our home library app. 
# Perhaps think of a way you could accept additional arguments when the function is called? 
# Also, imagine you have a list filled with dictionaries like above.

def pages_under_400(lotr_list):
    book_pages = []

    for book in lotr_list:
        if book['pages'] <= 400:
            book_pages.append(book['title'])
        else:
            pass
    return book_pages


print(pages_under_400(lotr_list))


def book_series(lotr_list):
    series = []

    for b_series in lotr_list:
        if 'The Lord of the Rings:' in b_series['title']:
            series.append(b_series['title'])
        else:
            pass
    return series

print(book_series(lotr_list))

def book_rating(lotr_list):
    rating = []

    for book in lotr_list:
        if book['rating'] >= 4.30:
            rating.append(book['title'])
        else:
            pass
    return rating

print(book_rating(lotr_list))


