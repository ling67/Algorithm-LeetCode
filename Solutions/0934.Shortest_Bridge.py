"""
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.

 

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1
Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
 

Constraints:

n == grid.length == grid[i].length
2 <= n <= 100
grid[i][j] is either 0 or 1.
There are exactly two islands in grid.
"""

"""
memory limit exceeded.
"""

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def dfs(curr_i, curr_j):
            grid[curr_i][curr_j] = 2
            q.append((curr_i, curr_j))
            for delta_i, delta_j in [(1,0),(-1,0),(0,1),(0,-1)]:
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n and grid[next_i][next_j] == 1:
                    dfs(next_i, next_j)
                    
        #step 1找到第一个所有的小岛，标记成2，放入Q中
        q = deque()
        find = False   #exit nest for loop
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    find = True
                    break
            if find:
                break
            
        #BFS 求最短路径    
        layer = -1
        while len(q) > 0:
            size = len(q)
            layer += 1
            for _ in range(size):
                curr_i, curr_j = q.popleft()
                for delta_i, delta_j in [(1,0),(-1,0),(0,1),(0,-1)]:
                    next_i, next_j = curr_i + delta_i, curr_j + delta_j
                    if 0 <= next_i < m and 0 <= next_j < n:
                        if grid[next_i][next_j] == 0:
                            q.append((next_i, next_j))
                        elif grid[next_i][next_j] == 1:
                            return layer
                        elif grid[next_i][next_j] == 2:
                            continue
                            
        return -1
                        


