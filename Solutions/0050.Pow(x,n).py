/*
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
*/

//python version

"""
-3 % 2 = 1
-3 // 2 = -2
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1/x
        
        if n % 2 == 0:
            half = self.myPow(x, n // 2)
            return half * half
        else:
            half = self.myPow(x, n // 2)
            return half * half * x    
                
        return res
       
       

//recursion solution: O(logN)

class Solution {
    public double myPow(double x, int n) {
        if (n == 0) return 1;
        if (n == 1) return x;
        if (n == -1) return 1 / x;
        
        double res = 0.0;
        double half = myPow(x, n / 2);
        
        if (n % 2 == 0) {
            res = half * half;
        } else {
            if (n < 0) {
                res = 1 / x * half * half;
            } else {
                res = x * half * half;
            }
        }
        
        return res;
    }
}
