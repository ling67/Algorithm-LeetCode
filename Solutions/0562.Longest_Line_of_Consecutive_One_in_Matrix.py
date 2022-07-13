"""
Given an m x n binary matrix mat, return the length of the longest line of consecutive one in the matrix.

The line could be horizontal, vertical, diagonal, or anti-diagonal.

 

Example 1:


Input: mat = [[0,1,1,0],[0,1,1,0],[0,0,0,1]]
Output: 3
Example 2:


Input: mat = [[1,1,1,1],[0,1,1,0],[0,0,0,1]]
Output: 4
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
"""

"""
Solution 1 :brute force
each time we meet a 1, we explore horizontally, vertically and diagonally.
Use set to store the nodes that were horizontally visited, vertically visited and diagonally visited. 
"""
class Solution:
    def longestLine(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        h_visited = set()   # store the nodes that were horizontally visited
        v_visited = set()
        d_visited = set()
        ad_visited = set()  # store the nodes that were anti-diagonally visited
        m, n = len(matrix), len(matrix[0])
        max_len = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if (i, j) not in h_visited:
                        p, q = i, j
                        while p < m and matrix[p][q] == 1:
                            h_visited.add((p, q))
                            p += 1
                        max_len = max(max_len, p - i)
                    
                    if (i, j) not in v_visited:
                        p, q = i, j
                        while q < n and matrix[p][q] == 1:
                            v_visited.add((p, q))
                            q += 1
                        max_len = max(max_len, q - j)
                    if (i, j) not in d_visited:
                        p, q = i, j
                        while p < m and q < n and matrix[p][q] == 1:
                            d_visited.add((p, q))
                            p += 1
                            q += 1
                        max_len = max(max_len, p - i)
                    if (i, j) not in ad_visited:
                        p, q = i, j
                        while p < m and q >= 0 and matrix[p][q] == 1:
                            ad_visited.add((p, q))
                            p += 1
                            q -= 1
                        max_len = max(max_len, p - i)
        return max_len
      
# Solution 2: 3D dp      
class Solution:
    """
    - dp (3D) dp[i][j] = [vertical line length, horizontal line length, diagnal line length, anti-diagonal line length]
    - time: O(mn), space: O(mn)
    """
    def longestLine(self, M: List[List[int]]) -> int:
        
        if not M or not M[0]:
            return 0
        
        max_length = 0
        m, n = len(M), len(M[0])
        dp = [[[0] * 4 for _ in range(n + 2)] for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if M[i][j] == 1:
                    dp[i + 1][j + 1] = [dp[i][j + 1][0] + 1,dp[i + 1][j][1] + 1, dp[i][j][2] + 1, dp[i][j + 2][3] + 1]
                    max_length = max(max_length, max(dp[i + 1][j + 1]))
        return max_length
      
# Solution 2: 2D dp      
"""
    - dp (2D) - only need to keep track of prev line status to calculate current line status
    - time: O(mn), space: O(n)
    """
    def longestLine(self, M: List[List[int]]) -> int:
        
        if not M or not M[0]:
            return 0
        
        max_length = 0
        m, n = len(M), len(M[0])
        prev = [[0] * 4 for _ in range(n + 2)]
        for i in range(m):
            curr = [[0] * 4 for _ in range(n + 2)]
            for j in range(n):
                if M[i][j] == 1:
                    curr[j + 1] = [prev[j + 1][0] + 1, curr[j][1] + 1, prev[j][2] + 1, prev[j + 2][3] + 1]
                    max_length = max(max_length, max(curr[j + 1]))
            prev = curr
        return max_length

