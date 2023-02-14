//用一个mapping 保存node-->node_copy. 然后一边dfs一边新建copied nodes
class Solution {
    public Node cloneGraph(Node node) {
        if (node == null) return node;
        Map<Node, Node> mapping = new HashMap<>();
        Node newNode = new Node(node.val);
        mapping.put(node, newNode);
        dfs(node, mapping);
        return mapping.get(node);
    }

    private void dfs(Node curr, Map<Node, Node> mapping) {
        for (Node nei: curr.neighbors) {
            if (mapping.containsKey(nei)) {
                mapping.get(curr).neighbors.add(mapping.get(nei));
                continue;
            } 
            Node newNeighbor = new Node(nei.val);
            mapping.put(nei, newNeighbor);
            mapping.get(curr).neighbors.add(newNeighbor);
            dfs(nei, mapping);
        }
    }
}
