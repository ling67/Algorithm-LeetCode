/*
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 
Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

*/

"""
1.确定状态 dp[i][j] 从[0][0]到[i][j]的路径
2.求dp[m-1][n-1]
3.初始化 dp[0][0]=1 dp[i][0]=1 dp[0][j]=1
4.递推公式：dp[i][j] = dp[i-1][j]+dp[i][j-1]
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]   #注意二维数组初始化
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:    ## 初始条件：只有一种方法走到行为0或者列为0的地方，因为不能往左走也不能往上走
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]


//1.状态定义 dp[i][j] 代表从（0，0）出发到（i,j）总共的路径数
//2.求dp[m-1][n-1]
//3.初始化 dp[0][0] = 1, dp[i][0]=1, dp[0][j]=1;
//4.递推公式 dp[i][j] = dp[i][j-1] + dp[i-1][j];
class Solution {
    public int uniquePaths(int m, int n) {
        int dp[][] = new int[m][n];
        
        dp[0][0] = 1;
        for (int i = 1; i < m; i++) {
            dp[i][0] = 1;
        }
        for (int j = 1; j < n; j++) {
            dp[0][j] = 1;
        }
        
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = dp[i][j-1] + dp[i-1][j];
            }
        }
        return dp[m-1][n-1];
    }
}

