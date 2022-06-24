"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

Example 1:


Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Example 2:

Input: heights = [[2,1],[1,2]]
Output: [[0,0],[0,1],[1,0],[1,1]]
 

Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105

"""
"""
题目的意思是外围一圈的地方是water进来的地方，左上角的外围是pacific ocean water进来的地方，右下角的外围是atlantic ocean water进来的地方。
step 1: 从左上角外围的每个点出发做dfs, next_pos is a valid candidate if matrix[curr_pos] <= matrix[next_pos], 
如果能visited就存起来表示pacific ocean water可以到达这个pos；
step 2: 同样的方法记录atlantic ocean water可以达到的pos.  然后用2nd pass 来找到哪些点是两个ocean都能到达的。
"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(curr_i, curr_j, visited):
            visited.add((curr_i, curr_j))
            for delta_i, delta_j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n:
                    if (next_i, next_j) not in visited and heights[next_i][next_j] >= heights[curr_i][curr_j]:   #判断四周是不是大于当前
                        dfs(next_i, next_j, visited)
        
        m, n = len(heights), len(heights[0])
        #从pacific ocean 边界开始判断每个是不是可以流向太平洋
        pacific_visited = set()
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 and (i, j) not in pacific_visited:
                    dfs(i, j, pacific_visited)
                    
        #atlantic ocean 边界开始判断每个是不是可以流向太平洋
        atlantic_visited = set()
        for i in range(m):
            for j in range(n):
                if i == m - 1 or j == n - 1 and (i, j) not in atlantic_visited:
                    dfs(i, j, atlantic_visited)
    
        #得到既可以流向太平洋又可以流向大西洋的点
        res = []
        for i in range(m):
            for j in range(n):
                if (i, j) in pacific_visited and (i, j) in atlantic_visited:
                    res.append([i, j])
        return res
