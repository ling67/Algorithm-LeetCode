"""
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

 

Example 1:


Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
Example 2:

Input: board = [["X"]]
Output: [["X"]]
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
"""

"""
dfs
从边界开始，访问所有能访问到的o,放入visited中，最后翻转，如果不在visited中输出X
"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(curr_i, curr_j):
            visited.add((curr_i, curr_j))
            for delta_x, delta_y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_x, next_y = curr_i + delta_x, curr_j + delta_y
                if 0 <= next_x < m and 0 <= next_y < n:
                    if (next_x, next_y) not in visited and board[next_x][next_y] == 'O':
                        dfs(next_x, next_y)
        
        m, n = len(board), len(board[0])
        visited = set()
        for i in range(m):
            for j in range(n):
                if i not in (0, m - 1) and j not in (0, n - 1):
                    continue
                if (i, j) in visited:
                    continue
                if board[i][j] == 'X':
                    continue
                dfs(i, j)
                
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i, j) not in visited:
                    board[i][j] = 'X'
        return board
                
