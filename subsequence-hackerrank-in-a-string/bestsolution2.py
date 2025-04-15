# input: abcdefg, ace 
        #0123456 #012
def is_subsequence(str1,s):
    i,j=0,0
    while i<len(str1) and j<len(s):
        if str1[i]==s[j]: #match
            j=j+1
        i=i+1
    return True if j==len(s) else False 
print(is_subsequence("abcdefg","ace")) 
print(is_subsequence("abcdefg","aec"))  