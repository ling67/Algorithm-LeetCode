"""
Given an integer n, return all the strobogrammatic numbers that are of length n. You may return the answer in any order.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

 

Example 1:

Input: n = 2
Output: ["11","69","88","96"]
Example 2:

Input: n = 1
Output: ["0","1","8"]
 

Constraints:

1 <= n <= 14
"""

"""
once the left half of the valid string s is fixed, then we can find the right half.
so we can find all combinations for n//2 lens, using backtrack.
"""
"""
O(5^(n//2))
"""
"""
find all possible permutation with of n//2 long that are composed of [0, 1, 6, 8, 9].
backtrack结束条件：len(curr_comb) == n // 2
constraint on next_candidate: cannot have leading "0"
arguments pass into backtrack function: curr_comb
"""

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        def backtrack(curr_comb):
            if len(curr_comb) == n // 2:
                res.append(curr_comb)
                return
            for next_num in ["0","1","6","8","9"]:
                if len(curr_comb) == 0 and next_num == "0":
                    continue
                backtrack(curr_comb + next_num)
                
        mapping = {"6": "9", "9": "6", "1": "1", "0": "0", "8": "8"}
        same_nums = {"1":"1", "0":"0", "8":"8"}
        res = []
        backtrack("")
        
        ans = []
        if n % 2 == 0:
            for left in res:
                right = "".join([mapping[ch] for ch in left[::-1]])
                ans.append(left + right)
        elif n % 2 == 1:
            for left in res:
                right = "".join([mapping[ch] for ch in left[::-1]])
                for ch in same_nums:
                    ans.append(left + ch + right)
        return ans
        
