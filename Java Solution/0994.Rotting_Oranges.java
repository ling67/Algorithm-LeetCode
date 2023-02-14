class Solution {
    
    public int orangesRotting(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int sumNum = 0;
        int layer = -1; //record the minimum number of minutes
        
        Queue<Pair> queue = new LinkedList<>();
        Set<Pair> set = new HashSet<>();
        
        //统计橙子数量
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++ ) {
                if (grid[i][j] == 2) {
                    Pair<Integer, Integer> p = new Pair(i, j);
                    queue.offer(p);    //讲起始的坏橘子放进队列
                    set.add(p);
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
        int[] X = {0, 1, -1, 0};
        int[] Y = {1, 0, 0, -1};
        
        while (!queue.isEmpty()) {
            layer++;
            if(set.size() == sumNum) {
                return layer;
            }
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                Pair<Integer, Integer> cur = queue.poll();
                for (int j = 0; j < 4; j++) {
                    int x = cur.getKey() + X[j];
                    int y = cur.getValue() + Y[j];
                     Pair<Integer, Integer> adj = new Pair(x, y);
                    if (x < 0 || x >= m || y < 0 || y >= n) {
                        continue;
                    }
                    if (grid[x][y] == 1 && !set.contains(adj)) {
                        grid[x][y] = 2;
                        queue.offer(adj);
                        set.add(adj);
                    }
                }
            }
        }
        return -1;
    }
}
