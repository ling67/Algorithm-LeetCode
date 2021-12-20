/*
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

 

Example 1:

Input: x = 4
Output: 2
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
 

Constraints:

0 <= x <= 231 - 1
Accepted
891,713
Submissions
2,472,427
*/

//确定答案的范围
//在范围中找答案-满不满足答案 
//注意mid * mid 会overflow
class Solution {
    public int mySqrt(int x) {
        
        if (x < 0) throw new IllegalArgumentException();
        else if (x <= 1) {
            return x;
        }
        int start = 0,  end = x;
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            if (mid == x / mid) return mid;
            else if (mid < x / mid) start = mid;
            else end = mid;
        }
        
        if (end > x / end) return start;
        return end;
    }
}
