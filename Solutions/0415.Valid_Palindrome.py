"""
Description
Given a string, determine if it is a palindrome, considering only letters are considered and case is ignored
Contact me on wechat to get Amazon、Google requent Interview questions . (wechat id : jiuzhang15)
Have you consider that the string might be empty? This is a good question to ask during an interview.
For the purpose of this problem, we define empty string as valid palindrome.
Example
Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama"
Example 2:
Input: "race a car"
Output: false
Explanation: "raceacar"
Challenge
O(n) time without extra memory.
"""

class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        lens = len(sgood)
        i, j = 0, lens - 1

        while i < j:
            if sgood[i] != sgood[j]:
                return False
            i += 1
            j -= 1
        return True
