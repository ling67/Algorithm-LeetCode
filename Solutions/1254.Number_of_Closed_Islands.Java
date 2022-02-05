/*
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

 

Example 1:



Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).
Example 2:



Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1
Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
*/


/*
"&" will evaluate both side even the left part is false
"&&" will ignore the right part if the left part is false

res = res && dfs(grid, x + d[0], y + d[1]);
if res is false, the right dfs will not be evaluated.
for this question, we need to enter dfs(grid, x + d[0], y + d[1]) no matter what.

for example:
111
101
100
111
think about if we are in the position of 0 at (2,1) - if dfs goes to right 0 (2, 2) first, res will be false
in the meantime, we still want to dfs go to (1, 1)'s 0 to set it as 1 even res is false
问题出在了，我们会设置 grid[x][y] = 1; 就算最后结果是FALSE，有时候也设置
*/
class Solution {
    public int closedIsland(int[][] grid) {
        int count = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++ ) {
                if (grid[i][j] == 0) {
                    if(dfs(grid, i, j)) {
                        count++;
                    }
                }
            }
        }
        return count;
    }
    
    //判断连通小岛有没有在边界的情况
    public boolean dfs(int[][] grid, int x, int y) {
        if (x < 0 || y < 0 || x >= grid.length || y >= grid[0].length) {
            return false;
        }
        
        if (grid[x][y] == 1) {
            return true;
        }

        grid[x][y] = 1;
        
        //这里用位与，逻辑与有问题，有一个false后面不会调用
        return dfs(grid, x + 1, y) & dfs(grid, x - 1, y) & dfs(grid, x, y + 1) & dfs(grid, x, y - 1);
    }
}
