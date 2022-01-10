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


