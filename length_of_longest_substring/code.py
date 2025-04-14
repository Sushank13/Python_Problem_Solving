# for each substring -> freq map 
# if freq of an element in substring is not 1 ->duplicates in substring
# if no duplicates in substring then calculate len of that substring and make 
#it the longest length.
# If the next substring with longest length, then assign that value
#from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, input_string):
        longest_length=0
        #list_of_non_duplicate_substring=[]
        for i in range(len(input_string)):
            for j in range(len(input_string)):
                if j<=i:
                    duplicates=self.has_duplicates(input_string[j:i+1])
                    if duplicates is False:
                        if len(input_string[j:i+1])>longest_length:
                            longest_length=len(input_string[j:i+1])
        return longest_length
                        #list_of_non_duplicate_substring.append(input_string[j:i+1])
        #for substring in list_of_non_duplicate_substring:
            #list_of_lengths.append(len(substring))
        #list_of_lengths=list(map(len,list_of_non_duplicate_substring))
        #list_of_lengths.sort()
        #if not list_of_lengths: # edge case if no substring without dupicates exists
            #return 0
        #else:
            #return list_of_lengths[-1]
        
    def has_duplicates(self,input_string):
        if len(input_string)!=len(set(input_string)): # has duplicates
            return True
        #char_freq=dict(Counter(input_string))
        #for freq in char_freq.values():
            #if freq!=1:
                #return True
        return False
mysolution=Solution()
print(mysolution.lengthOfLongestSubstring("bbbbb"))
print(mysolution.lengthOfLongestSubstring("abcabcbb"))
print(mysolution.lengthOfLongestSubstring("pwwkew"))
