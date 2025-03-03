def swap_case(s):
    output=""
    for alphabet in s:
        if alphabet.lower()!=alphabet: # i.e. alphabet was in upper case
            output=output+alphabet.lower()
        elif alphabet.upper()!=alphabet: # i.e. alphabet was in lower case
            output=output+alphabet.upper()
        else:
            output=output+alphabet
    return output

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)