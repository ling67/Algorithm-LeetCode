/*
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Return the number of distinct islands.

 

Example 1:


Input: grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
Output: 1
Example 2:


Input: grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.

*/
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(org_i, org_j, curr_i, curr_j):
            visited.add((curr_i, curr_j))
            shape.append((curr_i-org_i, curr_j-org_j))  # append the relative lacation into shape
            for delta_i, delta_j in [(1,0), (-1,0), (0,1), (0,-1)]:
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n:
                    if grid[next_i][next_j] == 1 and (next_i, next_j) not in visited:
                        dfs(org_i, org_j, next_i, next_j)
        
        shapes = []
        visited = set()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    shape = []    #shape必须在外面，不能在dfs里面
                    dfs(i,j,i,j)
                    shapes.append(tuple(shape))    
        return len(set(shapes))


/*
从1开始遍历，记录下每个独立小岛的符号，用string记录小岛的符号
用set去重

为什么要加b?
Try Input [[1,1,0],[0,1,1],[0,0,0],[1,1,1],[0,1,0]], without sb.append('b') we get "ordr" for both islands, which means we move right, down then right. In order to make them different, we need to also record when we "hit a wall" and return. With sb.append('b'), we now have "ordrbbbb" and "ordbrbbb" representing two different islands.
Since it is DFS, there will be many levels of recursion, you need to know a '1' is to which point's up/down/left/right. I think "o" and "b" are used to bound a specific point in the grid. So the first time you go to a new point, you append "o". Once you finish traversing that point, append "b". You can use this example to see the difference.
*/

class Solution {
    public int numDistinctIslands(int[][] grid) {
        HashSet<String> set = new HashSet<>();
        
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] != 0) {
                    StringBuilder sb = new StringBuilder();
                    dfs(grid, i, j, sb, "o");
                    set.add(sb.toString());
                }
            }
        }
        return set.size();
    }
    
    private void dfs(int[][] grid, int i, int j, StringBuilder sb, String dir) {
        
        //判断是否越界，是否等于0，如果是就返回
        if (i < 0 || i == grid.length || j < 0 || j == grid[0].length || grid[i][j] == 0) {
            return;
        }
        sb.append(dir);
        grid[i][j] = 0;
        dfs(grid, i - 1, j, sb, "u");
        dfs(grid, i + 1, j, sb, "d");
        dfs(grid, i, j - 1, sb, "l");
        dfs(grid, i, j + 1, sb, "r");
        sb.append("b");   // 这里要append("b")特别注意
    }
    
}
