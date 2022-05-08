/*
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
*/

"""
python 版本
1.define state dp[i] the distinct ways climb to the i step
2.get result dp[n]
3.dp[0] = 1 dp[1] = 1 
4.transit function dp[i] = dp[i-1] + dp[i-2] 
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1]*(n+1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


//1.状态定义dp[i] 从下至上到达第i个台阶的时候有的不同的方法
//2.求dp[n]
//3.初始化 dp[1] = 1 dp[2] = 2
//4.递推公式 dp[n] = dp[n-1] + dp[n-2]
//time complexity O(n)
class Solution {
    public int climbStairs(int n) {
        if (n == 1) {
            return 1;
        }
        
        int dp[] = new int[n+1];
        dp[1] = 1;
        dp[2] = 2;
        
        for (int i = 3; i < n+1; i++) {
            dp[i] = dp[i-1] + dp[i-2];
        }
        return dp[n];
    }
}
