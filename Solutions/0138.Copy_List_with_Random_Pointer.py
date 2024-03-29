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

#Solution 1 : hashmap + recursion

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.visit = {None: None}
    
    # return the copylist
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head in self.visit:
            return self.visit[head]
        node = Node(head.val, None, None)
        self.visit[head] = node
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return node

#Solution 2 : hashmap + traverse
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        dummy = Node(-1)
        new_curr = dummy
        mapping = defaultdict(Node)
        while curr:
            if curr not in mapping:
                mapping[curr] = Node(curr.val)
            new_curr.next = mapping[curr]
            
            if curr.random:
                if curr.random not in mapping:
                    mapping[curr.random] = Node(curr.random.val)
                mapping[curr].random = mapping[curr.random]
                
            curr = curr.next
            new_curr = new_curr.next
        
        return dummy.next
   
#Solution 3 : copy node in original list

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        #step1: create new node and interleave new node into original node
        curr = head
        while curr:
            curr_copy = Node(curr.val)
            curr_copy.next = curr.next
            curr.next = curr_copy
            curr = curr.next.next
            
        #step2: copy random node
        curr = head
        while curr:
            new_curr = curr.next
            if curr.random:
                new_curr.random = curr.random.next
            curr = new_curr.next
            
        #step3: seperate listnode
        dummy = Node(-1)
        curr, curr1 = head, dummy
        while curr:
            curr1.next = curr.next
            curr.next = curr.next.next
            curr = curr.next
            curr1 = curr1.next
            
        return dummy.next
        
        
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
