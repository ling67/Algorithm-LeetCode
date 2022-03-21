/*
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
*/

//python bfs 
class Solution:
    
    EMPTY = 0
    FRESH = 1
    ROTTEN = 2
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == self.ROTTEN:
                    q.append((i,j))
        
        minutes = -1
        while q:
            minutes += 1
            size = len(q)
            for _ in range(size):
                cur_i, cur_j = q.popleft()
                for delta_i, delta_j in [(1,0),(-1,0),(0,-1),(0,1)]:
                    nei_i, nei_j = cur_i + delta_i, cur_j + delta_j
                    if 0 <= nei_i < m and 0 <= nei_j < n:
                        if grid[nei_i][nei_j] == self.FRESH:
                            q.append((nei_i, nei_j))
                            grid[nei_i][nei_j] = self.ROTTEN
        for i in range(m):
            for j in range(n):
                if grid[i][j] == self.FRESH:    # 如果还有访问不到的FRESH, 那就return -1
                    return -1
        return 0 if minutes == -1 else minutes  # 如果minutes=-1, 那说明最开始就没有ROTTEN的进q里去
            

//Coordinate可以改成pair做
class Solution {
    
    class Coordinate {
        int x, y;
        public Coordinate(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    
    public int orangesRotting(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int sumNum = 0;
        int layer = -1; //record the minimum number of minutes
        
        Queue<Coordinate> queue = new LinkedList<>();
        Set<Coordinate> set = new HashSet<>();
        
        //统计橙子数量
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++ ) {
                if (grid[i][j] == 2) {
                    Coordinate co = new Coordinate(i, j);
                    queue.offer(co);    //讲起始的坏橘子放进队列
                    set.add(co);
                    sumNum++;
                }
                if (grid[i][j] == 1) {
                    sumNum++;
                }
            }
        }
        
        if (sumNum == 0) {
            return 0;
        }
        
        //方向：右-下-左-上
        int[] directionX = {0, 1, -1, 0};
        int[] directionY = {1, 0, 0, -1};
        
        while (!queue.isEmpty()) {
            layer++;
            if(set.size() == sumNum) {
                return layer;
            }
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                Coordinate cur = queue.poll();
                for (int j = 0; j < 4; j++) {
                    Coordinate adj = new Coordinate(cur.x + directionX[j], cur.y + directionY[j]);
                    if (!inBound(adj, grid)) {
                        continue;
                    }
                    if (grid[adj.x][adj.y] == 1 && !set.contains(adj)) {
                        grid[adj.x][adj.y] = 2;
                        queue.offer(adj);
                        set.add(adj);
                    }
                }
            }
        }
        return -1;
    }
    
    //判断给出的点是否是数组合法边界, 在里面return true
    private boolean inBound(Coordinate cur, int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        return cur.x >= 0 && cur.x < m && cur.y >= 0 && cur.y < n; 
    }
    
}
