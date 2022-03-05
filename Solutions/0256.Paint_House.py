"""
There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by an n x 3 cost matrix costs.

For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is the cost of painting house 1 with color green, and so on...
Return the minimum cost to paint all houses.

 

Example 1:

Input: costs = [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
Minimum cost: 2 + 5 + 3 = 10.
Example 2:

Input: costs = [[7,6,2]]
Output: 2
 

Constraints:

costs.length == n
costs[i].length == 3
1 <= n <= 100
1 <= costs[i][j] <= 20
"""

"""
1.确定状态：dp[i][0]  dp[i][1] dp[i][2]  油漆前i+1栋房子，且第i+1栋房子是红色，蓝色，绿色的最小花费
2.求：min dp[n-1]  油漆前n栋房子的最少花费  
3.初始化：dp[0][0]  油漆前0栋房子 = costs[][], costs[][], costs[][]
4.递推公式：dp[n-1][0] = min{dp[n][1], dp[n][2]}
"""

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        
        dp = [[0] * 3 for _ in range(n)]
        dp[0][0], dp[0][1], dp[0][2] = costs[0][0], costs[0][1], costs[0][2] 
        
        for i in range(1, n):
            dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2]) 
            dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2]) 
            dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1]) 
        
        return min(dp[-1])
        
