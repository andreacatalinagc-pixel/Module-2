print("Hello World 2")

fruits = ["Mango", "Apple", "Banana", "Strawberry"]
print(fruits)
fruits.append("Orange")
fruits.pop(1)
fruits.sort()
first_three = fruits[:3]

print("Original list", fruits)
print("New list (first three):", first_three)

print(7 % 5)

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