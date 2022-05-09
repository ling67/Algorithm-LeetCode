"""
There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by an n x k cost matrix costs.

For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on...
Return the minimum cost to paint all houses.

 

Example 1:

Input: costs = [[1,5,3],[2,9,4]]
Output: 5
Explanation:
Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5; 
Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5.
Example 2:

Input: costs = [[1,3],[2,4]]
Output: 5
 

Constraints:

costs.length == n
costs[i].length == k
1 <= n <= 100
2 <= k <= 20
1 <= costs[i][j] <= 20
"""

"""
python version 1
1.define state dp[i][0] represent hourse 0...i-1 has painted and i paint by color 0
2.get min{dp[n-1][0....k-1]}
3.initialize dp[0][0]....dp[0][k-1] = cost[0][0]...cost[0][k-1]
4.dp[i][j] = min{dp[i-1][0]...dp[i-1][j-1]...dp[i-1][j+1]...dp[i-1][k-1]} + cost[i][j]
"""
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n, k = len(costs), len(costs[0])
        dp = [[0] * k for _ in range(n)]
        for i in range(k):
            dp[0][i] = costs[0][i]
        
        for i in range(1, n):
            for j in range(k):
                minValue = float('inf')
                for t in range(k):
                    if t != j:
                        minValue = min(minValue, dp[i-1][t])
                dp[i][j] =  minValue + costs[i][j]
                
        return min(dp[-1])

"""
python version 2
跟之前不一样的是变成了K个颜色

优化成O(N*K)，因为每次都需要求出最小值，如果我们记录最小值就可以减小计算量了
提前计算好的思想非常重要，后面的1289. Minimum Falling Path Sum II也会用到
1.define state dp[i][0] represent hourse 0...i-1 has painted and i paint by color 0
2.get min{dp[n-1][0....k-1]}
3.initialize dp[0][0]....dp[0][k-1] = cost[0][0]...cost[0][k-1]
4.dp[i][j] = min{dp[i-1][0]...dp[i-1][j-1]...dp[i-1][j+1]...dp[i-1][k-1]} + cost[i][j]

k*k*n
"""
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n, k = len(costs), len(costs[0])
        dp = [[0] * k for _ in range(n)]
        dp[0] = costs[0]
        
        for i in range(1, n):
            
            # Step 1: find the position for the first and second minimum in dp[i - 1]
            min_1, min_2 = float("inf"), float("inf")
            j_1, j_2 = -1, -1
            for j in range(k):
                if dp[i-1][j] <= min_1:
                    min_1, min_2 = dp[i - 1][j], min_1
                    j_1, j_2 = j, j_1
                else:
                    if min_1 < dp[i-1][j] < min_2:
                        min_2 = dp[i - 1][j]
                        j_2 = j
                    
            # step 2: update dp[i] based on the minimums found in dp[i-1]
            for j in range(k):
                if j != j_1:
                    dp[i][j] = min_1 + costs[i][j]
                else:
                    dp[i][j] = min_2 + costs[i][j]
        
        return min(dp[-1])
