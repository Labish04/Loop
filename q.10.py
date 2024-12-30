lst = [1, 2, 3, 4]
for i in range(len(lst)):
    if i == 0 or i == 1 or i == len(lst) - 1:
        print(lst[i])