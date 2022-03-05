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
time o(m*n) space: o(m*n)
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

"""
version2： 空间优化             
1.确定状态 dp[i][j] 表示到坐标[i+1][j+1]的最小路径和
2.求 dp[m-1][n-1]
3.初始化 dp[0][0] = grid[0][0]
4.递推公式 dp[m-1][n-1] = grid[m-1][n-1] + min{dp[m-2][n-1], dp[m-1][n-2]}
O(m*n)

空间优化：由于dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
也就是说dp[i][j]只与他的前一行有关，所以计算得到了了dp[7]之后，就可以吧dp[6]之前都删掉了，因为再需要计算dp[8]的时候用不到，所以dp每次只需要保存一行数组用于后面的计算就可以了。如何实现呢？我们是用滚动数组：一开始不要开m行，之开两行dp[0][]和dp[1][]两行，初始化dp[0][]，计算dp[1][]，然后计算dp[2][]的时候就不需要dp[0][]了，把dp[2][]存到dp[0][]里面就可以了
空间就优化为O(N)了

"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(2)]
        
        #初始化
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                
                elif j == 0:
                    if i % 2 == 1:
                        dp[1][j] = dp[0][j] + grid[i][j]
                    else:
                        dp[0][j] = dp[1][j] + grid[i][j]   
                        
                else:
                    if i % 2 == 1:
                        dp[1][j] = min(dp[0][j], dp[1][j - 1]) + grid[i][j]
                    else:
                        dp[0][j] = min(dp[1][j], dp[0][j - 1]) + grid[i][j]                
                
        return dp[1][-1] if m % 2 == 0 else dp[0][-1]
 

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
