"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
Example 2:


Input: matrix = [["0","1"],["1","0"]]
Output: 1
Example 3:

Input: matrix = [["0"]]
Output: 0
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.
"""

"""dp[i][j] 表示以 (i, j) 位置结尾所能组成的最大正方形的边长。返回max(dp)
初始条件是边角上的dp[i][j] = int(matrix[i][j])
只有当前 (i, j) 位置为1，dp[i][j] 才有可能大于0，否则 dp[i][j] 一定为0。当 (i, j) 位置为1，此时要看 dp[i-1][j-1], dp[i][j-1]，和 dp[i-1][j] 这三个位置，我们找其中最小的值，并加上1，就是 dp[i][j] 的当前值了，这个并不难想，毕竟不能有0存在，所以只能取交集，最后再用 dp[i][j] 的值来更新结果 res 的值即可。
特别注意：为什么up[i-1][j] 为什么能用dp[i-1][j]代替
"""

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = int(matrix[0][0])
        for i in range(1, m):
            dp[i][0] = int(matrix[i][0])
        for j in range(1, n):
            dp[0][j] = int(matrix[0][j])
            
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == "1":
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        
        return max(dp[i][j]**2 for i in range(m) for j in range(n))
