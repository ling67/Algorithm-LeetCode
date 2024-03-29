/*
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 105
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
*/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            True 
        
        # 1. construct a dictoinary of adjacency list for the graph
        graph = collections.defaultdict(list)
        for u, v in prerequisites: 
            graph[v].append(u)
        
        # 2. get in_degree information for all nodes
        in_degree = collections.defaultdict(int)
        for n in range(numCourses):
            in_degree[n] = 0
        for u, v in prerequisites: 
            in_degree[u] += 1
            
        # 3. topological sort - bfs
        # step I: initialze q by putting all in_degree = 0 into q        q = collections.deque()
        q = collections.deque()
        for node, i in in_degree.items():
            if i == 0:
                q.append(node)
                
        # step II: keep adding in_degree = 0 node into q and pop out while updating res
        res = []
        while q:
            curr = q.popleft()
            res.append(curr)
            for next_node in graph[curr]:
                in_degree[next_node] -= 1
                if in_degree[next_node] == 0:
                    q.append(next_node)
                    
        return len(res) == numCourses
            
    
        

class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[][] matrix = new int[numCourses][numCourses];
        int[] inDegree = new int[numCourses];
        
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
            if (inDegree[i] == 0) queue.offer(i);     //queue里面放的横坐标
        }
        while (!queue.isEmpty()) {
            int course = queue.poll();
            count++;
            for (int i = 0; i < numCourses; i++) {
                if (matrix[course][i] != 0) {    //!=0说明有路径过来
                    if (--inDegree[i] == 0) {
                        queue.offer(i);
                    }
                }
            }
        }
        return count == numCourses;
    }
}
