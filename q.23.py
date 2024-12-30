string = input("Enter a string: ")
space_count = 0

for char in string:
    if char == ' ': 
        space_count += 1
print(f"The number of spaces in the given string is: {space_count}")