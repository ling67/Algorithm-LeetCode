"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
"""
#solution1:Two point
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        i, j = 0, 0
        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == m
      
"""
Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, 
and you want to check one by one to see if T has its subsequence. 
In this scenario, how would you change your code?
"""
"""
solution2: binary search: O(mlogn)
refer:https://www.youtube.com/watch?v=5daodUGSFp0
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        dic = collections.defaultdict(list)
        for i, c in enumerate(t):
            dic[c].append(i)
            
        cur = -1
        for c in s:
            if c not in dic:
                return False
            l = dic[c]
            p = bisect.bisect_left(l, cur)
            if p == len(l):
                return False
            cur = l[p] + 1
        return True




   
