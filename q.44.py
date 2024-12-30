list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common_elements = []
for i in list1:
    if i in list2:
        common_elements.append(i)
print(f"Common elements: {common_elements}")