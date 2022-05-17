"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        
        #1.get mid value, then seperate it to 2 part
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        right_head = slow.next
        slow.next = None
        
        #2. reverse second part
        prev, curr = None, right_head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        right_head = prev
        
        #3. connect the 1st and 2nd half
        dummy = ListNode(-1)
        curr = dummy
        left, right = head, right_head
        while left and right:
            curr.next = left
            left = left.next
            curr = curr.next
            
            curr.next = right
            right = right.next
            curr = curr.next
        if left:
            curr.next = left
        if right:
            curr.next = right
        
        return dummy.next
