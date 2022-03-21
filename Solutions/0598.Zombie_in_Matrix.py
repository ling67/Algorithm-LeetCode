/*
描述
给一个二维网格，每一个格子都有一个值，2 代表墙，1 代表僵尸，0 代表人类(数字 0, 1, 2)。僵尸每天可以将上下左右最接近的人类感染成僵尸，但不能穿墙。将所有人类感染为僵尸需要多久，如果不能感染所有人则返回 -1。

样例
例1:

输入:
[[0,1,2,0,0],
 [1,0,0,2,1],
 [0,1,0,0,0]]
输出:
2
例2:

输入:
[[0,0,0],
 [0,0,0],
 [0,0,1]]
输出:
4
*/


//python version bfs O(mn)
from typing import (
    List,
)

class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """
    def zombie(self, grid: List[List[int]]) -> int:
        # write your code here
        m, n = len(grid), len(grid[0])
        q = collections.deque()
        visited = set()
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i,j))
                if grid[i][j] == 0:
                    cnt += 1
        layer = -1
        while q:
            layer += 1
            size = len(q)
            for _ in range(size):
                curr_i, curr_j = q.popleft()
                for delta_i, delta_j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nei_i = curr_i + delta_i
                    nei_j = curr_j + delta_j
                    if 0 <= nei_i < m and 0 <= nei_j < n and grid[nei_i][nei_j] == 0 and (nei_i, nei_j) not in visited:
                        q.append((nei_i,nei_j))
                        visited.add((nei_i, nei_j))
        if len(visited) == cnt:
            return layer
        else:
            return -1

//java version bfs O(mn)

class Coordinate {
    int x, y;
    public Coordinate(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class Solution {
    /**
     * @param grid: a 2D integer grid
     * @return: an integer
     */

    public int PEOPLE = 0;
    public int ZOMBIE = 1;
    public int WALL = 2;

    public int[] deltaX = {1, 0, 0, -1};
    public int[] deltaY = {0, 1, -1, 0}; 

    public int zombie(int[][] grid) {
        // write your code here

        //判空
        if (grid == null || grid.length == 0 || grid[0].length == 0) {
            return 0;
        }

        int n = grid.length;
        int m = grid[0].length;

        //initialize the queue & count people
        int people = 0;
        Queue<Coordinate> queue = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == PEOPLE) {
                    people++;
                }   
                if (grid[i][j] == ZOMBIE) {
                    queue.offer(new Coordinate(i, j));
                }
            }
        }

        //bfs 遍历每个僵尸，吃掉周围的人
        int days = 0;
        while (!queue.isEmpty()) {
            days++;
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                Coordinate zb = queue.poll();
                for (int direction = 0; direction < 4; direction++) {
                    Coordinate adj = new Coordinate(zb.x + deltaX[direction], zb.y + deltaY[direction]);
                    if (!isPeople(adj, grid)) {
                        continue;
                    }
                    grid[adj.x][adj.y] = ZOMBIE;
                    people--;
                    if (people == 0) {
                        return days;
                    }
                    queue.offer(adj);
                }
            }
        }
        return -1;
    }

    //判断是不是人
    private boolean isPeople(Coordinate coor, int[][] grid) {

        int n = grid.length;
        int m = grid[0].length;

        if (coor.x < 0 || coor.x >= n) {
            return false;
        }
        if (coor.y < 0 || coor.y >= m) {
            return false;
        }
        return (grid[coor.x][coor.y] == PEOPLE);
    }

}
