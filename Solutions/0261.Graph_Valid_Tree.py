/*
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.

 

Example 1:


Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
Example 2:


Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
 

Constraints:

1 <= n <= 2000
0 <= edges.length <= 5000
edges[i].length == 2
0 <= ai, bi < n
ai != bi
There are no self-loops or repeated edges.
*/

//BFS: python version
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return True
        
        #edge = n - 1
        if n != len(edges) + 1:
            return False
        
        #not exist circle
        # 图的实现方法是使用a dictionary of adjacency nodes，key是int表示节点, value是set(int)表示该节点所连接的相邻节点。
        graph = collections.defaultdict(list)  # 这里必须声明是一个list, 否则后面append会报错
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        visited = set()   # 与二叉树的BFS相比多加了一行visited
        self._bfs(graph, visited)
        
        return len(visited) == n  # 每个节点都被访问过且都被访问过一次
    
    def _bfs(self, graph, visited):
        q = collections.deque()
        q.append(0)
        visited.add(0)  
        
        while q:
            cur = q.popleft()
            for node in graph[cur]:
                if node not in visited:
                    q.append(node)
                    visited.add(node)
        
//DFS Python version
"""
Solution: 判断图是不是一棵树（不一定非要是二叉树）需要满足两点：
1. 首先点的数目一定比边的数目多一个
2. 然后要确保no isolated node and no cycle，也即是保证每个点都能被访问且只被访问了一次，也就是visited的数目要等于节点数目!
"""
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #节点和边数 
        m = len(edges)
        if m != n - 1:
            return False
        
        graph = collections.defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        visited = set()
        self._dfs(graph, 0, visited)
        
        return len(visited) == n #每个节点都被访问过
    
    def _dfs(self, graph, cur_node, visited):
        visited.add(cur_node)
        
        for next_node in graph[cur_node]:
            if next_node not in visited:
                self._dfs(graph, next_node, visited)
        
        

//method 1: BFS

class Solution {
    public boolean validTree(int n, int[][] edges) {
        
        if (n == 0) return false;
        
        // condition 1.边的个数为点的个数减去1
        if (edges.length != n - 1) return false;
        
        Map<Integer, Set<Integer>> graph = initializeGraph(n, edges);
        
        // condition 2.通过一个点能把其他的点都找到 bfs
        Queue<Integer> queue = new LinkedList<>();
        Set<Integer> hash = new HashSet<>();
        
        queue.offer(0);
        hash.add(0);
        
        while (!queue.isEmpty()) {
            int node = queue.poll();
            for (Integer neighbor : graph.get(node)) {
                if (hash.contains(neighbor)) {
                    continue;
                }
                hash.add(neighbor);
                queue.offer(neighbor);
            }
        }
        return hash.size() == n;    
    }
    
    //初始化图，使用结构Map<Integer, HashSet<Integer>>
    private Map<Integer, Set<Integer>> initializeGraph(int n, int[][] edges) {    //初始化容易忘记
        Map<Integer, Set<Integer>> graph = new HashMap<>();
        for (int i = 0; i < n; i++) {
            graph.put(i, new HashSet<Integer>());
        }
        
        for (int i = 0; i < edges.length; i++) {
            int u = edges[i][0];
            int v = edges[i][1];
            graph.get(u).add(v);
            graph.get(v).add(u);
        }
        
        return graph;
    }
    
}

//method 2: DFS   实现：非递归
class Solution {
    public boolean validTree(int n, int[][] edges) {
        
        int m = edges.length;
        if (m != n - 1)
            return false;
    
        //create graph
        List<List<Integer>> adjacencyList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adjacencyList.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            adjacencyList.get(edge[0]).add(edge[1]);
            adjacencyList.get(edge[1]).add(edge[0]);
        }
        
        Set<Integer> visited = new HashSet<Integer>();
        Stack<Integer> stack = new Stack<>();
        stack.push(0);
        visited.add(0);
        
        while (!stack.isEmpty()) {
            int curr = stack.pop();
            for (int neighbor : adjacencyList.get(curr)) {
                if (visited.contains(neighbor)) {
                    continue;
                }
                stack.push(neighbor);
                visited.add(neighbor);
            }
        }
        return visited.size() == n;
    }
}

//method 3: DFS   实现：递归

/*
dfs的模板（递归实现）： 

def dfs(curr):
 visited.add(curr)
 for next in neighbors(curr):
     if next not in visited:
        dfs(next)
*/

class Solution {
    public boolean validTree(int n, int[][] edges) {
        
        int m = edges.length;
        if (m != n - 1)
            return false;
    
        //create graph
        List<List<Integer>> adjacencyList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adjacencyList.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            adjacencyList.get(edge[0]).add(edge[1]);
            adjacencyList.get(edge[1]).add(edge[0]);
        }
        
        Set<Integer> visited = new HashSet<Integer>();
        visited.add(0);
        dfs(adjacencyList, 0, visited);
        return visited.size() == n;
    }
    
    
    //递归定义：
    public void dfs(List<List<Integer>> adjacencyList, int curr, Set<Integer> visited) {
        visited.add(curr);
        
        //递归的拆解：
        for(int neighbor : adjacencyList.get(curr)) {
            if (visited.contains(neighbor)) {
                continue;
            }
            dfs(adjacencyList, neighbor, visited);
        }
    }
    //递归的出口
}
