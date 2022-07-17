"""
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

 

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
 

Constraints:

1 <= k <= num.length <= 105
num consists of only digits.
num does not have any leading zeros except for the zero itself.
"""

"""
refer:https://www.youtube.com/watch?v=dDJX1ZL8ZOw&t=10s
使用栈维护使得序列变成不
step 1: 用一个栈，用来维护序列，使得每次遇到比前面的数都小就把前面的数pop掉，是的序列是一个不降的序列
step 2: 删完所有数字之后，还剩下其他数字，就从末尾开始删除
"""
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return '0'
        stack = []
        for n in num:
            #step 1
            while k and stack and n < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(n)
        for i in range(k):
            stack.pop()
            
        # deal with "0"开头的数字
        i = 0
        while i < len(stack) and stack[i] == "0":  # deal with "0"开头的数字
            i += 1

        return "0" if i == len(stack) else "".join(stack[i:])

