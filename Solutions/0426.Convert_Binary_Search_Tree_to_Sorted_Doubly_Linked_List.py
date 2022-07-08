/*
Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.

 

Example 1:



Input: root = [4,2,5,1,3]


Output: [1,2,3,4,5]

Explanation: The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.

Example 2:

Input: root = [2,1,3]
Output: [1,2,3]

*/



"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return
        
        self.head, self.curr = None, None   # 定义两个全局变量head和curr，head记录最小的节点，curr一直往后遍历到最大的节点
        self.inOrder(root)
        
        # 将最小节点和最大节点hook up起来，完成闭环
        self.head.left = self.curr
        self.curr.right = self.head
        
        return self.head
    
    def inOrder(self, root):
        """in order traversal the tree without return, update the DLL"""
        if not root:
            return
        
        # 中序遍历，先遍历左边
        self.inOrder(root.left)
        
        # 中序遍历，遍历中间，在这里update DLL
        if not self.head:
            # 此时如果 first 为空的话，说明当前就是最左结点，赋值给 first
            # 也许使用dummy node可以省掉这一步
            self.head = root
            self.curr = root
            
        else:
            # curr 代表相邻两个节点中靠前的节点，root代表靠后的节点，将两个节点hook up起来即可
            self.curr.right = root
            root.left = self.curr
            self.curr = root    # curr 往前遍历
        
        # 中序遍历，遍历右边
        self.inOrder(root.right)

/*****************************************Java Version*****************************************/
        
/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val,Node _left,Node _right) {
        val = _val;
        left = _left;
        right = _right;
    }
};
*/     

class ResultType {
    public Node first, last;
    public ResultType(Node first, Node last) {
        this.first = first;
        this.last = last;
    }
}

public class Solution {
    
    Node first = null;
    Node last = null;
    
    public Node treeToDoublyList(Node root) {
        if (root == null) return null;
        help(root);
        last.right = first;
        first.left = last;
        return first;
    }
    
    //return first last node
    private void help(Node root) {

        if (root != null) {
            //left
            help(root.left);
            if (last != null) {
                last.right = root;
                root.left = last;
            } else {
                first = root;
            }
            last = root;
            help(root.right);
        }
    }
}
