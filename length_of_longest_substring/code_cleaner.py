class Solution:
    def lengthOfLongestSubstring(self, input_string):
        longest_length=0
        for i in range(len(input_string)):
            for j in range(len(input_string)):
                if j<=i:
                    if self.has_duplicates(input_string[j:i+1]) is False:
                        if len(input_string[j:i+1])>longest_length:
                            longest_length=len(input_string[j:i+1])
        return longest_length
        
    def has_duplicates(self,input_string):
        if len(input_string)!=len(set(input_string)): # has duplicates
            return True
        return False
mysolution=Solution()
print(mysolution.lengthOfLongestSubstring("bbbbb"))
print(mysolution.lengthOfLongestSubstring("abcabcbb"))
print(mysolution.lengthOfLongestSubstring("pwwkew"))