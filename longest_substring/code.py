# for each substring -> dict freq 
# if freq is not 1 ->duplicates in substring
# list of non-duplicate substrings
# list of lengths -> get the largest 
from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, input_string):
        list_of_non_duplicate_substring=[]
        for i in range(len(input_string)):
            for j in range(len(input_string)):
                if j<=i:
                    duplicates=self.has_duplicates(input_string[j:i+1])
                    if duplicates is False:
                        list_of_non_duplicate_substring.append(input_string[j:i+1])
        list_of_lengths=[]
        for substring in list_of_non_duplicate_substring:
            list_of_lengths.append(len(substring))
        list_of_lengths.sort()
        if list_of_lengths==[]:
            return 0
        else:
            return list_of_lengths[-1]
    def has_duplicates(self,input_string):
        char_freq=dict(Counter(input_string))
        for freq in char_freq.values():
            if freq!=1:
                return True
        return False
mysolution=Solution()
print(mysolution.lengthOfLongestSubstring("bbbbb"))
print(mysolution.lengthOfLongestSubstring("abcabcbb"))
print(mysolution.lengthOfLongestSubstring("pwwkew"))
