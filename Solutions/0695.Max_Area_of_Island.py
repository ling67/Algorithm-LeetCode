/*
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 

Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
*/

//version python bfs
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def bfs(curr_i, curr_j):
            q = deque()
            q.append((curr_i,curr_j))
            visited.add((curr_i, curr_j))
            
            cnt = 0
            while q:
                curr_i, curr_j = q.popleft()    #注意：这里是curr_i,curr_j, 不是curr
                cnt += 1
                for delta_i, delta_j in [(1,0),(-1,0),(0,1),(0,-1)]:
                    next_i, next_j = delta_i + curr_i, delta_j + curr_j
                    if 0 <= next_i < m and 0 <= next_j < n and grid[next_i][next_j] == 1:
                        if (next_i, next_j) not in visited:
                            q.append((next_i, next_j))
                            visited.add((next_i, next_j))   #注意：visited 和 q是一对，一定要一起加
            return cnt
                            
        
        m, n = len(grid), len(grid[0])
        visited=set()
        max_cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:   #注意：这里不要忘记判断（i，j）不在visited中
                    max_cnt = max(max_cnt, bfs(i,j))
        return max_cnt
        

//version python dfs
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #返回以curr_i, curr_j为起点的面积
        def dfs(curr_i, curr_j):
            cnt = 1
            visited.add((curr_i, curr_j))
            for delta_i, delta_j in [(1,0),(-1,0),(0,1),(0,-1)]:
                next_i, next_j = delta_i+curr_i, delta_j+curr_j
                if 0<=next_i<m and 0<=next_j<n and grid[next_i][next_j] == 1:
                    if (next_i, next_j) not in visited:
                        cnt += dfs(next_i, next_j)
            return cnt
        
        m, n = len(grid), len(grid[0])
        max_cnt = 0
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_cnt = max(max_cnt, dfs(i, j))
        return max_cnt


class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int max = 0;
        int m = grid.length;
        int n = grid[0].length;
         
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    int num = dfs(i, j, grid);
                    max = (num > max ? num : max);
                }
            }
        }
        return max;
    }

    //返回以x.y为起点的面积
    public int dfs(int x, int y, int[][] grid) {
        
        int count = 1;
        //就像模板中的visited
        grid[x][y] = 0;
        
        int m = grid.length;
        int n = grid[0].length;
        
        int[] directionX = {0, 1, 0, -1};
        int[] directionY = {1, 0, -1, 0};

        for (int i = 0; i < 4; i++) {
            int neiX = x + directionX[i];
            int neiY = y + directionY[i];
            if (neiX < 0 || neiX >= m || neiY < 0 || neiY >= n) {
                continue;
            }
            if (grid[neiX][neiY] == 1) {
                count = count + dfs(neiX, neiY, grid);
            }
        }
        
        return count;
    }
}
