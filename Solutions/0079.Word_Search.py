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

"""
图上的搜索：dfs + backtracking
这题5min内写出来了才算真正会了图上的dfs + backtracking
Time Complexity: O(N*3^L) where N is the number of cells in the board and L is the length of the word to be matched.
"""
"""
套用backtrack的模板，backtrack 里面要传入(curr_i, curr_j, curr_idx on word). find solution: if board[next_i][next_j] == word[curr_idx + 1].  
if find a solution, backtrack函数输出True
if valid: if board[next_i][next_j] == word[curr_idx + 1]. 需要一个visited set来标记已经走过的路径避免走重复的路径。
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(curr_i, curr_j, curr_idx):
            if curr_idx == len(word) - 1:
                return True
            for delta_i, delta_j in [(1,0),(-1,0),(0,1),(0,-1)]:
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n:
                    if (next_i, next_j) not in visited:
                        if board[next_i][next_j] == word[curr_idx+1]:
                            visited.add((next_i, next_j))
                            if backtrack(next_i, next_j, curr_idx+1):
                                return True
                            visited.remove((next_i, next_j))
            return False
        
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited = set()
                    visited.add((i, j))
                    if backtrack(i, j, 0):
                        return True
        return False
                

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



