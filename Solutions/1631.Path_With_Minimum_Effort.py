"""
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

 

Example 1:



Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
Example 2:



Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
Example 3:


Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.
 

Constraints:

rows == heights.length
columns == heights[i].length
1 <= rows, columns <= 100
1 <= heights[i][j] <= 106
"""

"""
有多条路径，求出每条路径的最大差值
求最大差值中的最小值
hint:将最大路径差值放入heap，每次pop出最小值，然后沿着这个方向走，最后出来的就是最大差值中的最小值
"""
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        hq = [(0, 0, 0)]   #存储到当前为止，两个节点之间最大的diff
        min_maxcosts = defaultdict(int)   #max absolute diff -> min 说明路越平
        while len(hq) > 0:
            curr_maxcost, curr_i, curr_j = heappop(hq)
            if (curr_i, curr_j) == (m - 1, n - 1):
                return curr_maxcost
            
            if (curr_i, curr_j) in min_maxcosts:
                continue
            min_maxcosts[(curr_i, curr_j)] = curr_maxcost
            
            for delta_i, delta_j in [(1,0),(-1,0),(0,1),(0,-1)]:
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n:
                    next_maxcost = max(curr_maxcost, abs(heights[next_i][next_j] - heights[curr_i][curr_j]))
                    heappush(hq, (next_maxcost, next_i, next_j))
