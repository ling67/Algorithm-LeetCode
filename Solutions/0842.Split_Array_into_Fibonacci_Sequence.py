"""
You are given a string of digits num, such as "123456579". We can split it into a Fibonacci-like sequence [123, 456, 579].

Formally, a Fibonacci-like sequence is a list f of non-negative integers such that:

0 <= f[i] < 231, (that is, each integer fits in a 32-bit signed integer type),
f.length >= 3, and
f[i] + f[i + 1] == f[i + 2] for all 0 <= i < f.length - 2.
Note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from num, or return [] if it cannot be done.

 

Example 1:

Input: num = "1101111"
Output: [11,0,11,11]
Explanation: The output [110, 1, 111] would also be accepted.
Example 2:

Input: num = "112358130"
Output: []
Explanation: The task is impossible.
Example 3:

Input: num = "0123"
Output: []
Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.
 

Constraints:

1 <= num.length <= 200
num contains only digits.
"""

"""
套backtrack模板即可
backtrack end condition: curr_idx == len(s) - 1.
backtrack next candidate constraint: 1. next_num should equal prev two numbers add together; 2. no leading zero; 3. next_num should be less then 2**31 - 1
backtrack should pass: (curr_idx, curr_comb)
"""

class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        def backtrack(curr_index, curr_comb):
            if curr_index == len(num) - 1 and len(curr_comb) >= 3:
                res.append(curr_comb.copy())
                return
            
            for next_index in range(curr_index + 1, len(num)):
                next_num = num[curr_index + 1: next_index + 1]
                if next_num[0] == '0' and len(next_num) > 1:
                    continue
                if int(next_num) > 2**31 - 1:        # 题目要求0 <= F[i] <= 2^31 - 1
                    continue
                if len(curr_comb) >= 2 and curr_comb[-2] + curr_comb[-1] != int(next_num):
                    continue
                curr_comb.append(int(next_num))
                backtrack(next_index, curr_comb)
                curr_comb.pop()
        res = []
        backtrack(-1, [])
        return res[0] if len(res) > 0 else []
                    
