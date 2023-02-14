class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        if (image[sr][sc] == color) return image;
        dfs(image, sr, sc, image[sr][sc], color);
        return image;
    }

    private void dfs(int[][] image, int row, int col, int target, int color) {
        if (row < image.length && row >= 0 && col < image[0].length && col >= 0 && image[row][col] == target) {
            image[row][col] = color;
            dfs(image, row - 1, col, target, color);
            dfs(image, row, col - 1, target, color);
            dfs(image, row + 1, col, target, color);
            dfs(image, row, col + 1, target, color);
        }
    }
}
