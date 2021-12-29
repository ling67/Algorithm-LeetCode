/*
描述
给定骑士在棋盘上的 初始 位置(一个2进制矩阵 0 表示空 1 表示有障碍物)，找到到达 终点 的最短路线，返回路线的长度。如果骑士不能到达则返回 -1 。

起点跟终点必定为空.
骑士不能碰到障碍物.
路径长度指骑士走的步数.
如果骑士的位置为 (x,y)，他下一步可以到达以下这些位置:

(x + 1, y + 2)
(x + 1, y - 2)
(x - 1, y + 2)
(x - 1, y - 2)
(x + 2, y + 1)
(x + 2, y - 1)
(x - 2, y + 1)
(x - 2, y - 1)
样例
例1:

输入:
[[0,0,0],
 [0,0,0],
 [0,0,0]]
source = [2, 0] destination = [2, 2] 
输出: 2
解释:
[2,0]->[0,1]->[2,2]
例2:

输入:
[[0,1,0],
 [0,0,1],
 [0,0,0]]
source = [2, 0] destination = [2, 2] 
输出:-1
*/

//version 1:memory limit exceeded

/**
 * Definition for a point.
 * class Point {
 *     int x;
 *     int y;
 *     Point() { x = 0; y = 0; }
 *     Point(int a, int b) { x = a; y = b; }
 * }
 */

public class Solution {
    /**
     * @param grid: a chessboard included 0 (false) and 1 (true)
     * @param source: a point
     * @param destination: a point
     * @return: the shortest path 
     */
    int deltaX[] = {1, 1, -1, -1, 2, 2, -2, -2};
    int deltaY[] = {2, -2, 2, -2, 1, -1, 1, -1};

    public int shortestPath(boolean[][] grid, Point source, Point destination) {
        // write your code here
        if (grid == null || grid.length == 0 || grid[0].length == 0) {
            return 0;
        }

        int m = grid.length;
        int n = grid[0].length;

        Queue<Point> queue = new LinkedList<Point >();
        HashSet<Point> visited = new HashSet<Point>();
        queue.offer(source);
        visited.add(source);

        int step = 0;
        while(!queue.isEmpty()) {
            int size = queue.size();
            step++;
            for (int i = 0; i < size; i++) {
                Point curr = queue.poll();
                for (int j = 0; j < 8; j++) {
                    Point neighbor = new Point(curr.x + deltaX[j], curr.y + deltaY[j]);
                    if (!isInBound(neighbor, m, n)) {
                        continue;
                    }
                    if (neighbor.x == destination.x && neighbor.y == destination.y) {
                        return step;
                    }
                    if ((!visited.contains(neighbor)) && (!grid[neighbor.x][neighbor.y])) {
                        queue.offer(neighbor);
                        visited.add(neighbor);
                    } 
                }
            }
        }
        return -1;
    }

    private boolean isInBound(Point point, int m, int n) {

        if (point.x < 0 || point.x >= m) {
            return false;
        }
        if (point.y < 0 || point.y >= n) {
            return false;
        }
        return true;
    }
}

//version 2 :用distance去存储距离

/**
 * Definition for a point.
 * class Point {
 *     int x;
 *     int y;
 *     Point() { x = 0; y = 0; }
 *     Point(int a, int b) { x = a; y = b; }
 * }
 */

public class Solution {
    /**
     * @param grid: a chessboard included 0 (false) and 1 (true)
     * @param source: a point
     * @param destination: a point
     * @return: the shortest path 
     */
    int dx[] = {1, 1, -1, -1, 2, 2, -2, -2};
    int dy[] = {2, -2, 2, -2, 1, -1, 1, -1};

    public int shortestPath(boolean[][] grid, Point source, Point destination) {
        // write your code here
        if (grid == null || grid.length == 0 || grid[0].length == 0) {
            return 0;
        }

        Queue<Point> queue = new LinkedList<Point >();
        Map<Integer, Integer> distance = new HashMap();

        int n = grid.length, m = grid[0].length;
        queue.offer(source);
        distance.put(source.x * m + source.y, 0);

        while(!queue.isEmpty()) {
            Point point = queue.poll();
            if(point.x == destination.x && point.y == destination.y) {
                return distance.get(point.x * m + point.y);
            }

            for (int i = 0; i < 8; i++) {
                int adjX = point.x + dx[i];
                int adjY = point.y + dy[i];
                if (!isValid(adjX, adjY, grid)) {
                    continue;
                }
                if (distance.containsKey(adjX * m + adjY)) {
                    continue;
                }

                distance.put(adjX * m + adjY, distance.get(point.x * m + point.y) + 1);
                queue.offer(new Point(adjX, adjY));
            }
        }
        return -1;
    }

    private boolean isValid(int x, int y, boolean[][] grid) {

        if (x < 0 || x >= grid.length || y < 0 || y >= grid[0].length) {
            return false;
        }
        return !grid[x][y];
    }
}





