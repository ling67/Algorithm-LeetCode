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
