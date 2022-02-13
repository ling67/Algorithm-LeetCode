/*
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:


The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.
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
