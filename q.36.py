bad_chars = [';', ':', '!', "*"]
string = "py;th*o:n!;py*t*h:o!n"
cleaned_string = ""
for i in string:
    if i not in bad_chars:
        cleaned_string += i 
print(cleaned_string)