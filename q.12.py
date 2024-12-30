lst = [1, 2, 3, 4, 5]
odd_numbers = []
even_numbers = []

for num in lst:
    if num % 2 == 0: 
        even_numbers.append(num)
    else:  
        odd_numbers.append(num)
print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)