"""
In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position, you can walk one step to the left, right, up, or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.
 

Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.
Example 2:

Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 15
0 <= grid[i][j] <= 100
There are at most 25 cells containing gold.
"""

"""
尝试每一个pos出发backtrack所有可能的path比较哪一条path能得到最多的gold - O( (MN)* 3^(MN) ).
每个位置都有3种选择，所以时间复杂度是3^(MN)
注意backtrack遍历得到的是每一条path的curr_sum, 而不是像普通dfs那样得遍历的是整个区域的
"""
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def backtrack(curr_i, curr_j, curr_sum):
            self.max_gold = max(self.max_gold, curr_sum)    # 注意backtrack遍历得到的是每一条path的curr_sum, 而不是像普通dfs那样得遍历的是整个区域的
            for delta_i, delta_j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n:
                    if grid[next_i][next_j] != 0:
                        if (next_i, next_j) not in visited:
                            visited.add((next_i, next_j))
                            backtrack(next_i, next_j, curr_sum + grid[next_i][next_j])
                            visited.remove((next_i, next_j))  # 就这一句remove使得backtrack遍历得到的是每一条path的curr_sum, 而不是像普通dfs那样得遍历的是整个区域的
                                                              # 对比200. Number of island, 就这一个地方不一样
        self.max_gold = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    visited = set()
                    visited.add((i, j))
                    backtrack(i, j, grid[i][j])     # 这个backtrack从(i, j)开始，所以path里一定是包含(i, j)的
        return self.max_gold
