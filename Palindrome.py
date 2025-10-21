
def palindrome(string):
    if (string == string[::-1]):
        return "The String is a palindrome"
    else:
        return "The String is not a palindrome"

string = input("Enter the String: ")
print(palindrome(string.lower()))

reverse_string = ""
for i in string.lower():
    reverse_string = i+reverse_string

if string.lower() == reverse_string:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
