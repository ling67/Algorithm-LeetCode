/*
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.

*/

//BFS : Python
#Complexity Analysis
#Time complexity : O(M \times N)O(M×N) where MM is the number of rows and NN is the number of columns.
#Space complexity : O(min(M, N))O(min(M,N)) because in worst case where the grid is filled with lands, the size of queue can grow up to min(M,NM,N).
 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.bfs(grid, i, j)
                    cnt += 1
        return cnt
        
    def bfs(self, grid, x, y):
        m, n = len(grid), len(grid[0])
        
        q = collections.deque()
        q.append((x, y))

        while q:
            (x, y) = q.popleft()
            for delta_x, delta_y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                adj_x, adj_y = x+delta_x, y+delta_y
                if 0 <= adj_x < m and 0 <= adj_y < n and grid[adj_x][adj_y] == "1":
                    q.append((adj_x, adj_y))
                    grid[adj_x][adj_y] = "0"
 
 //DFS python
 class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(curr_i, curr_j):
            visited.add((curr_i, curr_j))
            for delta_i, delta_j in [(1,0), (-1,0), (0,1), (0,-1)]:
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n and grid[next_i][next_j] == "1":
                    if (next_i, next_j) not in visited:
                        dfs(next_i, next_j)
        
        cnt = 0
        m, n = len(grid), len(grid[0])
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visited:   #注意这里是（i，j）not in visited
                    dfs(i, j)
                    cnt += 1
        return cnt
                        

//java version        
//标定坐标点
class Coordinate {
    int x, y;
    public Coordinate(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

class Solution {
    
    public int numIslands(char[][] grid) {
        
        //grid.length代表数组的行数  grid[0].length代表对应行的长度(即列数)
        if (grid == null || grid.length == 0 || grid[0].length == 0) {
            return 0;
        }
        
        int n = grid.length;
        int m = grid[0].length;
        int islands = 0;
        
        //遍历二位数组每个点  char：相等判断 ==  字符串判断：equals
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == '1') {
                    markByBFS(grid, i, j);
                    islands++;
                }
            }
        }
        return islands;        
    }
    
    private void markByBFS(char[][] grid, int x, int y) {
        
        //方向：右-下-左-上
        int[] directionX = {0, 1, -1, 0};
        int[] directionY = {1, 0, 0, -1};

        Queue<Coordinate> queue = new LinkedList<>();
        
        //1.起始点放入数组内
        queue.offer(new Coordinate(x, y));
        grid[x][y] = '0';
        
        //2.while循环
        while (!queue.isEmpty()) {
            Coordinate coor = queue.poll();
            for (int i = 0; i < 4; i++) {
                Coordinate adj = new Coordinate(coor.x + directionX[i], coor.y + directionY[i]);
                if (!inBound(adj, grid)) {
                    continue;
                }
                if (grid[adj.x][adj.y] == '1') {
                    grid[adj.x][adj.y] = '0';
                    queue.offer(adj);
                }
            }
        }
    } 
    
    //判断给出的点是否是数组合法边界
    private boolean inBound(Coordinate coor, char[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        return coor.x >= 0 && coor.x < n && coor.y >= 0 && coor.y < m;
    }
}

//version 2：DFS
class Solution {
    
    public int numIslands(char[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        
        int count = 0;
        
        Set<Pair<Integer, Integer>> visited = new HashSet<>();
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (visited.contains(new Pair<Integer, Integer>(i, j))) {
                    continue;
                }
                if (grid[i][j] == '1') {
                    dfs(i, j, grid, visited);
                    count++;
                }
            }
        }
        return count;
    }
    
    //遍历连成一片的小岛
    public void dfs(int x, int y, char[][] grid, Set<Pair<Integer, Integer>> visited) {
        int m = grid.length;
        int n = grid[0].length;
        
        int[] directionX = {0, 1, 0, -1};
        int[] directionY = {-1, 0, 1, 0};
        
        visited.add(new Pair<Integer, Integer>(x, y));
        for (int i = 0; i < 4; i++) {
            int neiX = x + directionX[i];
            int neiY = y + directionY[i];
            if (neiX < 0 || neiX >= m || neiY < 0 || neiY >= n ) {
                continue;
            }    
            Pair<Integer, Integer> pair = new Pair(neiX, neiY);
            if (!visited.contains(pair) && grid[neiX][neiY] == '1'){
                dfs(neiX, neiY, grid, visited);
            }    
        }
    }
}


