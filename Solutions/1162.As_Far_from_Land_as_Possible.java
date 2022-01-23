/*
Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

 

Example 1:


Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.
Example 2:


Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.
*/

/*
1.暴力法：对每一个water做BFS记录最大值
2.对每一个land,找最近的water, 即找到所有water的最大值
*/
class Solution {
    public int maxDistance(int[][] grid) {
        
        Queue<Pair> queue = new LinkedList<>();
        Set<Pair> set = new HashSet<>();
        int layer = -1;
        
        int m = grid.length;
        int n = grid[0].length;
        
        //把所有陆地加入queue
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    Pair p = new Pair(i, j);
                    queue.offer(p);
                    set.add(p);
                }
            }
        }
        
        //没有陆地或者没有水
        if (queue.size() == 0 || queue.size() == m * n) {
            return -1;
        }
        
        int[] directionX = {-1, 0, 1, 0};
        int[] directionY = {0, 1, 0, -1};
            
        while (!queue.isEmpty()) {
            layer++;
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                Pair<Integer, Integer> p = queue.poll();
                for (int j = 0; j < 4; j++) {
                    int row = p.getKey() + directionX[j];
                    int column = p.getValue() + directionY[j];
                    Pair<Integer, Integer> cur = new Pair(row, column);
                    if (!inBound(grid, row, column)) {
                        continue;
                    }
                    if (grid[row][column] == 0 && !set.contains(cur)) {
                        queue.offer(cur);
                        set.add(cur);
                    }
                }
            }
        }
        return layer;
    }
    
    private boolean inBound(int[][] grid, int row, int column) {
        int m = grid.length;
        int n = grid[0].length;
        
        return row >= 0 && row < m && column >= 0 && column < n;
    }
    
}
