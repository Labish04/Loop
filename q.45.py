def is_prime(number):
    if number <= 1:
        print("false")
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0: 
           print("false")
    else:
        True 
number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")