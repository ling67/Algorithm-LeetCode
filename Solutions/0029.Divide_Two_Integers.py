"""
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

 

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.
"""


# version 1 brute force, time complexity O(n)

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        d = abs(dividend)
        dv = abs(divisor)
        output = 0
        
        while d >= dv:
            d -= dv
            output += 1
        
        if (dividend < 0 and divisor >= 0) or (divisor < 0 and dividend >= 0):
            output = -output
        
        return output
       
// time complexity logn       
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (dividend < 0) == (divisor < 0)
        a, b = abs(dividend), abs(divisor)
        
        res = 0
        while a >= b:
            shift = 0   #shift多少次就是乘以多少次2
            while a >= (b << (shift + 1)):   #b往左移动shift+1位，就是乘以2^(shift + 1)
                shift += 1    #知道找到最大的shift
            res += 1 << shift   #提取除数
            a -= b << shift  #提取余数
        
        return min(res if sign else -res, 2**31-1)
      

