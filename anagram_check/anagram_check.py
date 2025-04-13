# given two strings check if one is an anagram of the other
# str1=abbc, a:1,b:2,c:1
#str2=babb, a:1,b:3
from collections import Counter
def check_anagram(str1,str2):
    str1_map=dict(Counter(str1))
    str2_map=dict(Counter(str2))
    if len(str1)!=len(str2): #edge case: if lengths oftwo strings is not same, they can not be an anagram
        return False
    for key in str1_map.keys():
        if str1_map[key]!=str2_map[key]:
            return False
    return True
print(check_anagram("abbc","babb"))
print(check_anagram("abbc","babc"))
print(check_anagram("abbc","babccc"))