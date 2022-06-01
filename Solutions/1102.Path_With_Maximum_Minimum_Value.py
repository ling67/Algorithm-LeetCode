"""
Given an m x n integer matrix grid, return the maximum score of a path starting at (0, 0) and ending at (m - 1, n - 1) moving in the 4 cardinal directions.

The score of a path is the minimum value in that path.

For example, the score of the path 8 → 4 → 5 → 9 is 4.
 

Example 1:


Input: grid = [[5,4,5],[1,2,6],[7,4,6]]
Output: 4
Explanation: The path with the maximum score is highlighted in yellow. 
Example 2:


Input: grid = [[2,2,1,2,2,2],[1,2,2,2,1,2]]
Output: 2
Example 3:


Input: grid = [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
0 <= grid[i][j] <= 109
"""

class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        hq = [(-grid[0][0], 0, 0)]   # max heap for (min_val_in_the_path_to_curr_pos, curr_pos)
        max_minvals = defaultdict(int)  # curr_pos --> the maximum minval in the path, 这个extra space必不可少是用来换时间的
        
        while len(hq) > 0:
            curr_minval, curr_i, curr_j = heappop(hq)   # 每次pop出来的都是minval最大的path, 我们选择这个path走
            curr_minval = -curr_minval
            
            if (curr_i, curr_j) == (m - 1, n - 1):
                return curr_minval
            
            if (curr_i, curr_j) in max_minvals:
                continue
            max_minvals[(curr_i, curr_j)] = curr_minval
            
            for delta_i, delta_j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n:
                    next_minval = min(curr_minval, grid[next_i][next_j])    # ***** 注意这里很容易错，我们要的是path里面的最大的minval, 
                    heappush(hq, (-next_minval, next_i, next_j))  # 所以我们把每个path里面的minval放入max heap, 这样我们每次pop出来的都是path里面最大的那个最小值
              

