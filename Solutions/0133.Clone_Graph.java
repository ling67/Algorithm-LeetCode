/*
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

 

Example 1:


Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
Example 2:


Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
Example 3:

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
*/

/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

//java 对象之间不能直接用“=”赋值，两对象之间使用“=”是将引用所指地址进行赋值，而不是内存块的内容。

//

//写题的流程：不一定把细节都实现的特别完美，所以要先把主干先实现出来：主函数调用子函数，先把主函数写出来
class Solution {
    
    public Node cloneGraph(Node node) {
        if (node == null) {
            return node;
        }
       
        //通过给出的源点，找到所有的点
        ArrayList<Node> nodes = get(node);
        
        //复制所有的点,将映射关系存起来，因为要复制边的时候要用
        HashMap<Node, Node> mapping = new HashMap<>();
        for(Node n : nodes) {
            mapping.put(n, new Node(n.val)); 
        }
        
        //找到所有的边，复制每一条边
        for (Node n : nodes) {
            Node newNode = mapping.get(n);
            for (Node neighbor : n.neighbors) {
                Node newNeighbor = mapping.get(neighbor);
                newNode.neighbors.add(newNeighbor);
            }
        }
        return mapping.get(node);
    }
    
    private ArrayList<Node> get(Node node) {
        
        Queue<Node> queue = new LinkedList<Node>();
        HashSet<Node> set = new HashSet<>();
    
        queue.offer(node);
        set.add(node);
        while(!queue.isEmpty()) {
            Node head = queue.poll();
            for (Node neighbor : head.neighbors) {
                if (!set.contains(neighbor)) {
                    set.add(neighbor);
                    queue.offer(neighbor);
                }
            }
        }
        
        return new ArrayList<>(set);
    }
    
}





