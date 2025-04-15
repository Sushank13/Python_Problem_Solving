# LeetCode #28: WAP to Find the Index of the First Occurrence in a String
# Given two strings haystack and needle, 
# return the index of the first occurrence of needle in haystack, 
# or -1 if needle is not part of haystack.
# input 1: haystack = "sadbutsad", needle = "sad"
#ouput1:0
#input2: haystack = "leetcode", needle = "leeto"
#output2:-1
#simple splution(not to be used): use in-built string method find()->haystack.find(needle)
# I want to match substrings in the haystack with the needle
#in such a way that substring will be of length=len of needle
# will increase the start index by step of 1 as I want to look at
# every position in the haystack. 
def haystack_needle(haystack,needle):
    if not needle: # empty needle
        return 0
    i=0
    flag=0
    while(i<len(haystack)-len(needle)): # no need to iterate till full length of haystack 
        if haystack[i:i+len(needle)]==needle:
            flag=1
            break
        i=i+1
    return i if flag==1 else -1 
print(haystack_needle("sadbutsad","sad"))
print(haystack_needle("leetcode","leeto"))
print(haystack_needle("helloworld","owo")) 
print(haystack_needle("hello","ll")) 
print(haystack_needle("hello","")) 
