"""
A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.

We can rotate digits of a number by 180 degrees to form new digits.

When 0, 1, 6, 8, and 9 are rotated 180 degrees, they become 0, 1, 9, 8, and 6 respectively.
When 2, 3, 4, 5, and 7 are rotated 180 degrees, they become invalid.
Note that after rotating a number, we can ignore leading zeros.

For example, after rotating 8000, we have 0008 which is considered as just 8.
Given an integer n, return the number of confusing numbers in the inclusive range [1, n].

 

Example 1:

Input: n = 20
Output: 6
Explanation: The confusing numbers are [6,9,10,16,18,19].
6 converts to 9.
9 converts to 6.
10 converts to 01 which is just 1.
16 converts to 91.
18 converts to 81.
19 converts to 61.
Example 2:

Input: n = 100
Output: 19
Explanation: The confusing numbers are [6,9,10,16,18,19,60,61,66,68,80,81,86,89,90,91,98,99,100].
 

Constraints:

1 <= n <= 109
"""

#solution1: brute force 超时
class Solution:
    def confusingNumberII(self, n: int) -> int:
        cnt = 0
        for i in range(1, n + 1):
            if self.confusingNumber(i):
                cnt += 1
        return cnt
    
    def confusingNumber(self, n):
        mapping = {"0":"0","1":"1","6":"9","8":"8","9":"6"}
        s = str(n)
        rotated = ""
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in mapping:
                return False
            rotated += mapping[s[i]]
        return rotated != s

#solution2: backtrack 超时
""" 
backtrack结束条件: int(curr_comb) in range [1, N +1] and curr_comb is confusing nubmer
constraints on next_candidates: has to come from mapping, cannot have leading zero
arguments pass into function: curr_comb
time complexity: O(M*5^M)
"""

class Solution:
    def confusingNumberII(self, N: int) -> int:
        mapping = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        
        def backtrack(curr_comb):
            if 1 <= int(curr_comb) <= N and curr_comb != "".join([mapping[ch] for ch in curr_comb[::-1]]):
                res.add(curr_comb)
            
            if int(curr_comb) >= N:
                return
                
            for next_num in mapping:
                backtrack(curr_comb + next_num)
        
        
        res = set()
        for num in ["1", "6", "8", "9"]:
            backtrack(num)
        return len(res)

