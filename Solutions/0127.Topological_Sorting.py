/*
描述
给定一个有向图，图节点的拓扑排序定义如下:

对于图中的每一条有向边 A -> B , 在拓扑排序中A一定在B之前.
拓扑排序中的第一个节点可以是图中的任何一个没有其他节点指向它的节点.
针对给定的有向图找到任意一种拓扑排序的顺序.

你可以假设图中至少存在一种拓扑排序
有关图的表示详情请看这里

图结点的个数 <= 5000
样例
样例 1：

输入：

graph = {0,1,2,3#1,4#2,4,5#3,4,5#4#5}
输出：

[0, 1, 2, 3, 4, 5]
解释：

图如下所示:

picture

拓扑排序可以为:
[0, 1, 2, 3, 4, 5]
[0, 2, 3, 1, 5, 4]
...
您只需要返回给定图的任何一种拓扑顺序。

挑战
能否分别用BFS和DFS完成？
*/

1.BFS - Python
"""
class DirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here

        # 1. collect indgree information of each node an store in a dict
        in_degree = collections.defaultdict(int)
        for node in graph:
            if node not in in_degree:
                in_degree[node] = 0
            for n in node.neighbors:
                in_degree[n] += 1

        #2. topological sorting -bfs
        q = collections.deque()
        for node in graph:
            if in_degree[node] == 0:
                q.append(node)
        res = []        
        while q:
            curr = q.popleft()
            res.append(curr)
            for next_node in curr.neighbors:
                in_degree[next_node] -= 1
                if in_degree[next_node] == 0:
                    q.append(next_node)
        return res




/**
 * Definition for Directed graph.
 * class DirectedGraphNode {
 *     int label;
 *     List<DirectedGraphNode> neighbors;
 *     DirectedGraphNode(int x) {
 *         label = x;
 *         neighbors = new ArrayList<DirectedGraphNode>();
 *     }
 * }
 */

public class Solution {
    /**
     * @param graph: A list of Directed graph node
     * @return: Any topological order for the given graph.
     */
    public ArrayList<DirectedGraphNode> topSort(ArrayList<DirectedGraphNode> graph) {
        // write your code here

        ArrayList<DirectedGraphNode> order = new ArrayList<>();

        if (graph == null) {
            return order;
        }

        //1.count indegree
        Map<DirectedGraphNode, Integer> indegree = getIndegree(graph); 

        //2.topological sorting - put all nodes that indgree = 0 into queue bfs 为什么不需要hashset，因为靠的是indegree中是否为0控制的是否进入队列，不可能两次为0
        Queue<DirectedGraphNode> queue = new LinkedList<>();
        for (DirectedGraphNode node : graph) {
            if (indegree.get(node) == 0) {
                queue.offer(node);
                order.add(node);
            }
        }
        
        while (!queue.isEmpty()) {
            DirectedGraphNode node = queue.poll();
            for (DirectedGraphNode neighbor : node.neighbors) {
                indegree.put(neighbor, indegree.get(neighbor) - 1);
                if (indegree.get(neighbor) == 0) {
                    queue.offer(neighbor);
                    order.add(neighbor);
                }
            }
        }

        return order;
    }

    private Map<DirectedGraphNode, Integer> getIndegree(ArrayList<DirectedGraphNode> graph) {
        Map<DirectedGraphNode, Integer> indegree = new HashMap<>();
        for (DirectedGraphNode node : graph) {
            indegree.put(node, 0);
        } 
        for (DirectedGraphNode node : graph) {
            for (DirectedGraphNode neighbor : node.neighbors) {
                indegree.put(neighbor, indegree.get(neighbor) + 1);
            }
        }
        return indegree;
    }
}

//修改程序，如果没有对应的拓扑排序，输出为null
public class Solution {
    /**
     * @param graph: A list of Directed graph node
     * @return: Any topological order for the given graph.
     */
    public ArrayList<DirectedGraphNode> topSort(ArrayList<DirectedGraphNode> graph) {
        // write your code here

        ArrayList<DirectedGraphNode> order = new ArrayList<>();

        if (graph == null) {
            return order;
        }

        //1.count indegree
        Map<DirectedGraphNode, Integer> indegree = getIndegree(graph); 

        //2.topological sorting - put all nodes that indgree = 0 into queue bfs 为什么不需要hashset，因为靠的是indegree中是否为0控制的是否进入队列，不可能两次为0
        Queue<DirectedGraphNode> queue = new LinkedList<>();
        for (DirectedGraphNode node : graph) {
            if (indegree.get(node) == 0) {
                queue.offer(node);
                order.add(node);
            }
        }
        
        while (!queue.isEmpty()) {
            DirectedGraphNode node = queue.poll();
            for (DirectedGraphNode neighbor : node.neighbors) {
                indegree.put(neighbor, indegree.get(neighbor) - 1);
                if (indegree.get(neighbor) == 0) {
                    queue.offer(neighbor);
                    order.add(neighbor);
                }
            }
        }
        
        //只有当点全部拿出来了才说明有拓扑排序
        if(order.size() == graph.size()) {
            return order;
        }
        return null;
    }

    private Map<DirectedGraphNode, Integer> getIndegree(ArrayList<DirectedGraphNode> graph) {
        Map<DirectedGraphNode, Integer> indegree = new HashMap<>();
        for (DirectedGraphNode node : graph) {
            indegree.put(node, 0);
        } 
        for (DirectedGraphNode node : graph) {
            for (DirectedGraphNode neighbor : node.neighbors) {
                indegree.put(neighbor, indegree.get(neighbor) + 1);
            }
        }
        return indegree;
    }
}






