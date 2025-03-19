def hackerrankInString(s):
    subsequence=[item for item in "hackerrank"]
    i=0
    item=subsequence[i]
    match=0
    for element in s:
        if element==item:
            match=match+1
            i=i+1
            if i>=len(subsequence):
                break
            item=subsequence[i]
    if match==len(subsequence):
        return True
    else:
        return False

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()
        result=hackerrankInString(s)
        if result is True:
            print("YES")
        else:
            print("NO")
            
            