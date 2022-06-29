"""
An additive number is a string whose digits can form an additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits, return true if it is an additive number or false otherwise.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

 

Example 1:

Input: "112358"
Output: true
Explanation: 
The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
Example 2:

Input: "199100199"
Output: true
Explanation: 
The additive sequence is: 1, 99, 100, 199. 
1 + 99 = 100, 99 + 100 = 199
 

Constraints:

1 <= num.length <= 35
num consists only of digits.
"""

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def backtrack(curr_idx, curr_comb):
            if curr_idx == len(num) - 1 and len(curr_comb) >= 3:
                return True
            
            for next_idx in range(curr_idx + 1, len(num)):
                next_num = num[curr_idx + 1 : next_idx + 1]
                if next_num[0] == "0" and len(next_num) > 1:
                    continue
                if len(curr_comb) < 2 or (len(curr_comb) >= 2 and int(next_num) == int(curr_comb[-1]) + int(curr_comb[-2])):
                    curr_comb.append(next_num)
                    if backtrack(next_idx, curr_comb):
                        return True
                    curr_comb.remove(next_num)
            return False
        
        return backtrack(-1, [])
