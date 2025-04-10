def is_palindrome(input_string):
    input_string=input_string.lower()
    reverse_string=reversed_string(input_string)
    if input_string==reverse_string:
        return True
    return False
def reversed_string(input_string):
    output_string=""
    for element in input_string:
        output_string=element+output_string
    return output_string
print(is_palindrome("pot"))
print(is_palindrome("pop"))