class Solution {
    public int numIslands(char[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int count = 0;

        //we also can set the value to 0 after we visit, then we don't need the hashset
        Set<Pair<Integer, Integer>> visited = new HashSet<>();

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (visited.contains(new Pair<Integer, Integer>(i, j))) continue;
                if (grid[i][j] == '1') {
                    dfs(i, j, grid, visited);
                    count++;
                }
            }
        }
        return count;
    }

    public void dfs(int x, int y, char[][] grid, Set<Pair<Integer, Integer>> visited) {
        int m = grid.length;
        int n = grid[0].length;

        int[] directionX = {0, 1, 0, -1};
        int[] directionY = {-1, 0, 1, 0};

        visited.add(new Pair<Integer, Integer>(x, y));
        for (int i = 0; i < 4; i++) {
            int neiX = x + directionX[i];
            int neiY = y + directionY[i];
            if (neiX < 0 || neiX >= m || neiY < 0 || neiY >= n) continue;
            Pair<Integer, Integer> pair = new Pair(neiX, neiY);
            if (!visited.contains(pair) && grid[neiX][neiY] == '1'){
                dfs(neiX, neiY, grid, visited);
            }
        }
    }
}
