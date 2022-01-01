/*
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

 

Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
*/


/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        if (head == null) {
            return head;
        }
        copyNext(head);
        copyRandom(head);
        Node copyList = splitList(head);
        return copyList;
    }
    
    
    //1.先变成1-1'-2-2'-3-3'
    private void copyNext(Node head) {
        Node curt = head;
        while (curt != null) {
            Node curtCopy = new Node(curt.val);
            curtCopy.next = curt.next;
            curt.next = curtCopy;
            curt = curt.next.next;
        }
    }
    
    //2.再复制关系
    private void copyRandom(Node head) {
        Node curt = head;
        while (curt != null) {
            if(curt.random == null) {
                curt.next.random = null;
            } else {
                curt.next.random = curt.random.next;
            }
            curt = curt.next.next;
        }
    }
    
    //3.分离 1-2-3  1’-2‘-3’
    private Node splitList(Node head) {
        Node newHead = head.next;
        while (head != null) {
            Node temp = head.next;
            head.next = temp.next;
            head = head.next;
            if (temp.next != null) {
                temp.next = temp.next.next;
            }
        }
        return newHead;
    }
}
