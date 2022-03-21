/*
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]

*/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [i for i in range(numCourses)]
        
        #1.construct a dictionary of adjancency list for the graph
        graph = collections.defaultdict(list)
        for u, v in prerequisites:
            graph[v].append(u)
        
        #2.construct all indegree 
        in_degree = collections.defaultdict(int)
        for n in range(numCourses):
            in_degree[n] = 0
        for u, v in prerequisites:
            in_degree[u] += 1
        
        #3.bfs visite
        q = collections.deque()
        res = []
        for u, v in in_degree.items():
            if v == 0:
                q.append(u)
        
        while q:
            curr = q.popleft()
            res.append(curr)
            for node in graph[curr]:
                in_degree[node] -= 1
                if in_degree[node] == 0:
                    q.append(node)
                    
        if len(res) == numCourses:
            return res
        else:
            return []
            
        


class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        int[][] matrix = new int[numCourses][numCourses];
        int[] inDegree = new int[numCourses];
        List<Integer> list = new ArrayList<>();
        
        for (int i = 0; i< prerequisites.length; i++) {
            int ready = prerequisites[i][0];
            int pre = prerequisites[i][1];
            if (matrix[pre][ready] == 0) {   //去重
                inDegree[ready]++;  //得到入度
            }
            matrix[pre][ready] = 1;
        }
        
        int count = 0;
        Queue<Integer> queue = new LinkedList();
        for (int i = 0; i < inDegree.length; i++) {
            if (inDegree[i] == 0) 
            {
                queue.offer(i);     //queue里面放的横坐标  
                list.add(i);
            }
        }
        
        while (!queue.isEmpty()) {
            int course = queue.poll();
            count++;
            for (int i = 0; i < numCourses; i++) {
                if (matrix[course][i] != 0) {    //!=0说明有路径过来
                    if (--inDegree[i] == 0) {
                        queue.offer(i);
                        list.add(i);
                    }
                }
            }
        }
        if (list.size() == numCourses) {
            int[] result = new int[numCourses];
            for (int i = 0; i < numCourses; i++) {
                result[i] = list.get(i);
            }
            return result;
        }
        
        return new int[]{};
    }
}
