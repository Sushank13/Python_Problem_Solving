## What is a subsequence?
**A string (say, s) can be called a subsequence of another string (say, t) if all the characters in "s" can be found in "t" in the same order as in the string "t"**

or

A subsequence is a **sequence that appears in the same relative order as the original sequence but not necessarily contiguous (consecutive)**.

**Unlike a substring (which must be contiguous)**, a subsequence can be formed by *removing some elements* **without changing the order** of the remaining elements.
## Example 
Original String: "abcdef"

Possible subsequences:
* "abc" (keeping first three letters)
* "ace" (skipping b and d)
* "def" (keeping last three letters)
* "aef" (skipping b, c, and d)
* "fa" (**not a subsequence** because the order is changed)
## Real-World Examples of Subsequences
* **Typing Auto-Suggestions** → If you type "hlo", the system might match "hello" since "hlo" is a subsequence.
* **DNA Sequences** → If "AGCTG" is the original DNA sequence, "ACT" is a valid subsequence
## Logic to be applied
* It is a dynamic programming question.We need to use **two-pointers**. 
* We have to iterate over the given strings (t) & (s) using two-pointers and match the elements in both.
* We will *move (the pointers) to the next element in both (s) and (t) only if there is a match while we will  move (the pointer) to the next element in (t) and not (s) if there is no match as now we will have to check the next character in (t)* (to preserve order as it will ensure that the next element in the (s) comes only after the previous element). 
* The *total number of matches should be equal to the length of the string (s)* (meaning we have successfully moved through the entire string).

     or

* The *pointer of string (s) should have vlue equal to that of the length of the string (s)*. 
* Else, *if we reach the end of the large string without finishing the small string, it's not a subsequence*.
## What Does "Preserving Order" Mean here?
* We say a sequence preserves order if characters appear in the same relative order as in the original subsequence, even if they are not consecutive.
* The **key to preserving order is moving the pointer forward only in the subsequence when a match occurs and never move backwards in the given sequence (i.e. We never reset the iteration)**.

## Refer Video
https://www.youtube.com/watch?v=99RVfqklbCE
