"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""

"""
三个字典：行，列，九宫格 (行，列):set 
只验证已经出现过的数，空格不用判断
refer: https://www.youtube.com/watch?v=oeMw30HapdQ&t=61s
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(lambda:set())
        rows = defaultdict(lambda:set())
        grids = defaultdict(lambda:set())
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in cols[j]:
                    return False
                cols[j].add(board[i][j])
                if board[i][j] in rows[i]:
                    return False 
                rows[i].add(board[i][j])
                if board[i][j] in grids[10*(i//3)+j//3]:   #记住怎么给9宫格编号，i//3放到十位，j//3放到个位
                    return False
                grids[10*(i//3)+j//3].add(board[i][j])
        return True

