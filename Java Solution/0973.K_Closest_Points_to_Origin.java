//Solution1: brute force
class Solution {
    public int[][] kClosest(int[][] points, int k) {
        int N = points.length;
        int[] dists = new int[N];
        for (int i = 0; i < N; i++) {
            dists[i] = dist(points[i]);
        }
        Arrays.sort(dists);
        int distK = dists[k - 1];

        int [][] res = new int[k][2];
        int index = 0;
        for (int i = 0; i < N; i++) {
            if (dist(points[i]) <= distK) {
                res[index][0] = points[i][0];
                res[index][1] = points[i][1];
                index++;
            }
        }
        return res;
    }

    public int dist(int[] point) {
        return point[0] * point[0] + point[1] * point[1];
    }
}

//Solution2: priorityQueue

class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((p1, p2) -> dist(p1) - (dist(p2)));

        for (int i = 0; i < points.length; i++) {
            pq.add(points[i]);
        }

        int [][] result = new int[k][2];

        for (int i = 0; i < k; i++) {
            result[i] = pq.poll();
        }
        return result;
    }

    public int dist(int[] point) {
        return point[0] * point[0] + point[1] * point[1];
    }
}
