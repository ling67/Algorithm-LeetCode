class Solution {
    public boolean exist(char[][] board, String word) {
        int m = board.length;
        int n = board[0].length;
        Set<Pair<Integer, Integer>> visited = new HashSet<>();
        
        if(word.length() > m * n) return false;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == word.charAt(0) 
                    && !visited.contains(new Pair<Integer, Integer>(i, j))) {
                    if (dfs(board, word, 0, i, j, visited)) {
                        return true;
                    }
                }
            }
        }
        return false;
        
    }
    
    //返回以
    private boolean dfs(char[][] board, 
                        String word, 
                        int index, 
                        int i, 
                        int j, 
                        Set<Pair<Integer, Integer>> visited) {
        
        int m = board.length;
        int n = board[0].length;
        
        //exit
        if (word.length() == index) {
            return true;
        }
        
        if (i < 0 || j < 0 || i >= m || j >= n 
            || visited.contains(new Pair<Integer, Integer>(i,j)) == true 
            || (word.charAt(index) != board[i][j])) {
            return false;
        }
        
        //split
        Pair<Integer, Integer> pair = new Pair<>(i,j);
        visited.add(pair);
        boolean res = dfs(board, word, index + 1, i + 1, j, visited) ||
                    dfs(board, word, index + 1, i - 1, j, visited) ||
                    dfs(board, word, index + 1, i, j + 1, visited) ||
                    dfs(board, word, index + 1, i, j - 1, visited);
        visited.remove(pair);
        return res;
    }
}
