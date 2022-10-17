my_book = {
    "title": "Then Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

my_book_list = [
    {
        "title": "Then Hunger Games",
        "author": "Suzanne Collins",
        "year": 2008,
        "rating": 4.32,
        "pages": 374
    },
    {
        "title": "The Catcher in the Rye",
        "author": "J.D. Sallinger",
        "year": 1972,
        "rating": 9.8,
        "pages": 274
    },
    {
        "title": "Twilight",
        "author": "Walker Hebert",
        "year": 2006,
        "rating": 7.9,
        "pages": 721
    }
]

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below
def book_parser(book_dictionary):
    
    bookString = f"the name of the book is the {book_dictionary['title']}, and it was written by {book_dictionary['author']}, and it was published in {book_dictionary['year']}, and the rating is {book_dictionary['rating']}, and it has {book_dictionary['pages']} pages."
    
    return bookString

print(book_parser(my_book))



# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below
def my_function_title(book_dictionary):
    book_title = book_dictionary["title"]
    return book_title

def my_function_author(book_dictionary):
    book_author = book_dictionary["author"]
    return book_author

def my_function_year(book_dictionary):
    book_year = book_dictionary["year"]
    return book_year

def my_function_rating(book_dictionary):
    book_rating = book_dictionary["rating"]
    return book_rating

def my_function_pages(book_dictionary):
    book_pages = book_dictionary["pages"]
    return book_pages
    
    
print(my_function_title(my_book))
print(my_function_author(my_book))
print(my_function_year(my_book))
print(my_function_rating(my_book))
print(my_function_pages(my_book))


# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below
def book_parser_from_list(book_dictionary_list):
    for book_dictionary in book_dictionary_list:
        print(book_parser(book_dictionary))
        
def get_set_of_authors(book_dictionary_list):
    author_set = set()
    
    for book_dictionary in book_dictionary_list:
        author_set.add(book_dictionary["author"])

    return author_set

def get_total_pages(book_dictionary_list):
    total_pages = 0

    for book_dictionary in book_dictionary_list:
        total_pages += book_dictionary["pages"]

    return total_pages



book_parser_from_list(my_book_list)
print(get_set_of_authors(my_book_list))
print(get_total_pages(my_book_list))