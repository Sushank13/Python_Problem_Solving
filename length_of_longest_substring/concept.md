## Strategy to be Used
We need to use **Sliding Window Startegy** because if we use **brute force** (check each and every substring)it is inefficient.
## Brute Force Approach
1. Iterate the strig using two pointers and retrive substrings
2. For reach substring, check if it has duplicates.
3. If no duplicates found, check the length of the substring
4. Return the value of the longest substring 
## Mistake made by me in Brute Force approach
1. I was storing the substrings with no duplicates in a list but it was not required as I was not going to utilize those substrings anywhere. So, I was wasting memory.
2. **While checking for duplicates, I was creating a dictionary-map while a simple set() could be used**. 
## Problem with Brute Force approach
We would be checking every substring for a particular character in the string,even after first duplicate if found. So, we do not need to keep the algorithm going after first duplicate is found. To achieve this, we need to use sliding window technique.
## Sliding Window Approach
This is ensure that are substring/window always never contain any duplicates.
***Refer Python_My_Notes-> Algorithms to understand this approach***
### Algorithm
***TBD***
