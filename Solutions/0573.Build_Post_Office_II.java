/*
573 · 邮局的建立 II
给出一个二维的网格，每一格可以代表墙 2 ，房子 1，以及空 0 (用数字0,1,2来表示)，在网格中找到一个位置去建立邮局，使得所有的房子到邮局的距离和是最小的。
返回所有房子到邮局的最小距离和，如果没有地方建立邮局，则返回-1.

你不能穿过房子和墙，只能穿过空地。
你只能在空地建立邮局。
样例
样例 1:

输入：[[0,1,0,0,0],[1,0,0,2,1],[0,1,0,0,0]]
输出：8
解释： 在(1,1)处建立邮局，所有房子到邮局的距离和是最小的。
样例 2:

输入：[[0,1,0],[1,0,1],[0,1,0]]
输出：4
解释：在(1,1)处建立邮局，所有房子到邮局的距离和是最小的。
*/


class Point {
    int x, y;
    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class Solution {
    /**
     * @param grid: a 2D grid
     * @return: An integer
     */
    public int shortestDistance(int[][] grid) {
        if(grid == null || grid.length == 0 || grid[0].length == 0) {
            return -1;
        }
        // write your code here
        int m = grid.length;
        int n = grid[0].length;

        int shortestDis = -1;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0) {
                    //对于每个为0的点做BFS，返回距离源点的距离和
                    int distance = getDistByBFS(grid, i, j);
                    if (distance == -1) {
                        continue;
                    }
                    if(shortestDis < 0 || shortestDis > distance) {
                        shortestDis = distance;
                    }
                }
            }
        }
        return shortestDis;
    }

    private int getDistByBFS(int[][] grid, int x, int y) {
        int m = grid.length;
        int n = grid[0].length;

        //方向：右-下-左-上
        int[] directionX = {0, 1, -1, 0};
        int[] directionY = {1, 0, 0, -1};

        int[][] distance = new int[m][n];
        
        //起始点放入队列内
        Queue<Point> queue = new LinkedList<Point>();
        queue.offer(new Point(x, y));
        boolean[][] visited = new boolean[m][n];  //visit用于存储访问过的所有房子, 选择使用2D数组而不是hashset，这样可以避免hashset.contains(new Point)时判断出错
        visited[x][y] = true;
        distance[x][y] = 0;

        //while 循环
        while (!queue.isEmpty()) {
            //模板第一步：弹出源节点
            Point cur = queue.poll();
            // 第二步：放入源节点的neighbors到queue中
            for (int i = 0; i < 4; i++) {
                Point adj = new Point(cur.x + directionX[i], cur.y + directionY[i]);
                //判断是否越界
                if(isOutOfBound(adj, m, n)){
                    continue;
                }
                if (visited[adj.x][adj.y]) {
                    continue;
                }
                if (grid[adj.x][adj.y] == 0) {
                    distance[adj.x][adj.y] = distance[cur.x][cur.y] + 1; 
                    queue.offer(adj);
                    visited[adj.x][adj.y] = true;
                }
                if (grid[adj.x][adj.y] == 1) {
                    distance[adj.x][adj.y] = distance[cur.x][cur.y] + 1;
                    visited[adj.x][adj.y] = true;   // 注意这里也要标记成visited
                }
            }
        }

        //如果有房子没有在visted里面，说明不能建房子
        if(!isVisited(grid, visited)) {
            return -1;
        } 
        
        //求距离之和 distance
        return getSum(distance, grid);
    }

    //判断有没有越界，越界返回true
    private boolean isOutOfBound(Point point, int m, int n) {
        if (point.x < 0 || point.x >= m) {
            return true;
        }
        if (point.y < 0 || point.y >= n) {
            return true;
        }
        return false;
    }

    //判断是不是所有房子已经被访问过，访问过返回true
    private boolean isVisited(int[][] grid, boolean[][] visited){
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if ((grid[i][j] == 1) && (!visited[i][j])) {
                    return false;
                }
            }
        }
        return true;
    }

    //获取二维数组之和
    private int getSum(int[][] distance, int[][] grid){
        int sum = 0;
        for (int i = 0; i < distance.length; i++) {
            for (int j = 0; j < distance[0].length; j++) {
                if (grid[i][j] == 1) {      //注意这里一定要判断只有是房子才 sum += dist操作
                    sum += distance[i][j];
                }
            }
        }
        return sum;
    }
}
