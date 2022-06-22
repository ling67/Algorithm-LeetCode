"""
Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.

Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).

 

Example 1:


Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
Output: 2
Example 2:

Input: board = [["."]]
Output: 0
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is either '.' or 'X'.
"""

class UnionFind:
    def __init__(self):
        self.father = collections.defaultdict(int)
        self.cnt = 0
    
    def add(self, x):    #when we need add function? when we donot know the exactly number we can use add function
        if x not in self.father:
            self.father[x] = x
            self.cnt += 1
    
    def find(self, x):
        if self.father[x] == x:
            return x
        else:
            self.father[x] = self.find(self.father[x])
            return self.father[x]
    
    def connect(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.cnt -= 1

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        uf = UnionFind()
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    uf.add((i, j))
                    for delta_i, delta_j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        next_i, next_j = i + delta_i, j + delta_j
                        if 0 <= next_i < m and 0 <= next_j < n and board[next_i][next_j] == 'X':
                            uf.add((next_i, next_j))
                            uf.connect((i, j), (next_i, next_j))
        return uf.cnt
