a = "Hello, how are you?"
vowels = "aeiouAEIOU"
result_string = ""
for i in a:
    if i not in vowels: 
        result_string +=i
print(result_string)