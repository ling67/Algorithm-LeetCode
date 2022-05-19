"""
You are given two strings s and t of the same length and an integer maxCost.

You want to change s to t. Changing the ith character of s to ith character of t costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII values of the characters).

Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of t with a cost less than or equal to maxCost. If there is no substring from s that can be changed to its corresponding substring from t, return 0.

 

Example 1:

Input: s = "abcd", t = "bcdf", maxCost = 3
Output: 3
Explanation: "abc" of s can change to "bcd".
That costs 3, so the maximum length is 3.
Example 2:

Input: s = "abcd", t = "cdef", maxCost = 3
Output: 1
Explanation: Each character in s costs 2 to change to character in t,  so the maximum length is 1.
Example 3:

Input: s = "abcd", t = "acde", maxCost = 0
Output: 1
Explanation: You cannot make any change, so the maximum length is 1.
 

Constraints:

1 <= s.length <= 105
t.length == s.length
0 <= maxCost <= 106
s and t consist of only lowercase English letters.
"""

"""
step 1: construct a cost arr; step 2: sliding window to solve the problem of 
finding the max lens of subarry with sum at most target
用第二种模板：find max subarray size for at most problem.
"""

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost = [abs(ord(t[i]) - ord(s[i])) for i in range(len(s))]   #注意这里绝对值
        i = 0 
        max_len = 0
        sum_cost = 0
        for j in range(len(s)):
            sum_cost += cost[j]
            
            while i <= j and sum_cost > maxCost:
                sum_cost -= cost[i]
                i += 1
                
            if sum_cost <= maxCost:
                max_len = max(max_len, j - i + 1)
        return max_len

