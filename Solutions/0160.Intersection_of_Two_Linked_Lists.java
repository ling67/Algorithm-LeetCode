/*
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:


The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.
*/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#version1：hashset 做很快
# version2： connect head and tail
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headA.next or not headB or not headB.next:
            return None
        
        # step 1: hook up head and tail of list B
        curr = headB;
        while curr.next:
            curr = curr.next
        curr.next = headB
        
        slow, fast = headA, headA
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
                
        if slow != fast:
            curr.next = None
            return None
        
        curr1, curr2 = headA, slow
        while curr1 != curr2:
            curr1 = curr1.next
            curr2 = curr2.next
            
        curr.next = None
        
        return curr1

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA == null || headB == null) {
            return null;
        }
        
        //将B的头尾相连
        ListNode curt = headB;
        while (curt.next != null) {
            curt = curt.next;
        }
        curt.next = headB;
        
        ListNode result = listCycleII(headA);
        curt.next = null;
        return result;
    }

    private ListNode listCycleII(ListNode head) {
        
        ListNode slow = head;
        ListNode quick = head;
        
        while (quick != null && quick.next != null) {
            slow = slow.next;
            quick = quick.next.next;
            if (slow == quick) {                
                //求相交的点
                ListNode curr = head;
                while (curr != slow) {
                    curr = curr.next;
                    slow = slow.next;
                }
                return curr;                   
            }
        }
        return null;
    }
}
