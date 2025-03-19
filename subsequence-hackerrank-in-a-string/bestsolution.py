def hackerrankInString(t):
    s="hackerrank"
    i,j=0,0 #initialiaze two pointers
    while i<=len(s)-1 and j<=len(t)-1:
        if s[i]==t[j]: # there is a match
            i=i+1 # move the pointer of string s to the next element
        j=j+1 # move the pointer of string t to next element in either case
    return "YES" if i==len(s) else "NO" # we were able to match every character in s
if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        t = input()
        result=hackerrankInString(t)
        print(result)