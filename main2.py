print("Hello World 2")
#EXERCISE 1 LISTS
fruits = ["Mango", "Apple", "Banana", "Strawberry"]
print(fruits)
fruits.append("Orange")
fruits.pop(1)
fruits.sort()
first_three = fruits[:3]

print("Original list", fruits)
print("New list (first three):", first_three)
print(fruits[2])
print(7 % 5)


#EXERCISE 2 TUPLES
# TODO: Create a tuple with your favorite colors
colors = ("fuchsia", "green", "baby bleu")
print(colors)
# TODO: Try to modify one of the colors (this should raise an error)
# TODO: V1 Count how many times a specific color appears in the tuple
count = colors.count("fuchsia")
print(count)
count_fuchsia = colors.count("fuchsia")
print("Fuchsia appears", count_fuchsia, "times")

# TODO: Find the index of a specific color
index_green = colors.index("green")
print("Index of green", index_green)


# TODO: Create a new tuple by concatenating two existing tuples
more_colors = ("yellow", "purple")
new_tuple = colors + more_colors

print("Original tuple:", colors)
print("New tuple:", new_tuple)

# Print the results of each operation

print(18 > 160)
print("18" > "160")

# TODO: Create a dictionary representing a person (name, age, city)
# TODO: Add a new key-value pair for the person's occupation
# TODO: Update the person's age
# TODO: Remove the 'city' key-value pair
# TODO: Print all keys, then all values
# TODO: Check if a specific key exists in the dictionary
# Print the final dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "Paris"}
person["occupation"] = "Designer"
person["age"] = 26
person.pop("city")
print("Keys:", person.keys())
print("Values:", person.values())
print("Is 'age' in dictionary?", "age" in person)
print("Is 'city' in dictionary?", "city" in person)
print("Final dictionary:", person)

# EXERCISE 4 SETS
# TODO: Create two sets of numbers
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("Set 1:", set1)
print("Set 2:", set2)
# TODO: Find the union of the two sets
union_set = set1.union(set2)
print("Union:", union_set)
# TODO: Find the intersection of the two sets
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

# TODO: Find the difference between the first and second set
difference_set = set1.difference(set2)
print("Difference (set1 - set2):", difference_set)

# TODO: Add a new element to one of the sets
set1.add(10)
print("After adding 10 to set1:", set1)

# TODO: Remove an element from one of the sets
print("After removing 2 from set1:", set1)

# Print the results of each operation


#EXE 5 NESTED DATA STRUCTURES 
# TODO: Create a list of dictionaries representing books (title, author, year)
books = [
    {"title": "The Alchemist", "author": "Paulo Coelho", "year": 1988},
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960}
    ]

# TODO: Add a new book to the list
books.append(
    {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932})

for book in books:
    print(f"- {book['title']} ({book['year']}) by {book['author']}")

# TODO: Sort the list of books by year

# TODO: Create a dictionary where keys are authors and values are lists of their books

# TODO: Print all books by a specific author

# Print the final nested data structure


