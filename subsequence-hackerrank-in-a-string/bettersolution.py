def hackerrankInString(s):
    subsequence="hackerrank"
    i=0 # Pointer for subsequence
    for element in s:
        if element==subsequence[i]:
            i=i+1  # Move to the next subsequence character
            if i==len(subsequence): # If we match all chars
                return "YES"
    return "NO"

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()
        result=hackerrankInString(s)
        print(result)