/*
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.

 

Example 1:


Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
Example 2:


Input: obstacleGrid = [[0,1],[0,0]]
Output: 1

*/

/*
1.状态定义dp[i][j]代表从（0，0）出发到达（i，j）的路径条数
2.求dp[m-1][n-1]
3.初始化 
if obstacleGrid[0][0] = 1 dp[0][0] = 0;  dp[i][0] = 0  dp[0][j] = 0;
obstacleGrid[0][0] = 0 dp[0][0] = 1; dp[i][0] = dp[i-1][0]  dp[0][j] = dp[0][j-1];
4.递推公式 if obstacleGrid[i][j] = 0 dp[i][j] = dp[i][j-1] + dp[i-1][j]
*/
class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;
        int dp[][] = new int[m][n];
        
        dp[0][0] = obstacleGrid[0][0] == 1 ? 0 : 1;
        for (int i = 1; i < m; i++) {
            dp[i][0] = obstacleGrid[i][0] == 1 ? 0 : dp[i-1][0];
        }   
        for (int j = 1; j < n; j++) {
            dp[0][j] = obstacleGrid[0][j] == 1 ? 0 : dp[0][j-1];
        }  
        
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = obstacleGrid[i][j] == 1 ? 0 : (dp[i][j-1] + dp[i-1][j]);
            }
        }
        return dp[m-1][n-1];
    }
}
