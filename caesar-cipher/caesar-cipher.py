def caesarCipher(s, k):
    output=[]
    encrypted_alphabet=""
    k=k%26 # to consider the possibility that key is greater than 26
    for alphabet in s :
            ascii_code=ord(alphabet)# get ASCII code of the aplhabet
            if ascii_code>=65 and ascii_code<=90: # between A-Z
                if ascii_code+k>90:
                    encrypted_alphabet=chr(65+((ascii_code+k)-90)-1)
                else:
                    encrypted_alphabet=chr(ascii_code+k)
                output.append(encrypted_alphabet)
            elif ascii_code>=97 and ascii_code<=122:  # between a-z
                if ascii_code+k>122:
                    encrypted_alphabet=chr(97+((ascii_code+k)-122)-1)
                else:
                    encrypted_alphabet=chr(ascii_code+k)
                output.append(encrypted_alphabet)
            else: # ASCII code is not in those boundaries
                output.append(alphabet)
    return "".join(output)
            
    

if __name__ == '__main__':
    n = int(input().strip())
    s = input()
    k = int(input().strip())
    result = caesarCipher(s, k)
    print(result)