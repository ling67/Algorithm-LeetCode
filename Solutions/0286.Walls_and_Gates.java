/*
You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

 

Example 1:


Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
Example 2:

Input: rooms = [[-1]]
Output: [[-1]]
 

Constraints:

m == rooms.length
n == rooms[i].length
1 <= m, n <= 250
rooms[i][j] is -1, 0, or 231 - 1.

*/

/*
1.暴力搜索，对每一个empty room都做BFS
2.从gate开始，BFS收索empty room 记录最短路径，只需要一次BFS
*/
class Solution {
    public void wallsAndGates(int[][] rooms) {
       
        int m = rooms.length;
        int n = rooms[0].length;
        
        Queue<Pair<Integer, Integer>> queue = new LinkedList<>();
        Set<Pair> set = new HashSet<>();
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (rooms[i][j] == 0) {
                    Pair pair = new Pair(i, j);
                    queue.offer(pair);
                    set.add(pair);
                }
            }
        }
        
        int[] directionX = {-1, 0, 1, 0};
        int[] directionY = {0, 1, 0, -1};
        int distance = 0;
        
        while (!queue.isEmpty()) {
            distance++;
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                Pair<Integer, Integer> dir = queue.poll();
                for (int j = 0; j < 4; j++) {
                    int row = dir.getKey() + directionX[j];
                    int column = dir.getValue() + directionY[j];
                    Pair adj = new Pair(row, column);
                    if (!inBound(rooms, row, column)) {
                        continue;
                    }
                    if (rooms[row][column] == 2147483647 && !set.contains(adj)) {
                        queue.offer(adj);
                        rooms[row][column] = distance;
                    }
                }
            }
        }  
    }
    
    //判断数组下标是否越界，没有越界返回true
    private boolean inBound(int[][] rooms, int row, int column) {
        int m = rooms.length;
        int n = rooms[0].length;
        return row >=0 && row < m && column >=0 && column < n;
    }
    
}
