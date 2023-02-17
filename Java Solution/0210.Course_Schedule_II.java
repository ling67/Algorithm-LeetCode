class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        int[] res = new int[numCourses];

        Map<Integer, List<Integer>> map = new HashMap<>();
        for (int i = 0; i < numCourses; i++) {
            map.put(i, new LinkedList<Integer>());
        }

        int[] inDegree = new int[numCourses];

        for (int[] edge : prerequisites) {
            map.get(edge[1]).add(edge[0]);
            inDegree[edge[0]]++;
        }

        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (inDegree[i] == 0) queue.add(i);
        }

        int index = 0;
        while (!queue.isEmpty()){
            int cur = queue.poll();
            res[index++] = cur;
            for (int adj : map.get(cur)) {
                inDegree[adj]--;
                if (inDegree[adj] == 0) {
                    queue.add(adj);
                }
            }
        }
        return index == numCourses ? res : new int[0];
    }
}
