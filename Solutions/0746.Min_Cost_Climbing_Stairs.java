/*
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.

*/


"""
python
1.define state dp[i] the minimum cost to reach the ith floor
2.get dp[n]
3.initialize dp[0] = cost[0] dp[1] = cost[1]
4.transit function dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 0 
        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[n]
        

//1.定义状态 dp[i] 代表到达第i staircase需要的最小的cost
//2.求dp[n]
//3.初始化 dp[0] = 0; dp[1] = 0; dp[2] = min(A[0], A[1])
//4.递推公式 dp[i] = min(dp[i-1] + A[i-1], dp[i-2] + A[i-2]);
class Solution {
    public int minCostClimbingStairs(int[] cost) {
        if (cost == null || cost.length == 0 || cost.length == 1) {
            return 0;
        }
        int n = cost.length;
        int dp[] = new int[n+1]; //注意n+1，求的是dp[n];
        dp[0] = 0; dp[1] = 0;
        for (int i = 2; i < n+1; i++) {
            dp[i] = Math.min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2]);
        }
        return dp[n];
    }
}


