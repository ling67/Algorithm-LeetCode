/*
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row. 

Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
*/

//python

"""
1.define state dp[i][j] represent the minimus path sum to (i, j)
2.get result min{dp[i][n-1]}
3.initialize dp[i][0] = dp[i-1][0] + triangle[i][0]
4.transit function dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
"""
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        dp = [[0] * m for _ in range(m)]
        dp[0][0] = triangle[0][0]
        
        for i in range (1, m):
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            dp[i][i] = dp[i-1][i-1] + triangle[i][i]
            
        for i in range(1, m):
            for j in range(1, i):
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
        
        return min(dp[m-1])
                
        
/*
1.状态定义: dp[i][j] = 从坐标(i,j)出发，到达最底层的最小路径和
2.求dp[0][0];
3.初始条件 dp[n-1][j] = A[n-1][j]
4.递推公式： dp[i][j] = A[i][j] + min(dp[i+1][j], dp[i+1][j+1])
*/

class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int m = triangle.size();
        int dp[][] = new int[m][m];
        for (int j = 0; j < m; j++) {
            dp[m-1][j] = triangle.get(m-1).get(j);
        }
        
        for (int i = m - 2; i >= 0; i--) {
            for (int j = 0; j <= i; j++) {
                dp[i][j] = triangle.get(i).get(j) + Math.min(dp[i+1][j], dp[i+1][j+1]);
            }
        }
        return dp[0][0]; 
    }
}


//version 2
/*
1.状态定义: dp[i][j] = 从坐标(0,0)出发，到达坐标（i, j）的最小路径和
2.求dp[n-1][j]中最小的一个;
3.初始条件 dp[0][0] = A[0][0]
4.递推公式： dp[i][j] = A[i][j] + min(dp[i-1][j-1], dp[i-1][j])
O(m*m)
*/

class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int m = triangle.size();
        int dp[][] = new int[m][m];
        dp[0][0] = triangle.get(0).get(0);
        
        for (int i = 1; i < m; i++) {
            dp[i][0] = dp[i-1][0] + triangle.get(i).get(0);
            dp[i][i] = dp[i-1][i-1] + triangle.get(i).get(i);
        }
        
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < i; j++) {
                dp[i][j] = triangle.get(i).get(j) + Math.min(dp[i-1][j-1], dp[i-1][j]);
            }
        }
        
        int min = dp[m-1][0];
        for(int j = 0; j < m; j++) {
            min = min > dp[m-1][j] ? dp[m-1][j] : min;
        }
        
        return min;
    }
}


