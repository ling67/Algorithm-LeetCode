//1.状态定义dp[i] 从下至上到达第i个台阶的时候有的不同的方法
//2.求dp[n]
//3.初始化 dp[1] = 1 dp[2] = 2
//4.递推公式 dp[n] = dp[n-1] + dp[n-2]
class Solution {
    public int climbStairs(int n) {
        int dp[] = new int[n + 1];
        if (n == 1) return 1;
        dp[1] = 1;
        dp[2] = 2;

        for(int i = 3; i < n + 1; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[n];
    }
}
