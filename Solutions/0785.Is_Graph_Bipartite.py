/*
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.

*/

//DFS python 
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(curr_node, curr_color):
            visited[curr_node] = curr_color
            
            for next_node in graph[curr_node]:
                if next_node in visited:
                    if visited[next_node] == curr_color:
                        return False
                else: 
                    if not dfs(next_node, not curr_color):
                        return False
            return True
        
        # have to do dfs for every node cuz it could be a non-biparitite even if 
        # there are lots of dis-connected components in the graph
        visited = defaultdict(bool)# True表示red color, False表示blue color
        for node in range(len(graph)):   # for loop保证可以访问到所有的nodes
            if node not in visited:      # 注意这里要check in visited
                if not dfs(node, True):
                    return False
        return True


/*
Our goal is trying to use two colors to color the graph and see if there are any adjacent nodes having the same color.
Initialize a color[] array for each node. Here are three states for colors[] array:
0: Haven't been colored yet.
1: Blue.
-1: Red.
For each node,

If it hasn't been colored, use a color to color it. Then use the other color to color all its adjacent nodes (DFS).
If it has been colored, check if the current color is the same as the color that is going to be used to color it. (Please forgive my english... Hope you can understand it.)
*/ 
//version : DFS
class Solution {
    public boolean isBipartite(int[][] graph) {  
        int n = graph.length;
        int[] colors = new int[n];
        
        //为了遍历到所有的点，有可能图不连通
        for (int i = 0; i < n; i++) {
            if (colors[i] == 0) {
                if (!validColor(graph, colors, 1, i)) return false;
            }
        }
        return true;
    }
    
    //验证node开始的连通的图满不满足条件    
    public boolean validColor(int[][] graph, int[] colors, int color, int node){
        //If it has been colored, check if the current color is the same as the color that is going to be used to color it.
        if (colors[node] != 0) {
            return colors[node] == color;
        } 
        
        //If it hasn't been colored, use a color to color it.
        colors[node] = color;
        for (int next : graph[node]) {
            if (!validColor(graph, colors, -color, next)) {
                return false;
            }
        }
        return true;
    }
    
}
