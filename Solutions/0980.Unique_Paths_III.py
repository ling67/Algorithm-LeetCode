"""
You are given an m x n integer array grid where grid[i][j] could be:

1 representing the starting square. There is exactly one starting square.
2 representing the ending square. There is exactly one ending square.
0 representing empty squares we can walk over.
-1 representing obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

 

Example 1:


Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Example 2:


Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
Example 3:


Input: grid = [[0,1],[2,0]]
Output: 0
Explanation: There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 20
1 <= m * n <= 20
-1 <= grid[i][j] <= 2
There is exactly one starting cell and one ending cell.
"""

"""
套用backtrack模板就可以了. 每一个位置都有3种可能，所以time complexity O(3^N). 
"""
"""
backtrack结束条件：every non-obstacle squares are already visited (len(visited) == empty_cnt) and (curr_i, curr_j) == destination
constraints on next_candidates: can go to 4 neighbors
arguments pass into backtrack function: curr_i, curr_j
"""

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def backtrack(curr_i, curr_j):   #curr position and how many cell we need go 
            if len(visited) == self.empty_cnt:
                if (curr_i, curr_j) == dest:
                    self.res += 1
                return
            
            for delta_i, delta_j in [(1,0),(-1,0),(0,1),(0,-1)]:
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n and grid[next_i][next_j] != -1:
                    if (next_i, next_j) not in visited:
                        visited.add((next_i, next_j))
                        backtrack(next_i, next_j)
                        visited.remove((next_i, next_j))
            
        m, n = len(grid), len(grid[0])    
        start, dest = (0, 0), (0, 0)
        self.empty_cnt = 0
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == 1:
                    start = (i, j)
                    self.empty_cnt += 1
                elif grid[i][j] == 2:
                    dest = (i, j)
                    self.empty_cnt += 1
                elif grid[i][j] == 0:
                    self.empty_cnt += 1
        self.res = 0
        visited = set()
        visited.add(start)
        backtrack(start[0], start[1])
        return self.res
