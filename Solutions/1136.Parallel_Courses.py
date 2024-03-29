/*
You are given an integer n, which indicates that there are n courses labeled from 1 to n. You are also given an array relations where relations[i] = [prevCoursei, nextCoursei], representing a prerequisite relationship between course prevCoursei and course nextCoursei: course prevCoursei has to be taken before course nextCoursei.

In one semester, you can take any number of courses as long as you have taken all the prerequisites in the previous semester for the courses you are taking.

Return the minimum number of semesters needed to take all courses. If there is no way to take all the courses, return -1.

 

Example 1:


Input: n = 3, relations = [[1,3],[2,3]]
Output: 2
Explanation: The figure above represents the given graph.
In the first semester, you can take courses 1 and 2.
In the second semester, you can take course 3.
Example 2:


Input: n = 3, relations = [[1,2],[2,3],[3,1]]
Output: -1
Explanation: No course can be studied because they are prerequisites of each other.
 

Constraints:

1 <= n <= 5000
1 <= relations.length <= 5000
relations[i].length == 2
1 <= prevCoursei, nextCoursei <= n
prevCoursei != nextCoursei
All the pairs [prevCoursei, nextCoursei] are unique.
*/

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        #step1: build the graph
        graph = defaultdict(list)
        for u, v in relations:
            graph[u].append(v)
        
        #step2: get in_degree for each node
        in_degrees = defaultdict(int)
        for node in range(1, n+1):
            in_degrees[node] = 0
        for u, v in relations:
            in_degrees[v] += 1
            
        #step3: put all in_degree == 0 node into q
        q = deque()
        for node, in_degree in in_degrees.items():
            if in_degree == 0:
                q.append(node)
        
        #step4: peel the onion
        steps = 0
        visited = set()
        
        while q:
            steps += 1
            lens = len(q)
            for _ in range(lens):
                curr = q.popleft()
                visited.add(curr)
                for next_node in graph[curr]:
                    in_degrees[next_node] -= 1
                    if in_degrees[next_node] == 0:
                        q.append(next_node)
        if len(visited) == n:
            return steps
        else:
            return -1
        

class Solution {
    public int minimumSemesters(int n, int[][] relations) {
        int[][] matrix = new int[n+1][n+1];
        int[] inDegree = new int[n+1];
        
        for (int i = 0; i < relations.length; i++) {
            int pre = relations[i][0];
            int ready = relations[i][1];
            inDegree[ready]++;
            matrix[pre][ready] = 1;
        }
        
        int count = 0;
        int layer = 0;    
        Queue<Integer> queue = new LinkedList();
        for (int i = 1; i < inDegree.length; i++) {
            if (inDegree[i] == 0) {
                queue.offer(i);     //queue里面放的横坐标  
            }
        }
        while (!queue.isEmpty()) {
            layer++;
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int course = queue.poll();
                count++;
                for (int j = 1; j < n + 1; j++) {
                    if (matrix[course][j] != 0) {    //!=0说明有路径过来
                        if (--inDegree[j] == 0) {
                            queue.offer(j);
                        }
                    }
                }
            }
        }
        if (count == n) {
            return layer;
        }
        return -1;
    }
}
