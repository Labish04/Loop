a = 100
total_sum = 0
for number in range(3, a):
    if number % 3 == 0 or number % 5 == 0:
        total_sum += number 
print(f"The sum of all multiples of 3 or 5 below {a} is: {total_sum}")