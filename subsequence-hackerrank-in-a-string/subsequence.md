## What is a subsequence?
A subsequence is a **sequence that appears in the same relative order as the original sequence but not necessarily contiguous (consecutive)**.
**Unlike a substring (which must be contiguous)**, a subsequence can be formed by removing some elements without changing the order of the remaining elements.
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
* We have to iterate over the given string & subsequence and match the elements in the subsequence.
* We will move to the next element in the subsequence only if there is a match with the element in the given string (to preserve order as it will ensure that the next element in the subsequence comes only after the previous element ).
* The total number of matches should be equal to the length of the subsequence (meaning we have successfully moved through the entire small string). Else, if we reach the end of the large string without finishing the small string, it's not a subsequence.
## What Does "Preserving Order" Mean here?
* We say a sequence preserves order if characters appear in the same relative order as in the original subsequence, even if they are not consecutive.
* The **key to preserving order is moving the pointer forward only in the subsequence when a match occurs and never move backwards in the given sequence (i.e. We never reset the iteration)**.
