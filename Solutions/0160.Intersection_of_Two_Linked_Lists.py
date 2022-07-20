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

#1.暴力解法
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        while headA is not None:
            pB = headB
            while pB is not None:
                if headA == pB:
                    return headA
                pB = pB.next
            headA = headA.next

        return None

#2.hashset   O(N+M) O(M)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodes_in_B = set()

        while headB is not None:
            nodes_in_B.add(headB)
            headB = headB.next

        while headA is not None:
            # if we find the node pointed to by headA,
            # in our set containing nodes of B, then return the node
            if headA in nodes_in_B:
                return headA
            headA = headA.next

        return None
 
 #3.Two point   O(N+M) O(1)
#refer: https://www.youtube.com/watch?v=Dk2-0A8soHw&t=173s
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        pa, pb = headA, headB
        while pa != pb:
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next
        return pa
    
        # Note: In the case lists do not intersect, the pointers for A and B
        # will still line up in the 2nd iteration, just that here won't be
        # a common node down the list and both will reach their respective ends
        # at the same time. So pA will be NULL in that case.
 
# 4.version connect head and tail 舍弃
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

    
/****************************************************java version**************************************************/ 

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
