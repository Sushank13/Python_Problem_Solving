def pangrams(s):
    list_of_words=s.lower().split() # convert to lower case to ignore case and split with space as seperator
    inputstring="".join(list_of_words) # convert the list to a string sans spaces
    return "pangram" if len(set(inputstring))==26 else "not pangram"
    
if __name__ == '__main__':
    s = input()
    result = pangrams(s)
    print(result)