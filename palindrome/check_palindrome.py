def is_palindrome(input_string):
    input_string=input_string.lower()
    if input_string==input_string[::-1]:
        return True
    return False
#print(is_palindrome("pot"))
print(is_palindrome("pop"))