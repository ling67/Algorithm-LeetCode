/*

We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.

Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.

 

Example 1:

Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4] and group2 [2,3].
Example 2:

Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false
*/

//DFS python
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def dfs(curr_node, curr_color):
            visited[curr_node] = curr_color
            for next_node in dis_graph[curr_node]:
                if next_node in visited:
                    if visited[next_node] == curr_color:
                        return False
                else:
                    if not dfs(next_node, not curr_color):
                        return False
            return True
        
        dis_graph = defaultdict(list)
        for u, v in dislikes:
            dis_graph[u].append(v)
            dis_graph[v].append(u)
        
        visited = defaultdict(bool)
        for node in range(1, n+1):
            if node not in visited:
                if not dfs(node, True):
                    return False
        return True
                

/*
group[i] = 0 means node i hasn't been visited.
group[i] = 1 means node i has been grouped to 1.
group[i] = -1 means node i has been grouped to -1.
first we need to get a graph base on dislikes[][]
*/
class Solution {
    public boolean possibleBipartition(int n, int[][] dislikes) {
        //transfer a array to a graph，1 represent dislike
        int [][] graph = new int[n][n];
        for (int[] d : dislikes) {
            graph[d[0] - 1][d[1] - 1] = 1;
            graph[d[1] - 1][d[0] - 1] = 1;
        }
        
        int[] group = new int[n];
        
        //为了遍历到所有的点，有可能图不连通
        for (int i = 0; i < n; i++) {
            if (group[i] == 0) {
                if (!dfs(graph, group, i, 1)) return false;
            }
        }
        return true;
    }
    
    //验证index开始的连通的图满不满足条件    
    public boolean dfs(int[][] graph, int[] group, int index, int g){
       group[index] = g;
        for (int i = 0; i < graph.length; i++) {
            if (graph[index][i] == 1) {
                if (group[i] == g) {
                    return false;
                }
                if (group[i] == 0 && !dfs(graph, group, i, -g)) {
                    return false;
                }
            }
        }
        return true;
    }
    
}
