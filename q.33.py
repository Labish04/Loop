lst1 = [1, "hello", 3.14, True, [1, 2], {"key": "value"}]
types_list = []
for i in lst1:
    types_list +=[type(i)]  
print(types_list)