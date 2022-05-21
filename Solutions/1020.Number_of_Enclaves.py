/*
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

 

Example 1:


Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
Example 2:


Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.

*/

//python dfs
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(curr_i, curr_j):
            visited.add((curr_i, curr_j))
            self.cnt += 1
            if curr_i == 0 or curr_i == m-1 or curr_j == 0 or curr_j == n-1:
                self.touching_border = True  #注意：就算是true也要继续做dfs,这样可以把不符合条件的都放入visited中
            for delta_i, delta_j in [(1,0),(-1,0),(0,1),(0,-1)]:
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n and grid[next_i][next_j] == 1:
                    if (next_i, next_j) not in visited:
                        dfs(next_i, next_j)
                
        m, n = len(grid), len(grid[0])
        visited= set()
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in visited:
                    self.touching_border = False    #对象的变量，这样dfs函数也可以使用了
                    self.cnt = 0
                    dfs(i,j)
                    if not self.touching_border:
                        res += self.cnt
        return res

/*
step1: 将四周为1的连通的陆地全部变成0
step2：遍历矩阵，返回所有的陆地
*/
class Solution {
    public int numEnclaves(int[][] grid) {
        int result = 0; 
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                //如果在边上，dfs遍历所有周围的岛屿赋值成land
                if(i == 0 || j == 0 || i == grid.length - 1 || j == grid[0].length - 1) {  
                    dfs(grid, i, j);
                }
            }
        }
        
        for(int i = 0; i < grid.length; i++) {
            for(int j = 0; j < grid[0].length; j++) {
                if(grid[i][j] == 1)
                    result++;
            }
        }
        
        return result;
    }
    
    public void dfs(int[][] grid, int x, int y) {
        if (x < 0 || y < 0 || x >= grid.length || y >= grid[0].length) {
            return;
        }
        if (grid[x][y] == 1) {
            grid[x][y] = 0;
            dfs(grid, x + 1, y);
            dfs(grid, x - 1, y);
            dfs(grid, x, y + 1);
            dfs(grid, x, y - 1); 
        }
    }
}
