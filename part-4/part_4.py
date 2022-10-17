### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here
# bookTitle = input('Enter the name of the book: ')
# bookAuthor = input('Enter the author of the book: ')
# bookYear = input('Enter the year of the book: ')
# bookGenre = input('Enter the genre of the book: ')
# bookPages = input('\nHow many pages is your favorite book? ')
    
### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here
# bookTitle = input('\nWhat is your favorite book? ')
# bookAuthor = input('\nWho is the author of your favorite book? ')
# bookYear = int('\nWhat year did your favorite book come out? ')
# bookGenre = input('\nWhat genre is your favorite book? ')
# bookPages = int('\nHow many pages is your favorite book? ')


### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here



### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here

def mm_function(books_library):

    choice = input('Choose 1 if you want to add a book. 2 if you want get all the books. 3 to create an account.')
    
    if choice == '1':
        books_library.append(addNewBook())
    elif choice == '2':
        getAllBooks(books_library)
    elif choice == '3':
        print("\nSee ya later!")
        active = False
    else:
        print("\n ERROR please add a number input")
    mm_function(books_library)
### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here
books = [
    {
        "name": "Twilight",
        "author": "Walker",
        "year": 2006,
        "genre": "Romance",
        "pages": 700
    },
    {
        "name": "Harry Potter",
        "author": "Rowling",
        "year": 2001,
        "genre": "Fantasy",
        "pages": 800
    },
    {
        "name": "The Hunger Games",
        "author": "Collins",
        "year": 2008,
        "genre": "Dystopian",
        "pages": 900
    },
    {
        "name": "The Fault in Our Stars",
        "author": "Green",
        "year": 2012,
        "genre": "Romance",
        "pages": 1000
    }
]


def addNewBook():
    name = input('Enter the name of the book: ')
    author = input('Enter the author of the book: ')
    genre = input('Enter the genre of the book: ')
    try:
        year = int(input('Enter the year of the book: '))
    except:
        year = int(input('Insert a number'))  
    try: 
        rating = float(input("What rating would you give this book on a scale of 1-10"))
    except: 
        rating = float(input("Insert a number"))
    try:
        pages = int(input('Enter the number of pages of the book: '))
    except:
        pages = int(input('Insert a number'))
    
    
    dictionary = {
        "name": name,
        "author": author,
        "year": year,
        "genre": genre,
        "pages": pages  
    }
    
    return dictionary

def getAllBooks(books_list):
    
    print("\nThese are the books\n")
    for book in books_list:
        name = book["name"]
        author = book["author"]
        year = book["year"]
        genre = book["genre"]
        pages = book["pages"]
        
        print(f'Book name: {name}, Book Author: {author}, Book Year: {year}, Book Genre: {genre}, Book Pages: {pages}')
    
def mm_function(books_library):
    
    active = True
    
    while active:
        choice = input('Pick 1 if you want to add a book \nPick 2 if you want get all the books \nPick 3 to create an account \nPick 4 to see the total of pages in your books \nPick 5 to leave \nInsert here: ')
        if choice == '1':
            books_library.append(addNewBook())
        elif choice == '2':
            getAllBooks(books_library)
        elif choice == "3":
            print(f"\nThe total in this library is {len(books_library)} books.\n")
        elif choice == "4":
            print(f"\nThe books page count total is {sum([x['pages'] for x in books_library])} pages!\n")
        elif choice == '5':
            print("\nSee ya later!")
            active = False
        else:
            print("\n ERROR please add a number input\n")
            
            
mm_function(books)
    