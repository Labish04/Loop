start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

sum_of_evens = 0
for num in range(start, end + 1):
    if num % 2 == 0: 
        sum_of_evens += num
print(f"The sum of all even numbers between {start} and {end} is: {sum_of_evens}")