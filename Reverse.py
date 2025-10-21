string = input("Enter the String: ")

reverse_string = ""
for i in string:
    reverse_string = i+reverse_string
rev = string[::-1]
print("The string reverse : "+reverse_string)
print("The string reverse type 2 : "+rev)