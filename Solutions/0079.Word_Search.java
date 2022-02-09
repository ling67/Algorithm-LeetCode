/*
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?


*/

//version: pair
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


// int[][]
class Solution {
    public boolean exist(char[][] board, String word) {
        int m = board.length;
        int n = board[0].length;
        boolean[][] visited = new boolean[m][n];
        
        if(word.length() > m * n) return false;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == word.charAt(0) 
                    && visited[i][j] == false) {
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
                        boolean[][] visited) {
        
        int m = board.length;
        int n = board[0].length;
        
        //exit
        if (word.length() == index) {
            return true;
        }
        
        if (i < 0 || j < 0 || i >= m || j >= n 
            || visited[i][j] == true
            || (word.charAt(index) != board[i][j])) {
            return false;
        }
        
        //split
        visited[i][j] = true;
        boolean res = dfs(board, word, index + 1, i + 1, j, visited) ||
                    dfs(board, word, index + 1, i - 1, j, visited) ||
                    dfs(board, word, index + 1, i, j + 1, visited) ||
                    dfs(board, word, index + 1, i, j - 1, visited);
        visited[i][j] = false;
        return res;
    }
    
}



