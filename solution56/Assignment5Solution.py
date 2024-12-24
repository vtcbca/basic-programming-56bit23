def is_palindrome(s):
    return s == s[::-1]

input_string = input("Enter a string: ").replace(" ", "").lower()  # Remove spaces and make lowercase
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")