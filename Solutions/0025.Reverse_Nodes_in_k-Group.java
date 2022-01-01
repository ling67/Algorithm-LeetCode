/*
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
*/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        //dummy.next is always head
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        head = dummy;
        while (head != null) {
            head = reverseNextK(head, k);
        }
        return dummy.next;
    }
    
    //head -> n1 -> n2 -> n3....nk -> nk+1...
    //->翻转后 head -> nk ->nk-1 ->....n1...nk+1..
    //return n1
    //head is not null
    private ListNode reverseNextK(ListNode head, int k) {
        ListNode n1 = head.next;
        ListNode nk = head;
        for (int i = 0; i < k; i++) {
            nk = nk.next;
            if (nk == null) {
                return null;
            }
        }
        
        //reverse
        ListNode nkplus = nk.next;
        ListNode prev = null;
        ListNode curt = n1;
        while (curt != nkplus) {
            ListNode temp = curt.next;
            curt.next = prev;
            prev = curt;
            curt = temp;
        }
         
        //前后连接起来
        head.next = nk;
        n1.next = nkplus;
        return n1;
    }
}
