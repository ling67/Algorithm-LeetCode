/*
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
*/


#方法是先把所有0放入q的第一层，然后一层层遍历，同时更新遇到的1为当前的层数，层数就是1离0的距离 - O(MN)

class Solution:
    ADJACENT = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return matrix
        
        m, n = len(matrix), len(matrix[0])
        
        q = collections.deque()
        visited = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))
                  
        level = 0
        while q:
            level += 1
            lens = len(q)
            
            for _ in range(len(q)):
                curr_x, curr_y = q.popleft()
                
                for delta_x, delta_y in self.ADJACENT:
                    next_x, next_y = curr_x + delta_x, curr_y + delta_y
                    
                    if 0 <= next_x < m and 0 <= next_y < n and (next_x, next_y) not in visited:
                        matrix[next_x][next_y] = level
                        q.append((next_x, next_y))
                        visited.add((next_x, next_y))
                        
        return matrix

//version1 暴力法：时间复杂度高，case过不了
class Solution {
    public int[][] updateMatrix(int[][] mat) {
        int m = mat.length;
        int n = mat[0].length;
        for (int i = 0; i < m; i++ ) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 1) {
                    getNearest(mat, i, j);
                }
            }
        }
        return mat;
    }
    
    private void getNearest(int[][] mat, int row, int column) {
        Queue<Pair> queue = new LinkedList<>();
        Set<Pair> set = new HashSet<>();
        Pair<Integer, Integer> head = new Pair(row, column);
        queue.offer(head);
        set.add(head);
        int layer = 0;
        
        int[] directionX = {-1, 0, 1, 0};
        int[] directionY = {0, 1, 0, -1};
            
        while (!queue.isEmpty()) {
            layer++;
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                Pair<Integer, Integer> p = queue.poll();
                for (int j = 0; j < 4; j++) {
                    int adjRow = p.getKey() + directionX[j];
                    int adjColumn = p.getValue() + directionY[j];
                    Pair<Integer, Integer> adj = new Pair(adjRow, adjColumn);
                    if (!inBound(mat, adjRow, adjColumn)) {
                        continue;
                    }
                    if (mat[adjRow][adjColumn] == 0 && !set.contains(adj)) {
                        mat[row][column] = layer;
                        return;
                    } 
                    queue.offer(adj);
                    set.add(adj);
                }
            }
        }
    }
    
    //在bound中返回true
    private boolean inBound(int[][] mat, int row, int column) {
        int m = mat.length;
        int n = mat[0].length;
        return row >= 0 && row < m && column >= 0 && column < n;
    }
}


//version2 从0 找1.更新所有节点
class Solution {
    public int[][] updateMatrix(int[][] mat) {
        Queue<Pair> queue = new LinkedList<>();
        Set<Pair> set = new HashSet<>();
        int layer = 0;

        int m = mat.length;
        int n = mat[0].length;
        for (int i = 0; i < m; i++ ) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 0) {
                    Pair<Integer, Integer> p = new Pair(i, j);
                    queue.offer(p);
                    set.add(p);
                }
            }
        }

        int[] directionX = {-1, 0, 1, 0};
        int[] directionY = {0, 1, 0, -1};
        
        while (!queue.isEmpty()) {
            layer++;
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                Pair<Integer, Integer> head = queue.poll();
                for (int j = 0; j < 4; j++) {
                    int row = head.getKey() + directionX[j];
                    int column = head.getValue() + directionY[j];
                    Pair<Integer, Integer> adj = new Pair(row, column);
                    if (!inBound(mat, row, column)) {
                        continue;
                    }
                    if (mat[row][column] == 1 && !set.contains(adj)) {
                        mat[row][column] = layer;
                        queue.offer(adj);
                        set.add(adj);
                    } 
                }
            }
        }
        return mat;
    }
    
    //在bound中返回true
    private boolean inBound(int[][] mat, int row, int column) {
        int m = mat.length;
        int n = mat[0].length;
        return row >= 0 && row < m && column >= 0 && column < n;
    }
}
