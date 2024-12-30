lst = [1, 2, 3, 4, "a", "b"]
integers = []
strings = []

for item in lst:
    if isinstance(item, int):  
        integers.append(item)
    elif isinstance(item, str):  
        strings.append(item)
print("Integers:", integers)
print("Strings:", strings)