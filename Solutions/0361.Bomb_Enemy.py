"""
Given an m x n matrix grid where each cell is either a wall 'W', an enemy 'E' or empty '0', return the maximum enemies you can kill using one bomb. You can only place the bomb in an empty cell.

The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since it is too strong to be destroyed.

 

Example 1:


Input: grid = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
Output: 3
Example 2:


Input: grid = [["W","W","W"],["0","0","0"],["E","E","E"]]
Output: 1
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid[i][j] is either 'W', 'E', or '0'.
"""


"""
DP解法: 把(i, j)位置能炸死多少敌人提前计算好放入二维数组中
up[i][j]=在(i,j)位置能向上炸的敌人数目
if (i,j) 是墙：up[i][j] = 0
if (i,j) 是空地：up[i][j] = 0; up[i][j] += up[i-1][j]
if (i,j) 是敌人：up[i][j] = 1; up[i][j] += up[i-1][j] 
同理算出down[i][j], left[i][j], right[i][j]
然后能炸的敌人数目为up+down+left+right
time O(M*N)  space O(M*N)
"""
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        res = [[0] * n for _ in range(m)]
        
        #up
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "W":
                    dp[i][j] = 0
                else:
                    dp[i][j] = 0
                    if grid[i][j] == "E":
                        dp[i][j] = 1
                        
                    if i - 1 >= 0:
                        dp[i][j] += dp[i-1][j]
                res[i][j] += dp[i][j]
        
        # down
        for i in range(m - 1, -1, -1):
            for j in range(n):
                if grid[i][j] == "W":
                    dp[i][j] = 0
                else:
                    dp[i][j] = 0
                    if grid[i][j] == "E":
                        dp[i][j] = 1
                    
                    if i + 1 < m:
                        dp[i][j] += dp[i + 1][j]
                        
                res[i][j] += dp[i][j]            
                    
        # left
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "W":
                    dp[i][j] = 0
                else:
                    dp[i][j] = 0
                    if grid[i][j] == "E":
                        dp[i][j] = 1
                        
                    if j - 1 >= 0:
                        dp[i][j] += dp[i][j - 1]
                        
                res[i][j] += dp[i][j]
                
        # right
        for i in range(m):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == "W":
                    dp[i][j] = 0
                else:
                    dp[i][j] = 0
                    if grid[i][j] == "E":
                        dp[i][j] = 1
                        
                    if j + 1 < n:
                        dp[i][j] += dp[i][j + 1]
                        
                res[i][j] += dp[i][j]
                
        maxRes = 0        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    maxRes = max(maxRes, res[i][j])
                    
        return maxRes
