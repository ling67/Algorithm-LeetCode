"""
Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        lens = 0
        curr = head
        tail = curr
        while curr:
            tail = curr
            curr = curr.next
            lens += 1
        
        k = lens - k % lens
        
        #find the k - rotate 
        if k == lens:
            return head
        
        dummy = ListNode(-1)
        dummy.next = head
        prev, curr = dummy, dummy.next
        for _ in range(k):
            prev = prev.next
            curr = curr.next
            
        prev.next = None
        tail.next = head
        
        return curr
