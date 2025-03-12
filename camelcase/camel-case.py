def camelcase(s):
    num_of_words=1
    for letter in s:
        if letter.isupper():
            num_of_words=num_of_words+1 #total number of words= number of capital letters + 1
    return num_of_words
            

if __name__ == '__main__':
    s = input()
    print(camelcase(s))