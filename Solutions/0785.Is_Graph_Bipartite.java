/*
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.

*/

// 用visit记录访问过的点，True表示red color, False表示blue color，用DFS一边遍历一边检查相邻的点是不是跟当前点颜色不一样

class Solution {
    public boolean isBipartite(int[][] graph) {
        int m = graph.length;
        Map<Integer, Boolean> visited = new HashMap<>();
        
        for (int i = 0; i < m; i++) {
            if(!visited.containsKey(i)) {
                visited.put(i, true);
            }
            for(int j = 0; j < graph[i].length; j++) {
                if (visited.containsKey(graph[i][j])) {
                    if(visited.get(graph[i][j]) == visited.get(i)) {
                        return false;
                    }
                    continue;
                } else {
                    visited.put(graph[i][j], !visited.get(i));
                }
            }
        }    
        return true;
    }
}
