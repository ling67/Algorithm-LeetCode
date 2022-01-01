/*
Given the head of a singly linked list, reverse the list, and return the reversed list.
Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
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

//non-recursion
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curt = head;
        
        while (curt != null) {
            ListNode temp = curt.next;
            curt.next = prev;
            prev = curt;
            curt = temp;
        }
        return prev;
    }
}

//recursion
class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode second_node = head.next;
        ListNode reversed_head = reverseList(second_node);  // 递归调用，返回的是已经revere好了的head
        second_node.next = head;
        head.next = null;
        return reversed_head;
    }
}





