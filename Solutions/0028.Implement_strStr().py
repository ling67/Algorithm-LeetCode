"""
Implement strStr().

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

 

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""

"""
A good application of this strStr() problem is that it can be used as an API for solving the problem of check if T2 is subtree of T1 ,both are very large trees.
572. Subtree of Another Tree
https://leetcode.com/discuss/interview-question/738978/Amazon-Onsite-or-check-if-T2-is-subtree-of-T1-both-are-very-large-trees
https://www.geeksforgeeks.org/check-binary-tree-subtree-another-binary-tree-set-2/
"""

# 暴力法 O(M*N)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        
        for i in range(len(haystack) + 1 - len(needle)):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
                if j == len(needle) - 1:
                    return i
        return -1
      
#KMP不会优化      

      
