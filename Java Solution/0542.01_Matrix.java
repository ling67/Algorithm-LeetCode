class Solution {
    public int[][] updateMatrix(int[][] mat) {
        int m = mat.length;
        int n = mat[0].length;

        Queue<Pair<Integer, Integer>> queue = new LinkedList<>();
        Set<Pair<Integer, Integer>> set = new HashSet<>();

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 0) {
                    Pair<Integer, Integer> p = new Pair<>(i, j);
                    queue.add(p);
                    set.add(p);
                }
            }
        }

        int[] X = {0, 0, 1, -1};
        int[] Y = {1, -1, 0, 0};

        int layer = 0;
        while(!queue.isEmpty()) {
            layer++;
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                Pair<Integer, Integer> cur = queue.remove();
                for (int j = 0; j < 4; j++) {
                    int x = cur.getKey() + X[j];
                    int y = cur.getValue() + Y[j];
                    Pair<Integer, Integer> adj = new Pair<>(x, y);
                    if (x < 0 || x >= m || y < 0 || y >= n) continue;
                    if (mat[x][y] == 1 && !set.contains(adj)) {
                        mat[x][y] = layer;
                        queue.add(adj);
                        set.add(adj);
                    }
                }
            }
        }
        return mat;
    }
}
