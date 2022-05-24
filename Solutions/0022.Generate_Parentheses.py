"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(left_cnt, right_cnt, curr_comb):
            if left_cnt == right_cnt == n:
                res.append(curr_comb)   # string doesn't need deep copy because it is immutable
                return
            if right_cnt > left_cnt:    # 这个判断尤为关键 - strong pruning
                return
            if left_cnt < n:
                backtrack(left_cnt + 1, right_cnt, curr_comb + "(")
            if right_cnt < n:
                backtrack(left_cnt, right_cnt + 1, curr_comb + ")")
                
        res = []
        backtrack(0, 0, "")
        return res

