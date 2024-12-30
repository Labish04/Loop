def is_palindrome(number):
    original_number = number
    reversed_number = 0
    while number > 0:
        digit = number % 10 
        reversed_number = reversed_number * 10 + digit 
        number = number // 10 
    if original_number == reversed_number:
        return True
    else:
        return False
number = int(input("Enter a number: "))
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")