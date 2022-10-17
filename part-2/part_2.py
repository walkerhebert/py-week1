### Step 1 - Lists ###

# Fill in this list with several authors you are a fan of. At least 7 or 8 should do.
my_authors = ['walker', 'juan', 'cody', 'brady', 'mom', 'chad', 'dad']

# Now let's add a new author to the end with the .append() method. Type your code below.
# Code here
my_authors.append('apple')
# Example: my_authors.append("H.G. Wells")


# Now let's remove an element in the list

# Code here
my_authors.remove('apple')
print(my_authors)
# Example: my_authors.remove("H.G. Wells")


# Now access an element by it's index. (Remember it indexes start at 0.)

# Code here
print(my_authors[-1])
# Example: my_authors[2]


# Now slice the list.

# Code here
print(my_authors[1:3])
# Example: my_authors[1:4]


### Step 2 - Tuples ###

# Create your tuple below. Assign it to a variable name you can reference later in the exercise.

# Code here
author_tuple_example = ('walker', 'juan', 'cody', 'brady', 'mom', 'chad', 'dad')
# Example: my_author_tuple = ("F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury")


### Step 3 - Sets ###

# Create a set with your authors.

# Code here
my_authors_set = {'walker', 'juan', 'cody', 'brady', 'mom', 'chad', 'dad'}
# Example: my_author_set = {"F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury"}


# Add a new author to your set.

# Code here
my_authors_set.add('Chad Brad')
# Example: my_author_set.add("J.R.R. Tolkien")


# Try adding the same author again, and be sure to print your set.

# Code here
my_authors_set.add('Chad Brad')
print(my_authors_set)
# Example: my_author_set.add("J.R.R. Tolkien")



### Step 4 - For Loops ###

# Create a for-loop for each of the data-structures above.

# Code here
for i in my_authors:
    print(i)
    
for i in tupee:
    print(i)
    
for i in my_authors_set:
    print(i)
# Example:

# for book in my_authors:
    # print(book)

# for book in my_authors_tuple:
    # print(book)

# for book in my_authors_set:
    # print(book)

