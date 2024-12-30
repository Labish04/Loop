input_string = input("Enter a string: ")

num_letters = 0
num_digits = 0
num_spaces = 0

for char in input_string:
    if char.isalpha(): 
        num_letters += 1
    elif char.isdigit():  
        num_digits += 1
    elif char.isspace():  
        num_spaces += 1
print(f"Letters: {num_letters}")
print(f"Digits: {num_digits}")
print(f"Spaces: {num_spaces}")