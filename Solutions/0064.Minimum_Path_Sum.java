/*
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
*/

"""
1.确定状态 dp[i][j] 表示到坐标[i+1][j+1]的最小路径和
2.求 dp[m-1][n-1]
3.初始化 dp[0][0] = grid[0][0]
4.递推公式 dp[m-1][n-1] = grid[m-1][n-1] + min{dp[m-2][n-1], dp[m-1][n-2]}
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        
        #初始化
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
                
        return dp[-1][-1]

//1.状态定义 dp[i][j] = 从（0，0）出发到（i, j）的最短距离和
//2.求dp[m-1][n-1];
//3.初始化：dp[0][0] = A[0][0]; dp[i][0] = dp[i-1][0] + A[i][0]; dp[0][j] = dp[0][j-1] + A[0][j]
//4.递推公式：dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + A[i][j]

class Solution {
    public int minPathSum(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        
        int dp[][] = new int[m][n];
        dp[0][0] = grid[0][0];
        for (int i = 1; i < m; i++) {
            dp[i][0] = dp[i-1][0] + grid[i][0];   //注意不要漏掉加上grid[i][0]
        }
        for (int j = 1; j < n; j++) {
            dp[0][j] = dp[0][j-1] + grid[0][j]; 
        }
        
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = Math.min(dp[i-1][j], dp[i][j-1]) + grid[i][j];
            }
        }
        return dp[m-1][n-1];
    }
}
